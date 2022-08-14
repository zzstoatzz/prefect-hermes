from flask import Flask, request
from prefect.client import get_client
from prefect.utilities.asyncutils import sync_compatible

app = Flask(__name__)


@sync_compatible
async def trigger_flow_run(deployment_id: str, params: dict):
    async with get_client() as client:
        return await client.create_flow_run_from_deployment(
            deployment_id=deployment_id, parameters=params
        )


@app.route("/askhermes", methods=["POST"])
def ask_hermes():

    trigger_flow_run(
        deployment_id="94c8909a-9adc-42f8-a632-21f454890b6e",
        params=dict(question=request.form.get("text")),
    )

    return "hold your 🐎 🐎 ... working on it"


if __name__ == "__main__":
    port = 80
    app.run(host="0.0.0.0", port=port, debug=True)
