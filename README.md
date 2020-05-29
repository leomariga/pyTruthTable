<div align="center">
  <img src="https://raw.githubusercontent.com/leomariga/pyTruthTable/master/doc/logo.png"><br>
</div>

-----------------

# What is pyTruthTable?
**_pyTruthTable_** is a library that uses Pandas' dataframe to create logical relations between it's elements. The library provides a big set of operations and is highly customizible. The user specify the inputs for the operation and a new column is created automaticaly.

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