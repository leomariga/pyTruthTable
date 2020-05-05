import pandas as pd
import itertools


class PyTruthTable:

    # Initialize dataframe 
    def __init__(self, names=[], df=pd.DataFrame()):
        self.table_df = df 
        if(len(names) > 0):
            self.table_df = self.generator(names)
            


    # If the sentence is long, put parenthesis
    def generator(self, names=[]):   
        table = list(itertools.product([True, False], repeat=len(names)))
        ddf = pd.DataFrame(table)
        for i in range(len(names)):
            ddf = ddf.rename(columns={i: names[i]})
        return ddf

    # If the sentence is long, put parenthesis
    def p(self, st):               # Put parenthesis if necessary
        if(len(st) >1):
            st = "("+ st +")"
        return st

    # Uses the implication definition for logical implies
    def implies(self, a, b):       # Definition of implication
        return (~a) | b

    def nimplies(self, a, b):       # Definition of implication
        return a & (~b)

    # Adds a new collumn in a pandas' dataframe with "a implies b"
    def l_implies(self, a, b, nomecoluna): # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a]) + " → " + self.p(self.table_df.columns[b])

        return pd.DataFrame({nomecoluna:self.implies(self.table_df.iloc[:,a], self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "a nimplies b"
    def l_nimplies(self, a, b, nomecoluna): # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a]) + " ↛ " + self.p(self.table_df.columns[b])

        return pd.DataFrame({nomecoluna:self.nimplies(self.table_df.iloc[:,a], self.table_df.iloc[:,b])})

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

        # Adds a new collumn in a pandas' dataframe with "a and b"
    def l_nand(self, a, b, nomecoluna):     # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = "¬("+self.p(self.table_df.columns[a])+ " ^ " + self.p(self.table_df.columns[b])+")"

        return pd.DataFrame({nomecoluna:~(self.table_df.iloc[:,a] & self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "a or b"
    def l_or(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " v " + self.p(self.table_df.columns[b])

        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] | self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "a nor b"
    def l_nor(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = "¬("+self.p(self.table_df.columns[a])+ " v " + self.p(self.table_df.columns[b]) + ")"

        return pd.DataFrame({nomecoluna:~(self.table_df.iloc[:,a] | self.table_df.iloc[:,b])})

        # Adds a new collumn in a pandas' dataframe with "a xor b"
    def l_xor(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " ⊕ " + self.p(self.table_df.columns[b])

        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] ^ self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "a xor b"
    def l_xnor(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = "¬("+self.p(self.table_df.columns[a])+ " ⊕ " + self.p(self.table_df.columns[b])+")"

        return pd.DataFrame({nomecoluna:~(self.table_df.iloc[:,a] ^ self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "a equals b"
    def l_equals(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " ↔ " + self.p(self.table_df.columns[b])
        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] == self.table_df.iloc[:,b])})

    def l_nequals(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " ↮ " + self.p(self.table_df.columns[b])
        return pd.DataFrame({nomecoluna:~(self.table_df.iloc[:,a] == self.table_df.iloc[:,b])})

    # Adds a new collumn in a pandas' dataframe with "a equals b"
    def l_converse(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " ← " + self.p(self.table_df.columns[b])
        return pd.DataFrame({nomecoluna:self.implies(self.table_df.iloc[:,b], self.table_df.iloc[:,a])})

        # Adds a new collumn in a pandas' dataframe with "a equals b"
    def l_nconverse(self, a, b, nomecoluna):      # input the name of the column or the index
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ " ↚ " + self.p(self.table_df.columns[b])
        return pd.DataFrame({nomecoluna:self.nimplies(self.table_df.iloc[:,b], self.table_df.iloc[:,a])})

    # Append and return the dataframe with the operation
    def append(self, operation, a, b="", newcolumn_name=""):
        if(operation == "implies"):
            self.table_df = self.table_df.join(self.l_implies(a, b, newcolumn_name))
        elif(operation == "nimplies"):
            self.table_df = self.table_df.join(self.l_nimplies(a, b, newcolumn_name))
        elif(operation == "converse"):
            self.table_df = self.table_df.join(self.l_converse(a, b, newcolumn_name))
        elif(operation == "nconverse"):
            self.table_df = self.table_df.join(self.l_nconverse(a, b, newcolumn_name))
        elif(operation == "not"):
            self.table_df = self.table_df.join(self.l_not(a, newcolumn_name))
        elif(operation == "and"):
            self.table_df = self.table_df.join(self.l_and(a, b, newcolumn_name))
        elif(operation == "or"):
            self.table_df = self.table_df.join(self.l_or(a, b, newcolumn_name))
        elif(operation == "nor"):
            self.table_df = self.table_df.join(self.l_nor(a, b, newcolumn_name))
        elif(operation == "xor"):
            self.table_df = self.table_df.join(self.l_xor(a, b, newcolumn_name))
        elif(operation == "xnor"):
            self.table_df = self.table_df.join(self.l_xnor(a, b, newcolumn_name))
        elif(operation == "nand"):
            self.table_df = self.table_df.join(self.l_nand(a, b, newcolumn_name))
        elif(operation == "equals"):
            self.table_df = self.table_df.join(self.l_equals(a, b, newcolumn_name))
        elif(operation == "nequals"):
            self.table_df = self.table_df.join(self.l_nequals(a, b, newcolumn_name))
        else:
            print("Operation does not exist")
        return self.table_df

    def append_df(self, a_dataframe):
        if isinstance(a_dataframe, pd.DataFrame):

            self.table_df = self.table_df.join(a_dataframe)

        else:
            print("Variável não reconhecida")

        # Append and return the dataframe with the operation
    def column(self, operation, a, b="", newcolumn_name=""):
        if(operation == "implies"):
            return self.l_implies(a, b, newcolumn_name)
        elif(operation == "nimplies"):
            return self.l_nimplies(a, b, newcolumn_name)
        elif(operation == "converse"):
            return self.l_converse(a, b, newcolumn_name)
        elif(operation == "nconverse"):
            return self.l_nconverse(a, b, newcolumn_name)
        elif(operation == "not"):
            return self.l_not(a, newcolumn_name)
        elif(operation == "and"):
            return self.l_and(a, b, newcolumn_name)
        elif(operation == "or"):
            return self.l_or(a, b, newcolumn_name)
        elif(operation == "nor"):
            return self.l_nor(a, b, newcolumn_name)
        elif(operation == "xor"):
            return self.l_xor(a, b, newcolumn_name)
        elif(operation == "xnor"):
            return self.l_xor(a, b, newcolumn_name)
        elif(operation == "nand"):
            return self.l_nand(a, b, newcolumn_name)
        elif(operation == "equals"):
            return self.l_equals(a, b, newcolumn_name)
        elif(operation == "nequals"):
            return self.l_nequals(a, b, newcolumn_name)
        else:
            print("Operation does not exist")
            return pd.DataFrame()