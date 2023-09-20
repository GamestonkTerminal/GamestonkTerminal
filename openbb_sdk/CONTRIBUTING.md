# CONTRIBUTING - THIS IS A WORK IN PROGRESS

- [CONTRIBUTING - THIS IS A WORK IN PROGRESS](#contributing---this-is-a-work-in-progress)
  - [Get started contributing with a template](#get-started-contributing-with-a-template)
  - [Cookiecuter, a closer look](#cookiecuter-a-closer-look)
    - [Get your data](#get-your-data)
    - [SDK commands: query and output your data](#sdk-commands-query-and-output-your-data)
  - [Adding a new data point](#adding-a-new-data-point)
    - [Identify which type of data you want to add](#identify-which-type-of-data-you-want-to-add)
    - [What is the Standardization Framework?](#what-is-the-standardization-framework)
      - [Standardization Caveats](#standardization-caveats)
    - [Standard QueryParams Example](#standard-queryparams-example)
    - [Standard Data Example](#standard-data-example)
      - [Check if the standard model exists](#check-if-the-standard-model-exists)
  - [Refer to the API documentation and start developing](#refer-to-the-api-documentation-and-start-developing)
    - [How to use the standardization framework?](#how-to-use-the-standardization-framework)
      - [Query Parameters](#query-parameters)
      - [Data Output](#data-output)
      - [Build the Fetcher](#build-the-fetcher)
    - [Make the new provider visible to the SDK](#make-the-new-provider-visible-to-the-sdk)
  - [Using other extension as a dependency](#using-other-extension-as-a-dependency)
    - [Using our internal extension](#using-our-internal-extension)
    - [Adding an external extension](#adding-an-external-extension)
    - [The charting extension](#the-charting-extension)
      - [Add a visualization to an existing SDK command](#add-a-visualization-to-an-existing-sdk-command)
      - [Using the `to_chart` OBBject method](#using-the-to_chart-obbject-method)
  - [Environment and dependencies](#environment-and-dependencies)
  - [Python package](#python-package)
    - [Overview](#overview)
    - [Import time](#import-time)

## Get started contributing with a template

In order to get started contributing we have setup a Cookiecutter template that will help you get started.

Please refer to the [Cookiecutter template](https://github.com/OpenBB-finance/openbb-cookiecutter) and follow the instructions there.

This document will walk you through the steps of adding a new custom extension to the SDK. The high level steps are:

- Generate the extension structure
- Install your dependencies
- Install your new package
- Use your extension (either from Python or the API interface)

## Cookiecuter, a closer look

The Cookiecutter template generates a set of files in which we can find instructions and explanations.

> Note that the code is functional, so you can just run it and start playing with it.

### Get your data

Either from a CSV file, local database or from an API endpoint, you'll need to get your data.

If you don't want to partake in the data standardization framework, you can simply write all the logic straight inside the router file. This is usually the case when you are adding unique data that isn't easily standardizable.

Saying that, we recommend following the standardization framework, as it will make your life easier in the long run and unlock a set of features that are only available to standardized data.

When standardizing, all data is defined using two different pydantic models:

1. Define the [query parameters](openbb_sdk\sdk\provider\openbb_provider\abstract\query_params.py) model.
2. Define the resulting [data schema](openbb_sdk\sdk\provider\openbb_provider\abstract\data.py) model.

> The models can be entirely custom, or inherit from the OpenBB standardized models.
> They enforce a safe and consistent data structure, validation and type checking.

We call this the ***Know-Your-Data*** principle.

After you've defined both models, you'll need to define a `Fetcher` class which contains three methods:

1. `transform_query` - transforms the query parameters to the format of the API endpoint.
2. `extract_data` - makes the request to the API endpoint and returns the raw data.
3. `transform_data` - transforms the raw data into the defined data model.

> Note that the `Fetcher` should inherit from the [`Fetcher`](openbb_sdk\sdk\provider\openbb_provider\abstract\`Fetcher`.py) class, which is a generic class that receives the query parameters and the data model as type parameters.

After finalizing your models you need to make them visible to the SDK. This is done by adding the `Fetcher` to the `__init__.py` file of the `<your_package_name>/<your_module_name>` folder as part of the [`Provider`](openbb_sdk\sdk\provider\openbb_provider\abstract\provider.py).

Any command using the `Fetcher` class you've just defined, will be calling the `transform_query`, `extract_data` and `transform_data` methods under the hood in order to get the data and output it do the end user.

If you're not sure what's a command and why is it even using the `Fetcher` class, follow along!

### SDK commands: query and output your data

The SDK will enable you to query and output your data in a very simple way.

> Any SDK endpoint will be available both from a Python interface and the API.

The command definition on the SDK follows [FastAPI](https://fastapi.tiangolo.com/) conventions, meaning that you'll be defining **endpoints** similar to like FastAPI.

The Cookiecutter template generates for you a `router.py` file with a set of examples that you can follow, namely:

- Perform a simple `GET` and `POST` request - without worrying on any custom data definition.
- Using a custom data definition so you get your data the exact way you want it.

You can expect the following when using a `Fetcher`:

```python
@router.command(model="Example")
def model_example(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return OBBject(results=Query(**locals()).execute())
```

Let's break it down:

- `@router.command(...)` - this tells the SDK that this is a command that can be called.
- `model="Example"` - this is the name of the data model that will be used to validate the data.
- `cc: CommandContext` - this is a parameter that is passed to the command. It contains a set of user and system settings that maybe useful during the execution of the command - eg. api keys.
- `provider_choices: ProviderChoices` - all the providers that implement the `Example` `Fetcher`.
- `standard_params: StandardParams` - standardized parameters that are common to all providers that implement the `Example` `Fetcher`.
- `extra_params: ExtraParams` - this is a parameter that is passed to the command and it contains the provider specific arguments.

You only need to change the `model` parameter to the name of the `Fetcher` dictionary key that you've defined in the `__init__.py` file of the `<your_package_name>/<your_module_name>` folder.

## Adding a new data point

In the above section, we've seen how to get started with a template.

In this section, we'll be adding a new data point to the SDK. We will add a new provider with an existing [standard data](openbb_sdk\sdk\provider\openbb_provider\standard_models) model.

### Identify which type of data you want to add

In this example, we'll be adding OHLC stock data that is used by the `stocks/load` command.

Note that, if no command exists for your data, we need to add one under the right router.
Each router is categorized into different extensions (stocks, forex, crypto, etc.).

### What is the Standardization Framework?

The Standardization Framework is a set of tools and guidelines that enable the user to query and obtain data in a consistent way across several providers.

Each data model should inherit from a [standard data](openbb_sdk\sdk\provider\openbb_provider\standard_models) that is already defined in the SDK. This will unlock a set of perks that are only available to standardized data, namely:

- Can query and output data in a standardized way.
- Can expect extensions that follow standardization to work out-of-the-box.
- Can expect transparently defined schemas for the data that is returned by the API.
- Can expect consistent data types and validation.
- Will work seamlessly with other providers that implement the same standard model.

The standard models are defined under the `./sdk/core/provider/openbb_provider/standard_models/` directory.

They implement the [`QueryParams`](openbb_sdk\sdk\provider\openbb_provider\abstract\query_params.py) and [`Data`](openbb_sdk\sdk\provider\openbb_provider\abstract\data.py) models, which are the models that are used to query and output data, respectively. They are pydantic models under the hood, so you can leverage all the pydantic features such as validators.

#### Standardization Caveats

The standardization framework is a very powerful tool, but it has some caveats that you should be aware of:

- We standardize fields that are shared between two or more providers. If there is a third provider that doesn't share the same fields, we will declare it as an `Optional` field.
- When mapping the column names from a provider-specific model to the standard model, the CamelCase to snake_case conversion is done automatically. If the column names are not the same, you'll need to manually map them. (e.g. `o` -> `open`)
- The standard models are created and maintained by the OpenBB team. If you want to add a new field to a standard model, you'll need to open a PR to the SDK.

### Standard QueryParams Example

```python
class StockEODQueryParams(QueryParams, BaseSymbol):
    """Stock end of day Query."""

    start_date: Optional[date] = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: Optional[date] = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )
```

The `QueryParams` is an abstract class that just tells us that we are dealing with query parameters. The `BaseSymbol` is a helper class that contains the `symbol` field and an
upper case validator.

The SDK dynamically knows where the standard models begin in the inheritance tree, so you don't need to worry about it.

### Standard Data Example

```python
class StockEODData(Data):
    """Stock end of day price Data."""

    date: datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: float = Field(description=DATA_DESCRIPTIONS.get("volume", ""))
    vwap: Optional[PositiveFloat] = Field(description=DATA_DESCRIPTIONS.get("vwap", ""))
```

The `Data` class is an abstract class that tells us the expected output data. Here we can see a `vwap` field that is `Optional`. This is because not all providers share this field while it is shared between two or more providers.

#### Check if the standard model exists

Given the fact that there's already an endpoint for OHLCV stock data, we can check if the standard exists.

In this case, it's `StockEOD` which can be found inside the `./sdk/core/provider/openbb_provider/standard_models/` directory.

If the standard model doesn't exist:

- you won't need to inherit from it in the next steps
- all your provider-specific query parameters will be under the `**kwargs` in the python interface
- it might not work out-of-the box with other extensions that follow standardization e.g. the `charting` extension

## Refer to the API documentation and start developing

You can start developing your extension by referring to the API documentation of the provider you are interested to integrate.

### How to use the standardization framework?

#### Query Parameters

Query Parameters are the parameters that are passed to the API endpoint in order to make the request.

For the `StockEOD` example, this would look like the following:

```python

class <ProviderName>StockEODQueryParams(StockEODQueryParams):
    """<ProviderName> Stock End of Day Query.

    Source: https://www.<provider_name>.co/documentation/
    """

    # provider specific query parameters

```

> Note that, since `StockEODQueryParams` inherits from pydantic's `BaseModel`, so we can leverage validators to perform additional checks on the query parameters.

#### Data Output

The data output is the data that is returned by the API endpoint.
For the `StockEOD` example, this would look like the following:

```python

class <ProviderName>StockEODData(StockEODData):
    """<ProviderName> Stock End of Day Data.

    Source: https://www.<provider_name>.co/documentation/
    """

    # provider specific data output

```

> Note that, since `StockEODData` inherits from pydantic's `BaseModel`, so we can leverage validators to perform additional checks on the output model. A very good example of this, would be to transform a string date into a datetime object.

#### Build the Fetcher

The `Fetcher` class is responsible for making the request to the API endpoint and providing the output.

It will receive the Query Parameters, and it will return the output while leveraging the Data model.

For the `StockEOD` example, this would look like the following:

```python

class <ProviderName>StockEODFetcher(
    Fetcher[
        <ProviderName>StockEODQueryParams,
        List[<ProviderName>StockEODData],
    ]
):
    """Transform the query, extract and transform the data."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> <ProviderName>StockEODQueryParams:
        """Transform the query parameters."""

        return <ProviderName>StockEODQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: <ProviderName>StockEODQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> dict:
        """Return the raw data from the endpoint."""

        obtained_data = my_request(query, credentials, **kwargs)

        return obtained_data

    @staticmethod
    def transform_data(
        data: dict,
    ) -> List[<ProviderName>StockEODData]:
        """Transform the data to the standard format."""

        return [<ProviderName>StockEODData.parse_obj(**d) for d in data]

```

> Make sure that you're following the TET pattern when building a `Fetcher` - **Transform, Extract, Transform**.

### Make the new provider visible to the SDK

In order to make the new provider visible to the SDK, you'll need to add it to the `__init__.py` file of the `providers/<provider_name>/openbb_<provider_name>/` folder.

```python

"""<Provider Name> Provider module."""
from openbb_provider.abstract.provider import Provider

from openbb_<provider_name>.models.stock_eod import <ProviderName>StockEODFetcher

<provider_name>_provider = Provider(
    name="<provider_name>",
    website="<URL to the provider website>",
    description="Provider description goes here",
    required_credentials=["api_key"],
    `Fetcher`_dict={
        "StockEOD": <ProviderName>StockEODFetcher,
    },
)

```

If the provider does not require any credentials, you can simply omit it. On the other hand if it requires more than 2 items to authenticate, you can simply add a list of all the required items to the `required_credentials` list.

After running `pip install .` on `openbb_sdk/providers/<provider_name>` your provider should be ready for usage, both from the Python interface and the API.

## Using other extension as a dependency

We can use internal and external extensions with the custom developed extension and bundle it as a dependency.

### Using our internal extension

We will use the `openbb-qa` extension by utilizing its `summary` endpoint.

To create a `period_summary_example` endpoint we need to add the following to the `router.py` file:

```python
from typing import List
from openbb_provider.abstract.data import Data
from openbb_core.app.utils import basemodel_to_df, df_to_basemodel
from openbb_qa.qa_router import summary


@router.command(methods=["POST"])
def period_summary_example(
    data: List[Data],
    target: str,
    start_date: str,
    end_date: str,
) -> OBBject[dict]:
    """Example Data."""

    df = basemodel_to_df(data)
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    df = df.reset_index(drop=True)
    target_data = df_to_basemodel(df)
    results = summary(target_data, target=target)

    return OBBject(results=results.results)
```

Here we are using two vital utility functions - `basemodel_to_df` and `df_to_basemodel`. The function `basemodel_to_df` converts the data to a pandas dataframe and `df_to_basemodel` converts the dataframe back to the `Data` model.

### Adding an external extension

To add the `openbb-charting` charting extension as a dependency, you'll need to add it to the `pyproject.toml` file:

<!-- TODO: Change the version to match the stable release -->
```toml
[tool.poetry.dependencies]
openbb-charting = "^0.0.0a1"
```

Then execute the command `poetry install` in the root of your extension to install the new dependency.

### The charting extension

> In theory the same principles apply to any other extension.

#### Add a visualization to an existing SDK command

One should first ensure that the already implemented endpoint is available in the [charting router](openbb_sdk/extensions/charting/openbb_charting/charting_router.py).

To do so, you can run:
 `python openbb_sdk/extensions/charting/openbb_charting/builder.py` - which will read all the available endpoints and add them to the charting router.

Afterwards, you'll need to add the visualization to the [charting router](openbb_sdk/extensions/charting/openbb_charting/charting_router.py). The convention to match the endpoint with the respective charting function is the following:

- `stocks/load` -> `stocks_load`
- `ta/ema` -> `ta_ema`

When you spot the charting function on the charting router file, you can add the visualization to it.

The implementation should leverage the already existing classes and methods to do so, namely:

- `OpenBBFigure`
- `OpenBBFigureTable`
- `PlotlyTA`

Note that the return of each charting function should respect the already defined return types: `Tuple[OpenBBFigure, Dict[str, Any]]`.

The returned tuple contains a `OpenBBFigure` that is an interactive plotly figure that can be used in a Python interpreter, and a `Dict[str, Any]` that contains the raw data leveraged by the API.

After you're done implementing the charting function, you can simply use either the Python interface or the API to get the chart. To do so, you'll only need to set the already available `chart` argument to `True`.

Refer to the charting extension [documentation](openbb_sdk/extensions/charting/README.md) for more information on usage.

#### Using the `to_chart` OBBject method

The `OBBject` is the custom OpenBB object that is returned by the SDK commands.
It implements a set of `to_<something>` functions that enable the user to easily transform the data into a different format.

The `to_chart` function should be taken as an advanced feature, as it requires the user to have a good understanding of the charting extension and the `OpenBBFigure` class.

The user can use any number of `**kwargs` that will be passed to the `PlotlyTA` class in order to build custom visualizations with custom indicators and similar.

Refer to the [`to_chart` implementation](openbb_sdk/extensions/charting/openbb_charting/core/to_chart.py) for further details.

> Note that, this method will only work to some limited extent with data that is not standardized.
> Also, it is designed only to handle time series data.

## Environment and dependencies

In order to contribute to the SDK you need to setup your environment in order to ensure a smooth development experience.

<details>
<summary>Need help setting up Miniconda or Git?</summary>

Sometimes installing Miniconda or Git can be a bit tricky, so we've prepared a set of instructions to help you get started.

Please refer to [OpenBBTerminal docs](https://docs.openbb.co/terminal/installation/pypi) for more information.
</details>

1. Clone the repository:

    ```bash
    git clone git@github.com:OpenBB-finance/OpenBBTerminal.git
    ```

2. Create and activate a virtual environment:

    > Supported python versions: python = ">=3.8,<3.12"

    ```bash
    conda create -n "obb-sdk" python=3.9.13
    conda activate obb-sdk
    ```

3. Manage your environment with [Poetry](https://python-poetry.org/):

    ```bash
    pip install poetry
    ```

4. Install the `openbb-core`:

    ```bash
    cd OpenBBTerminal/openbb_sdk/sdk/core/
    poetry install
    ```

5. Install dependencies:

    ```bash
    cd OpenBBTerminal/openbb_sdk/extensions/stocks/ # or any other extension
    poetry install
    ```

> When installing the dependencies using poetry we ensure that dependencies are being installed in editable mode, which is the most straightforward way to develop on top of the SDK.

<details>
<summary>Install all dependencies in editable mode at once</summary>

For development purposes, one can install every available extension by running a custom shell script:

Navigate to `/OpenBBTerminal/openbb_sdk`

Run `./install_all.sh` for Linux/mac or `install_all.bat` for Windows.
</details>

> In order to install any other custom extension or provider, you'd follow the exact same steps as above.

## Python package

### Overview

One of the interfaces we provide to users is the `openbb` python package.

The code you will find in this package is generated from a script and it is just a
wrapper around the `openbb-core` and any installed extensions.

When the user runs `import openbb`, `from openbb import sdk` or other variants, the
script that generates the package code is triggered. It detects if there are new openbb
extensions installed in the environment and rebuilds the package code accordingly. If
new extensions are not found it just uses the current package version.

When you are developing chances are you want to manually trigger the package rebuild.
You can do that with:

```python
python -c "import openbb; openbb.build()"
```

### Import time

We aim to have a short import time for the package. To measure that we use `tuna`.

- https://pypi.org/project/tuna/

To visualize the import time breakdown by module and find potential bottlenecks, run the
following commands from `openbb_sdk` directory:

```bash
pip install tuna
python -X importtime openbb/__init__.py 2> import.log
tuna import.log
```
