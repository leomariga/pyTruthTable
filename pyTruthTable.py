import pandas as pd

# If the sentence is long, put parenthesis
def p(st):               # Put parenthesis if necessary
    if(len(st) >1):
        st = "("+ st +")"
    return st

# Uses the implication definition for logical implies
def implies(a, b):       # Definition of implication
    return (~a) | b

# Adds a new collumn in a pandas' dataframe with "a implies b"
def l_implies(df, a, b): # input the name of the column or the index
    nomecoluna = p(df.columns[a]) + " → " + p(df.columns[b])
    return pd.DataFrame({nomecoluna:implies(df.iloc[:,a], df.iloc[:,b])})

# Adds a new collumn in a pandas' dataframe with "not a"
def l_not(df, a):        # input the name of the column or the index
    nomecoluna = "¬" + p(df.columns[a])
    return pd.DataFrame({nomecoluna:(~df.iloc[:,a])})

# Adds a new collumn in a pandas' dataframe with "a and b"
def l_and(df, a, b):     # input the name of the column or the index
    nomecoluna = p(df.columns[a])+ " ^ " + p(df.columns[b])
    return pd.DataFrame({nomecoluna:(df.iloc[:,a] & df.iloc[:,b])})

# Adds a new collumn in a pandas' dataframe with "a or b"
def l_or(df, a, b):      # input the name of the column or the index
    nomecoluna = p(df.columns[a])+ " v " + p(df.columns[b])
    return pd.DataFrame({nomecoluna:(df.iloc[:,a] | df.iloc[:,b])})

# Adds a new collumn in a pandas' dataframe with "a equals b"
def l_equals(df, a, b):      # input the name of the column or the index
    nomecoluna = p(df.columns[a])+ " ↔ " + p(df.columns[b])
    return pd.DataFrame({nomecoluna:(df.iloc[:,a] == df.iloc[:,b])})
