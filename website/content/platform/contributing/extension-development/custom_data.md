---
title: Add a custom data source
sidebar_position: 2
description: This page provides comprehensive guidance on using the OpenBB Platform
  for data sourcing from a CSV file, local database or API endpoint. It details the
  standardization framework, the use of Pydantic models for data extraction, and the
  importance of the Fetcher class. It also includes steps to define FastAPI endpoints,
  and utilize OpenBB commands for data querying and output.
keywords:
- OpenBB Platform
- standardization framework
- data validation
- type checking
- data schema
- query parameters
- Fetcher class
- OpenBB commands
- FastAPI endpoints
- data extraction
- API endpoint
- CSV file
- local database
- pydantic models
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="Add a custom data source - Extension Development - Contributing | OpenBB Platform Docs" />

You will get your data either from a CSV file, local database or from an API endpoint.

If you don't want or don't need to partake in the data standardization framework, you have the option to add all the logic straight inside the router file. This is usually the case when you are returning custom data from your local CSV file, or similar. Keep in mind that we also serve the REST API and that you shouldn't send non-serializable objects as a response (e.g. a pandas dataframe).

Saying that, we highly recommend following the standardization framework, as it will make your life easier in the long run and unlock a set of features that are only available to standardized data.

When standardizing, all data is defined using two different pydantic models:

1. Define the [query parameters](https://github.com/OpenBB-finance/OpenBBTerminal/tree/feature/openbb-sdk-v4/openbb_platform/platform/provider/openbb_provider/abstract/query_params.py) model.
2. Define the resulting [data schema](https://github.com/OpenBB-finance/OpenBBTerminal/tree/feature/openbb-sdk-v4/openbb_platform/platform/provider/openbb_provider/abstract/data.py) model.

> The models can be entirely custom, or inherit from the OpenBB standardized models.
> They enforce a safe and consistent data structure, validation and type checking.

We call this the ***Know-Your-Data*** principle.

After you've defined both models, you'll need to define a `Fetcher` class which contains three methods:

1. `transform_query` - transforms the query parameters to the format of the API endpoint.
2. `extract_data` - makes the request to the API endpoint and returns the raw data.
3. `transform_data` - transforms the raw data into the defined data model.

> Note that the `Fetcher` should inherit from the [`Fetcher`](https://github.com/OpenBB-finance/OpenBBTerminal/tree/feature/openbb-sdk-v4/openbb_platform/platform/provider/openbb_provider/abstract/fetcher.py) class, which is a generic class that receives the query parameters and the data model as type parameters.

After finalizing your models, you need to make them visible to the Openbb Platform. This is done by adding the `Fetcher` to the `__init__.py` file of the `<your_package_name>/<your_module_name>` folder as part of the [`Provider`](https://github.com/OpenBB-finance/OpenBBTerminal/tree/feature/openbb-sdk-v4/openbb_platform/platform/provider/openbb_provider/abstract/provider.py).

Any command, that uses the `Fetcher` class you've just defined, will be calling the `transform_query`, `extract_data` and `transform_data` methods under the hood in order to get the data and output it do the end user.

If you're not sure what's a command and why is it even using the `Fetcher` class, follow along!

## OpenBB Platform commands

The OpenBB Platform will enable you to query and output your data in a very simple way.

> Any Platform endpoint will be available both from a Python interface and the API.

The command definition on the Platform follows [FastAPI](https://fastapi.tiangolo.com/) conventions, meaning that you'll be creating **endpoints**.

The Cookiecutter template generates for you a `router.py` file with a set of examples that you can follow, namely:

- Perform a simple `GET` and `POST` request - without worrying on any custom data definition.
- Using a custom data definition so you get your data the exact way you want it.

You can expect the following endpoint structure when using a `Fetcher` to serve the data:

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

- `@router.command(...)` - this tells the OpenBB Platform that this is a command.
- `model="Example"` - this is the name of the `Fetcher` dictionary key that you've defined in the `__init__.py` file of the `<your_package_name>/<your_module_name>` folder.
- `cc: CommandContext` - this contains a set of user and system settings that is useful during the execution of the command - eg. api keys.
- `provider_choices: ProviderChoices` - all the providers that implement the `Example` `Fetcher`.
- `standard_params: StandardParams` - standardized parameters that are common to all providers that implement the `Example` `Fetcher`.
- `extra_params: ExtraParams` - it contains the provider specific arguments that are not standardized.

You only need to change the `model` parameter to the name of the `Fetcher` dictionary key and everything else will be handled by the OpenBB Platform.
