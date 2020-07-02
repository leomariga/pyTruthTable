## Initializing a truth table

pyTruthTable uses Pandas Dataframe in its structure. The library enables initialization of truth tables so all possible combinations of `true` and `false` are ready-to-use to create relations. There are two way of initializing a truth table:

### Method 1 - Use a String array

``` python
import pyTruthTable as ptt

tt = ptt.PyTruthTable(["A", "B"])
tt.table_df
```

Will result:

|   A   |   B   |
|:-----:|:-----:|
|  True |  True |
|  True | False |
| False |  True |
| False | False |

Remember: You can always get your main truth table using `tt.table_df`.

### Method 2 - Use your own custom dataframe

``` python
import pyTruthTable as ptt
import pandas as pd

# Create a custom dataframe to use as input
dataf = pd.DataFrame({'A':[True, True, False, False],
                   'B':[True, False, True, False]})

# Use 'df' parameter to initialize the truth table
tt = ptt.PyTruthTable(df=dataf)

tt.table_df

```

Will result:

|   A   |   B   |
|:-----:|:-----:|
|  True |  True |
|  True | False |
| False |  True |
| False | False |


## Creating relations
### Appending a new column
The logical relation between two columns can be computed using `append(.)`. The first parameter is the logic operation followed by the first and second argument.

``` python
import pyTruthTable as ptt

tt = ptt.PyTruthTable(["A", "B"])
tt.append("and", "A", "B") 
```

|     A |     B | A ^ B |
|------:|------:|------:|
| True  | True  | True  |
| True  | False | False |
| False | True  | False |
| False | False | False |


### Indexing
You can reference the existing columns with both column `name` or `index`.

``` python
import pyTruthTable as ptt

tt = ptt.PyTruthTable(["A", "B"])
tt.append("not", 0) # Column 0 = "A"
tt.append("or", "B", -1) # Index = -1 means the last column (not_A)
```

|     A |     B |   ¬ A | B v (¬ A) |
|------:|------:|------:|----------:|
| True  | True  | False | True      |
| True  | False | False | False     |
| False | True  | True  | True      |
| False | False | True  | True      |


### Renaming a column
The new column will always be named automaticaly with the operation, howerver you can specify the name for the new column.

``` python
import pyTruthTable as ptt

tt = ptt.PyTruthTable(["A", "B"])
tt.append("not", 0, name="Banana") # Banana = Not A
tt.append("nand", "Banana", "A") 
```

|   A   |   B   | Banana | ¬ ((Banana) ^ A) |
|:-----:|:-----:|:------:|:----------------:|
|  True |  True |  False |       True       |
|  True | False |  False |       True       |
| False |  True |  True  |       True       |
| False | False |  True  |       True       |

### Generate a column without append
You can use `column(.)` to only calculate and return the new column, without it being added to your main truth table `table_df`. 


``` python
import pyTruthTable as ptt

tt = ptt.PyTruthTable(["A", "B"])
tt.column("and", "A", "B")
```
Will return:

| A ^ B |
|------:|
| True  |
| False |
| False |
| False |

### Appending a new dataframe to the existing one

You can append a custom dataframe using `append_df(.)`.

The number of rows of each column must be the same.

``` python

import pyTruthTable as ptt
import pandas as pd

# Initialize truth table
tt = ptt.PyTruthTable(["A", "B"])

# Define your dataframe
dataf = pd.DataFrame({'C':[True, True, False, False],
                   'D':[True, False, True, False]})

# Append the new df
tt.append_df(dataf)

tt.table_df
```

|   A   |   B   |   C   |   D   |
|:-----:|:-----:|:-----:|:-----:|
|  True |  True |  True |  True |
|  True | False |  True | False |
| False |  True | False |  True |
| False | False | False | False |