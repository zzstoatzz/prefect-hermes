from typing import Dict, List

from prefect.blocks.core import Block


class OpenAICompletion(Block):
    """A block to store a typical Completion scheme to be used in flows.

    Args:
        engine (str): The name of the GPT engine to use for text completion.
        max_tokens (int): max number of tokens allowed in the response from the engine
        prompt (str): The full string value of the prompt to provide to the engine
        stop (List[str]): Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.
        temperature (float): spectrum of speculativeness, from deterministic (0) to creative (1)
        top_p (float): only consider the top top_p*100% tokens, only use if not using temperature and vice versa, idk partial derivatives baby [see docs](https://beta.openai.com/docs/api-reference/completions/create#completions/create-top_p)
    """

    engine: str
    max_tokens: int
    prompt: str
    stop: List[str]
    temperature: float
    top_p: int

    def to_dict(self) -> Dict:
        return {k: v for k, v in self.dict().items() if k[0] != "_"}
