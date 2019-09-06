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
