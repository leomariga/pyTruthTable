## Supported operations
**_pyTruthTable_** Supports the following operations:

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

### Example all operations

        
``` python
df = pd.DataFrame({'A':[True, True, False, False],
           'B':[True, False, True, False]})

t_table = ptt.PyTruthTable(df=df)

t_table.append("not", 0)
t_table.append("and", 0, 1)
t_table.append("or", 0, 1)
t_table.append("xor", 0, 1)
t_table.append("nor", 0, 1)
t_table.append("nand", 0, 1)
t_table.append("xnor", 0, 1)
t_table.append("equals", 0, 1)
t_table.append("nequals", 0, 1)
t_table.append("implies", 0, 1)
t_table.append("nimplies", 0, 1)
t_table.append("converse", 0, 1)
t_table.append("nconverse", 0, 1)

t_table.table_df
```



|     A |     B |   ¬ A | A ^ B | A v B | A ⊕ B | ¬ (A v B) | ¬ (A ^ B) | ¬ (A ⊕ B) | A ↔ B | A ↮ B | A → B | A ↛ B | A ← B | A ↚ B |
|------:|------:|------:|------:|------:|------:|----------:|----------:|----------:|------:|------:|------:|------:|------:|------:|
| True  | True  | False | True  | True  | False | False     | False     | True      | True  | False | True  | False | True  | False |
| True  | False | False | False | True  | True  | False     | True      | False     | False | True  | False | True  | True  | False |
| False | True  | True  | False | True  | True  | False     | True      | False     | False | True  | True  | False | False | True  |
| False | False | True  | False | False | False | True      | True      | True      | True  | False | True  | False | True  | False |