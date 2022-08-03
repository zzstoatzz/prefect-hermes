from prefect import flow

from prefect_hermes.tasks import goodbye_prefect_hermes, hello_prefect_hermes


def test_hello_prefect_hermes():
    @flow
    def test_flow():
        return hello_prefect_hermes()

    result = test_flow()
    assert result == "Hello, prefect-hermes!"


def goodbye_hello_prefect_hermes():
    @flow
    def test_flow():
        return goodbye_prefect_hermes()

    result = test_flow()
    assert result == "Goodbye, prefect-hermes!"
