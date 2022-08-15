import re

import openai
from prefect import flow, task
from prefect.blocks.system import Secret
from prefect_slack import SlackCredentials
from prefect_slack.messages import send_chat_message


@task(name="Generate chat log from prefect documentation")
def parse_faq(context: str = "faq") -> str:

    avoid_strs = ["🔒", "<aside>"]

    content = Secret.load(context).get().replace("?", "? ??").replace("\n", "")

    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    md_links = link_pattern.findall(content)

    for text, link in md_links:
        content = content.replace(f"[{text}]({link})", text)

    raw_QAs = [i.split("??", 1) for i in content.strip().split("##") if i != ""]

    shareable_QAs = [i for i in raw_QAs if all(j not in i[-1] for j in avoid_strs)]

    annotated_QAs = "".join(
        map(lambda i: f"\nPerson: {i[0]}\nHermes: {i[1]}\n", shareable_QAs)
    )

    return annotated_QAs


@task(name="Solicit response from OpenAI Completion engine")
def ask(question: str, chat_log: str = None, model: str = "text-davinci-002") -> str:

    openai.api_key = Secret.load("openai-api-key").get()

    context = Secret.load("prefect-context").get()
    start_sequence = "\n\nHermes:"
    restart_sequence = "\n\nPerson:"

    prompt_text = f"""{context}{chat_log}{restart_sequence}:{question}{start_sequence}"""
    
    response = openai.Completion.create(
        engine=model,
        prompt=prompt_text,
        temperature=0, # float in [0 (deterministic, objective), 1 (reads creatively between the lines)]
        max_tokens=150, # max tokens in response
        top_p=1, # see [docs](https://beta.openai.com/docs/api-reference/completions/create#completions/create-top_p) ("Only one of Temperature and Top P should be utilised", partial derivatives baby)
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )["choices"][0]["text"]
        
    match response:
        case "":
            print('bad prompt: raise OpenAIPromptError')
            raise ValueError
        case str():
            return response
        case _:
            raise AssertionError


@flow
def respond_in_slack(question: str = "what is prefect?"):
    historical_context = parse_faq()

    response = ask(question=question, chat_log=historical_context)

    send_chat_message(
        slack_credentials=SlackCredentials(Secret.load("slack-token").get()),
        channel="#testing-slackbots",
        text=response,
    )

if __name__ == "__main__":
    respond_in_slack(question="what is the purpose of prefect?")