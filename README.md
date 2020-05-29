Inline-style: 
![alt text](/docs/logo.png "Logo")


# What is pyTruthTable?
This library uses Pandas's dataframe to create logical relations between it's columns. E.g. you can call `l_implies(df, n ,m)` that will return a dataframe column with the logical operation "implies" between the column `m` and `n` (`m → n`). The function also names header of the column joining both columns' name with the operation symbol. 

## How to use?
- Download the file pyTruthTable.py in this repository
- Import the methods using:
```python
from pyTruthTable import * #Import all methods from pyTruthTable
```

## Examples

### Example 1

```python
import pandas as pd
from pyTruthTable import * #Import all methods from pyTruthTable

# intialise firs columns.
df = pd.DataFrame({'A':[True, True, False, False],
                   'B':[True, False, True, False]})

# Create other collumns of the dataframe calling methods
df = df.join(l_implies(df, 0 ,1)) # Thrid   column: a->b
df = df.join(l_not(df, 1))        # Forth   column: not b
df = df.join(l_and(df, 0, 1))     # Fith    column: a and b
df = df.join(l_or(df, 0, 1))      # Sixth   column: a or b
df = df.join(l_equals(df, 4, 5))  # Seventh column: fith column <-> sixth column
print(df)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>A → B</th>
      <th>¬B</th>
      <th>A ^ B</th>
      <th>A ∨ B</th>
      <th>(A ^ B) ↔ (A ∨ B)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>1</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>3</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>

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