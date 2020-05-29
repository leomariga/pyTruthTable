<div align="center">
  <img src="https://raw.githubusercontent.com/leomariga/pyTruthTable/master/doc/logo.png"><br>
</div>

-----------------
[![PyPI Latest Release](https://img.shields.io/pypi/v/pyTruthTable.svg?style=for-the-badge)](https://pypi.org/project/pyTruthTable/)
[![Package Status](https://img.shields.io/pypi/status/pyTruthTable?style=for-the-badge)](https://pypi.org/project/pyTruthTable/)
[![License](https://img.shields.io/pypi/l/pyTruthTable.svg?style=for-the-badge)](https://github.com/leomariga/pyTruthTable/blob/master/LICENSE)

# What is pyTruthTable?
**_pyTruthTable_** is a library that uses Pandas' dataframe to create logical relations between it's elements. The library provides a big set of operations, automatic name generation, and with highly customizible appearence.

## Installation

```
pip3 install pyTruthTable
```

## Example

``` python
import pyTruthTable as ptt

# Intialise first columns.
tt = ptt.PyTruthTable(["Hot", "Wet", "Rains"])

# Append new column with specified operation
tt.append("and", "Hot", "Wet")
tt.append("implies", 3, "Rains")
```

| Hot   | Wet   | Rains | Hot ^ Wet | (Hot ^ Wet) → (Rains) |
|-------|-------|-------|-----------|-----------------------|
| True  | True  | True  | True      | True                  |
| True  | True  | False | True      | False                 |
| True  | False | True  | False     | True                  |
| True  | False | False | False     | True                  |
| False | True  | True  | False     | True                  |
| False | True  | False | False     | True                  |
| False | False | True  | False     | True                  |
| False | False | False | False     | True                  |