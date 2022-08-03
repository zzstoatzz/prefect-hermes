# prefect-hermes

## Welcome!

Friend to seekers of knowledge

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-hermes` with `pip`:

```bash
pip install prefect-hermes
```

### Write and run a flow

```python
from prefect import flow
from prefect_hermes.tasks import (
    goodbye_prefect_hermes,
    hello_prefect_hermes,
)


@flow
def example_flow():
    hello_prefect_hermes
    goodbye_prefect_hermes

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-hermes`, feel free to open an issue in the [prefect-hermes](https://github.com/zzstoatzz/prefect-hermes) repository.

If you have any questions or issues while using `prefect-hermes`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-hermes` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/zzstoatzz/prefect-hermes.git

cd prefect-hermes/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
