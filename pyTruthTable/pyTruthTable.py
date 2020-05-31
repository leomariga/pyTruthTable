import pandas as pd
import itertools
import warnings


class PyTruthTable:

    """ 
    

    The constructor initialize a Truth Table with a list of `names` or with a custom dataframe.

        Initializing with a list of `names` means generating automatically all
        possible combination of `True` and `False`



      :param names: Name of the columns.
      :param df: Initial Pandas' dataframe.
      :raises UserWarning: If the initial `df` and `names` are specified simultaneously, 
      the table generation is ignored due to possible table dimention conflicts. Only the
      initial dataframe is used. 

      Example
      
            ``` python
            t_table = ptt.PyTruthTable(["A", "B", "C"])
            t_table.table_df
            ```
            
            |     A |     B |     C |
            |------:|------:|------:|
            | True  | True  | True  |
            | True  | True  | False |
            | True  | False | True  |
            | True  | False | False |
            | False | True  | True  |
            | False | True  | False |
            | False | False | True  |
            | False | False | False |

    ---
    """
    def __init__(self, names=[], df=pd.DataFrame()):

        self.set_default_symbols()
        self.set_default_spacing()
        self.table_df = df
        if(df.equals(pd.DataFrame())):  
            if(len(names) > 0):
                self.table_df = self.generator(names)
        else:
            if(len(names) > 0):
                warnings.warn("Initial dataframe already specified, ignoring list of names.")

    def set_default_spacing(self):
        """ 
        By default, all symbols are spaced from the variable name.

        ---
        """
        self.spacing = " "


    def set_no_spacing(self):
        """ 
        Remove spaces from column's name. By default, all symbols are spaced from the variable name.

        Example:

        ``` python
        t_table = ptt.PyTruthTable(["A"])

        t_table.append("or", 0, 0)   # Simple 'or' operation
        t_table.set_no_spacing()             # Remove spaces
        t_table.append("or", 0, 0)   # Same 'or' operation

        t_table.table_df
        ```
            
        |     A | A v A |   AvA |
        |------:|------:|------:|
        | True  | True  | True  |
        | False | False | False |

        ---
        """
        self.spacing = ""

    def set_default_symbols(self):
        """ 
        Name the new column using the default symbols.

        Notice that some operations does not contain symbols because they are a combination of other symbols.

        | Operation | Symbol |
        |-----------|--------|
        | implies   | "→"    |
        | nimplies  | "↛"    |
        | converse  | "←"    |
        | nconverse | "↚"    |
        | not       | "¬"    |
        | and       | "^"    |
        | or        | "v"    |
        | nor       | ""     |
        | xor       | "⊕"    |
        | xnor      | ""     |
        | nand      | ""     |
        | equals    | "↔"    |
        | nequals   | "↮"    |

        ---
        """
        self.symbols = {
                        "implies" : "→",
                        "nimplies" : "↛",
                        "converse" : "←",
                        "nconverse" : "↚",
                        "not" : "¬",
                        "and" : "^",
                        "or" : "v",
                        "nor" : "",
                        "xor" : "⊕",
                        "xnor" : "",
                        "nand" : "",
                        "equals" : "↔",
                        "nequals" : "↮"
                        }


    def set_text_symbols(self):
        """ 
        Name the new column using the operation name instead of symbol.

        i.e: When using `and` operation your new column will be called `A and B` instead of `A ^ B`.

        | Operation | Text           |
        |-----------|----------------|
        | implies   | "implies"      |
        | nimplies  | "not implies"  |
        | converse  | "converse"     |
        | nconverse | "not converse" |
        | not       | "not"          |
        | and       | "and",         |
        | or        | "or"           |
        | nor       | "nor"          |
        | xor       | "xor"          |
        | xnor      | "xnor"         |
        | nand      | "nand"         |
        | equals    | "equals"       |
        | nequals   | "not equals"   |

        Example:
      
        ``` python
        df = pd.DataFrame([A])

        t_table = ptt.PyTruthTable(df=df)

        t_table.append("or", 0, 0)   # Simple 'or' operation
        t_table.set_text_symbols()   # Change to text
        t_table.append("or", 0, 0)   # Same 'or' operation

        t_table.table_df
        ```
            
        |     A | A v A | A or A |
        |------:|------:|-------:|
        | True  | True  | True   |
        | False | False | False  |

        ---
        """
        self.symbols = {
                        "implies" : "implies",
                        "nimplies" : "not implies",
                        "converse" : "converse",
                        "nconverse" : "not converse",
                        "not" : "not",
                        "and" : "and",
                        "or" : "or",
                        "nor" : "nor",
                        "xor" : "xor",
                        "xnor" : "xnor",
                        "nand" : "nand",
                        "equals" : "equals",
                        "nequals" : "not equals"
                        }


    def generator(self, names=[]):   
        """ 
        Generate a combination of `True` and `False` columns given a list of `names`.

        :param names: Name of the columns.
        :returns:  A dataframe with a binary combination using the list `names` .

        Example:
      
        ``` python
        t_table = ptt.PyTruthTable()
        t_table.generator(["First", "Second"])
        ```
        
        | First | Second |
        |------:|-------:|
        | True  | True   |
        | True  | False  |
        | False | True   |
        | False | False  |

      
        ``` python
        t_table = ptt.PyTruthTable()
        t_table.generator(["First", "Second", "Third"])
        ```
        
        | First | Second | Third |
        |------:|-------:|------:|
        | True  | True   | True  |
        | True  | True   | False |
        | True  | False  | True  |
        | True  | False  | False |
        | False | True   | True  |
        | False | True   | False |
        | False | False  | True  |
        | False | False  | False |

        ---
        """
        table = list(itertools.product([True, False], repeat=len(names)))
        ddf = pd.DataFrame(table)
        for i in range(len(names)):
            ddf = ddf.rename(columns={i: names[i]})
        return ddf

    
    def p(self, st):               # Put parenthesis if necessary
        if(len(st) >3):
            st = "("+ st +")"
        return st

    
    def implies(self, a, b):       # Definition of implication
        return (~a) | b

    def nimplies(self, a, b):      
        return a & (~b)

    def verify_existence(self, nomecoluna):      
        if nomecoluna in self.table_df.columns:
            raise NameError('Column name already exists. Please, specify another name.')

    
    def l_implies(self, a, b, nomecoluna): 
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a]) + self.spacing + self.symbols["implies"] + self.spacing + self.p(self.table_df.columns[b])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:self.implies(self.table_df.iloc[:,a], self.table_df.iloc[:,b])})

    
    def l_nimplies(self, a, b, nomecoluna):
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a]) + self.spacing + self.symbols["nimplies"] + self.spacing + self.p(self.table_df.columns[b])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:self.nimplies(self.table_df.iloc[:,a], self.table_df.iloc[:,b])})

    
    def l_not(self, a, nomecoluna): 
        if(nomecoluna==""):
            nomecoluna = self.symbols["not"] + self.spacing+ self.p(self.table_df.columns[a])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:(~self.table_df.iloc[:,a])})

    
    def l_and(self, a, b, nomecoluna):
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["and"] + self.spacing + self.p(self.table_df.columns[b])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] & self.table_df.iloc[:,b])})

    
    def l_nand(self, a, b, nomecoluna):
        if(nomecoluna==""):
            if(self.symbols["nand"] == ""):
                nomecoluna = self.symbols["not"]+ self.spacing+"("+self.p(self.table_df.columns[a])+ self.spacing + self.symbols["and"] + self.spacing + self.p(self.table_df.columns[b])+")"
            else:
                nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["nand"] + self.spacing + self.p(self.table_df.columns[b])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:~(self.table_df.iloc[:,a] & self.table_df.iloc[:,b])})

    
    def l_or(self, a, b, nomecoluna):
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["or"] + self.spacing + self.p(self.table_df.columns[b])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] | self.table_df.iloc[:,b])})

    
    def l_nor(self, a, b, nomecoluna):
        if(nomecoluna==""):
            if(self.symbols["nor"] == ""):
                nomecoluna = self.symbols["not"]+ self.spacing+"("+self.p(self.table_df.columns[a])+ self.spacing + self.symbols["or"] + self.spacing + self.p(self.table_df.columns[b]) + ")"
            else:
                nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["nor"] + self.spacing + self.p(self.table_df.columns[b])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:~(self.table_df.iloc[:,a] | self.table_df.iloc[:,b])})

    
    def l_xor(self, a, b, nomecoluna):
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["xor"] + self.spacing + self.p(self.table_df.columns[b])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] ^ self.table_df.iloc[:,b])})

    
    def l_xnor(self, a, b, nomecoluna):
        if(nomecoluna==""):
            if(self.symbols["xnor"] == ""):
                nomecoluna = self.symbols["not"]+ self.spacing+"("+self.p(self.table_df.columns[a])+ self.spacing + self.symbols["xor"] + self.spacing + self.p(self.table_df.columns[b])+")"
            else:
                nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["xnor"] + self.spacing + self.p(self.table_df.columns[b])

        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:~(self.table_df.iloc[:,a] ^ self.table_df.iloc[:,b])})

    
    def l_equals(self, a, b, nomecoluna):
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["equals"] + self.spacing + self.p(self.table_df.columns[b])
        return pd.DataFrame({nomecoluna:(self.table_df.iloc[:,a] == self.table_df.iloc[:,b])})

    def l_nequals(self, a, b, nomecoluna):
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["nequals"] + self.spacing + self.p(self.table_df.columns[b])
        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:~(self.table_df.iloc[:,a] == self.table_df.iloc[:,b])})

    
    def l_converse(self, a, b, nomecoluna):
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["converse"] + self.spacing + self.p(self.table_df.columns[b])
        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:self.implies(self.table_df.iloc[:,b], self.table_df.iloc[:,a])})

        
    def l_nconverse(self, a, b, nomecoluna):
        if(nomecoluna==""):
            nomecoluna = self.p(self.table_df.columns[a])+ self.spacing + self.symbols["nconverse"] + self.spacing + self.p(self.table_df.columns[b])
        self.verify_existence(nomecoluna)
        return pd.DataFrame({nomecoluna:self.nimplies(self.table_df.iloc[:,b], self.table_df.iloc[:,a])})

    
    def append(self, operation, a_in, b_in="", name=""):
        """ 
        Make a logical `operation` with column `a_in` and `b_in`. The new column will automatically append to the main dataframe. 
        The new column name can be specified with `name`.

        `a_in` and `b_in` can be either a column name or number.


          :param operation: Logical operation to be executed
          :param a_in: First column. (Left side)
          :param b_in: Second column. (Right side)
          :raises NameError: Input column does not exist. 
          :raises NameError: Operation does not exist. 
          :raises ValueError: The operation needs `b_in` to also be specified

        ---
        """
        a = ""
        b = ""
        if isinstance(a_in, str):
            if a_in in self.table_df:
                a = self.table_df.columns.get_loc(a_in)
            else:
                raise NameError('First column does not exist.')
        else:
            a = a_in

        if(b_in != ""):
            if isinstance(b_in, str):
                if b_in in self.table_df:
                    b = self.table_df.columns.get_loc(b_in)
                else:
                    raise NameError('Second column does not exist.')
            else:
                b = b_in
        else:
            b = b_in
            if (operation != "not"):
                raise ValueError('Operation requires a second column to be defined.')
                
        if(operation == "implies"):
            self.table_df = self.table_df.join(self.l_implies(a, b, name))
        elif(operation == "nimplies"):
            self.table_df = self.table_df.join(self.l_nimplies(a, b, name))
        elif(operation == "converse"):
            self.table_df = self.table_df.join(self.l_converse(a, b, name))
        elif(operation == "nconverse"):
            self.table_df = self.table_df.join(self.l_nconverse(a, b, name))
        elif(operation == "not"):
            self.table_df = self.table_df.join(self.l_not(a, name))
        elif(operation == "and"):
            self.table_df = self.table_df.join(self.l_and(a, b, name))
        elif(operation == "or"):
            self.table_df = self.table_df.join(self.l_or(a, b, name))
        elif(operation == "nor"):
            self.table_df = self.table_df.join(self.l_nor(a, b, name))
        elif(operation == "xor"):
            self.table_df = self.table_df.join(self.l_xor(a, b, name))
        elif(operation == "xnor"):
            self.table_df = self.table_df.join(self.l_xnor(a, b, name))
        elif(operation == "nand"):
            self.table_df = self.table_df.join(self.l_nand(a, b, name))
        elif(operation == "equals"):
            self.table_df = self.table_df.join(self.l_equals(a, b, name))
        elif(operation == "nequals"):
            self.table_df = self.table_df.join(self.l_nequals(a, b, name))
        else:
            raise NameError('Operation does not exist.')
        return self.table_df

    def append_df(self, a_dataframe):
        """ 
        Append a custom dataframe to your truth table. The number of rows of `a_dataframe` must always match the current truth table.

          :param a_dataframe: Dataframe to append
          :raises TypeError: The parameter should be a dataframe
          :raises RuntimeError: Number of rows of dataframe must match with current truth table

        ---
        """
        if isinstance(a_dataframe, pd.DataFrame):
            if(len(self.table_df.index) == len(a_dataframe.index)):
                self.table_df = self.table_df.join(a_dataframe)
            else:
                raise RuntimeError('Number of rows of dataframe must match with current truth table')
                

        else:
            raise TypeError('The parameter should be a dataframe')


    def column(self, operation, a_in, b_in="", name=""):
        """ 
        Return a column of logical `operation` with column `a_in` and `b_in`. The new column will NOT append to the main dataframe. 
        The new column name can be specified with `name`.

        `a_in` and `b_in` can be either a column name or number.


          :param operation: Logical operation to be executed
          :param a_in: First column. (Left side)
          :param b_in: Second column. (Right side)
          :raises NameError: Input column does not exist. 
          :raises NameError: Operation does not exist. 
          :raises ValueError: The operation needs `b_in` to also be specified

        ---
        """
        a = ""
        b = ""
        if isinstance(a_in, str):
            if a_in in self.table_df:
                a = self.table_df.columns.get_loc(a_in)
            else:
                raise NameError('First column does not exist.')
        else:
            a = a_in

        if(b_in != ""):
            if isinstance(b_in, str):
                if b_in in self.table_df:
                    b = self.table_df.columns.get_loc(b_in)
                else:
                    raise NameError('Second column does not exist.')
            else:
                b = b_in
        else:
            b = b_in
            if (operation != "not"):
                raise ValueError('Operation requires a second column to be defined.')

        if(operation == "implies"):
            return self.l_implies(a, b, name)
        elif(operation == "nimplies"):
            return self.l_nimplies(a, b, name)
        elif(operation == "converse"):
            return self.l_converse(a, b, name)
        elif(operation == "nconverse"):
            return self.l_nconverse(a, b, name)
        elif(operation == "not"):
            return self.l_not(a, name)
        elif(operation == "and"):
            return self.l_and(a, b, name)
        elif(operation == "or"):
            return self.l_or(a, b, name)
        elif(operation == "nor"):
            return self.l_nor(a, b, name)
        elif(operation == "xor"):
            return self.l_xor(a, b, name)
        elif(operation == "xnor"):
            return self.l_xor(a, b, name)
        elif(operation == "nand"):
            return self.l_nand(a, b, name)
        elif(operation == "equals"):
            return self.l_equals(a, b, name)
        elif(operation == "nequals"):
            return self.l_nequals(a, b, name)
        else:
            raise NameError('Operation does not exist.')