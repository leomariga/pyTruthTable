import pandas as pd



class PyTruthTable:

    # Initialize dataframe 
    def __init__(self, first_df=""):
        self.table_df = first_df 

    # If the sentence is long, put parenthesis
    def p(self, st):               # Put parenthesis if necessary
        if(len(st) >1):
            st = "("+ st +")"
        return st

    # Uses the implication definition for logical implies
    def implies(self, a, b):       # Definition of implication
        return (~a) | b

    # Adds a new collumn in a pandas' dataframe with "a implies b"
    def l_implies(self, a, b, nomecoluna): # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a]) + " → " + self.p(self.table_df.columns[b])

        return pd.DataFrame({nomecoluna:self.implies(self.table_df.iloc[:,a], self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "not a"
    def l_not(self, a, nomecoluna):        # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = "¬" + self.p(self.table_df.columns[a])

        return pd.DataFrame({nomecoluna:(~self.table_df.iloc[:,a])})

    # Adds a new collumn in a pandas' dataframe with "a and b"
    def l_and(self, a, b, nomecoluna):     # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " ^ " + self.p(self.table_df.columns[b])

        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] & self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "a or b"
    def l_or(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " v " + self.p(self.table_df.columns[b])

        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] | self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "a equals b"
    def l_equals(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " ↔ " + self.p(self.table_df.columns[b])
        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] == self.table_df.iloc[:,b])})

    # Append and return the dataframe with the operation
    def append(self, operation, a, b="", newcolumn_name=""):
        if(operation == "implies"):
            self.table_df = self.table_df.join(self.l_implies(a, b, newcolumn_name))
        elif(operation == "not"):
            self.table_df = self.table_df.join(self.l_not(a, newcolumn_name))
        elif(operation == "and"):
            self.table_df = self.table_df.join(self.l_and(a, b, newcolumn_name))
        elif(operation == "or"):
            self.table_df = self.table_df.join(self.l_or(a, b, newcolumn_name))
        elif(operation == "equals"):
            self.table_df = self.table_df.join(self.l_equals(a, b, newcolumn_name))
        else:
            print("Operation does not exist")
        return self.table_df

    def append_df(self, a_dataframe):
        if isinstance(a_dataframe, pd.DataFrame):
            self.table_df = self.table_df.join(a_dataframe)
        else:
            print("Variável não reconhecido")

        # Append and return the dataframe with the operation
    def column(self, operation, a, b="", newcolumn_name=""):
        if(operation == "implies"):
            return self.l_implies(a, b, newcolumn_name)
        elif(operation == "not"):
            return self.l_not(a, newcolumn_name)
        elif(operation == "and"):
            return self.l_and(a, b, newcolumn_name)
        elif(operation == "or"):
            return self.l_or(a, b, newcolumn_name)
        elif(operation == "equals"):
            return self.l_equals(a, b, newcolumn_name)
        else:
            print("Operation does not exist")
            return pd.DataFrame()