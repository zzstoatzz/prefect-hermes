from flask import Flask, request
from prefect.client import get_client
from prefect.orion.schemas.core import FlowRun
from prefect.utilities.asyncutils import sync_compatible

app = Flask(__name__)


@sync_compatible
async def trigger_flow_run(deployment_id: str, params: dict) -> FlowRun:
    async with get_client() as client:
        return await client.create_flow_run_from_deployment(
            deployment_id=deployment_id, parameters=params
        )


@app.route("/askhermes", methods=["POST"])
def ask_hermes() -> dict:

    # TODO: add caching logic to prevent high volume users

    trigger_flow_run(
        deployment_id="94c8909a-9adc-42f8-a632-21f454890b6e",
        params=dict(
            end_user_id=request.form.get("user_id"), question=request.form.get("text")
        ),
    )

    return {
        "response_type": "ephemeral",
        "text": "whoaah now, hold your 🐎 🐎 ...I'm *working* on it",
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
