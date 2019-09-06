# pyTruthTable
A python tool to create truth tables 


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