"""This is an example flows module"""
from prefect import flow

from prefect_hermes.tasks import goodbye_prefect_hermes, hello_prefect_hermes


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    print(hello_prefect_hermes)
    print(goodbye_prefect_hermes)
    return "Done"
