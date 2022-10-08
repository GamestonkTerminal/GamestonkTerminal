---
title: OpenBB Python API
geekdocCollapseSection: true
---

The OpenBB Python API was created to enable usage of the terminal functionality in python
scripts and IPython Notebooks (Jupyter). The API wraps the functionality of the terminal in a way that the Python
commands follow the same convention as the terminal.

For example `stocks/load aapl` becomes `openbb.stocks.load("aapl")`.

---

## Python environment setup

Import the OpenBB API into your python script or notebook with

```python
from openbb_terminal.api import openbb
```
This imports all the commands at once. Now you can directly begin to use it. The api function is structured in the way that it always retrieves the underlying data. For charts add the `chart=True` parameter.

For example see:

```python
# Returns data:
openbb.stocks.ba.snews("aapl")
# Returns charts:
openbb.stocks.ba.snews("aapl", chart=True)
```

This allows easy integration to the jupyter notebook and allows you to build new applications on top of the terminal. The api also has new functionalities that are used in the backend of the Terminal (CLI). With these backend functions you can develop new functionalities and avoid copy-pasting the code from the repository.


## Understanding the API functions

To understand the parameters of an API function the simplest way is to refer to the
docstring. Docstrings can be viewed using the code introspection tools of your
text/notebook editor or the built-in python `help` command. Docstrings contain both the
description of the functionality and the overview of the parameters.

As an example this is the docstring of `openbb.economy.bigmac`:

```txt
Display Big Mac Index for given countries

Parameters
----------
country_codes : List[str]
    List of country codes to get for
raw : bool, optional
    Flag to display raw data, by default False
export : str, optional
    Format data, by default ""
external_axes : Optional[List[plt.Axes]], optional
    External axes (3 axes are expected in the list), by default None
```

## Usage examples

We'd recommend checking our example notebook reports to understand how to use OpenBB API. You can find inside [reports menu](https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/reports).

### Jupyter Notebook Tricks

**Get  matplotlib charts in the output cells**\
If you copy-paste the code below and use it as your initialization then you're matplotlib graphs will be inside
the result cell.

```python
import matplotlib.pyplot as plt
import matplotlib_inline.backend_inline
from openbb_terminal.api import openbb
%matplotlib inline
matplotlib_inline.backend_inline.set_matplotlib_formats("svg")
```

**Get function signature and docstring**\
When you press `shift + tab` in jupyter notebook while having the mouse parser in an API function, you get the
signature and docstring of the function.

### Visual Studio Code Tricks

**Get function docstring and signature**\
In order to get the docstrings and function signatures for the API when opening a Jupyter Notebook in VSCode,
you have to install the [Jupyter PowerToys
extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-powertoys).

## Code Examples

Just copy-paste the code examples below into a python script or jupyter notebook, and you're ready to go.

**Basic Stock Information**\
Prints general information about the selected stock (in this case Gamsetop)

```python
from openbb_terminal.api import openbb
gme_info = openbb.stocks.fa.info("gme").transpose()
print("-- Gamstop Stock --\n\n- Basic Info -")
print(f"Sector: {gme_info['Sector'].iloc[0]}")
print(f"Country: {gme_info['Country'].iloc[0]}")
print(f"Description: {gme_info['Long business summary'].iloc[0]}")
print("\n- Financial Info -")
print(f"Ebitda Margins: {gme_info['Ebitda margins'].iloc[0]}")
print(f"Profit Margins: {gme_info['Profit margins'].iloc[0]}")
print(f"Revenue growth: {gme_info['Revenue growth'].iloc[0]}")
print("\n- Target Price -")
print(f"Current price: {gme_info['Current price'].iloc[0]}")
print(f"Target mean price: {gme_info['Target mean price'].iloc[0]}")
print(f"Target high price: {gme_info['Target high price'].iloc[0]}")
print(f"Target low price: {gme_info['Target low price'].iloc[0]}")
```

**Use external axis**\
The code below utilises the `external_axes` parameter to get two axis in one chart

```python
import matplotlib.pyplot as plt
from openbb_terminal.api import openbb
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(11, 5), dpi=150)
openbb.stocks.dps.dpotc(
    "aapl",
    external_axes=[ax1, ax2],
    chart=True,
)
fig.tight_layout()
```

**Stocks Return Distribution** \
Fetches data from the OpenBB API and then plots the return distribution. This is a good example, where the data from
the API is leveraged to build a new feature on top of the API.

```python
import numpy as np
import matplotlib.pyplot as plt
from openbb_terminal.api import openbb
# Fetches data from the api
gme = openbb.stocks.load("gme")
# Calculates logarithmic returns
gme["Log Returns"] = np.log(gme["Adj Close"]/gme["Adj Close"].shift(1))
# Plots the return distributions
gme["Log Returns"].hist(bins=1000)
plt.tight_layout()
plt.show()
```

For more examples see the OpenBB jupyter notebook reports. They all use the API to its fullest extent!

---
