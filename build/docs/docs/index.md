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

## Examples

### Example 1

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

### Example 2

```python
import pandas as pd
from pyTruthTable import * #Import all methods from pyTruthTable

data = {'Hot':[True, True,True, True, False, False, False, False], # 0
        'Wet':[True, True, False, False, True, True, False, False], # 1
        'Rains':[True, False, True, False, True, False, True, False]} # 2
df = pd.DataFrame(data)

df = df.join(l_and(df,0,1)) # 3
df = df.join(l_implies(df,3,2)) # 4
df
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hot</th>
      <th>Wet</th>
      <th>Rains</th>
      <th>(Hot) ^ (Wet)</th>
      <th>((Hot) ^ (Wet)) → (Rains)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>3</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>4</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>5</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>6</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>