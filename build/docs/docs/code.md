<a name=".pyTruthTable.pyTruthTable"></a>
## pyTruthTable.pyTruthTable

<a name=".pyTruthTable.pyTruthTable.PyTruthTable"></a>
### PyTruthTable

```python
class PyTruthTable():
 |  PyTruthTable(names=[], df=pd.DataFrame())
```

The constructor initialize a Truth Table with a list of `names` or with a custom dataframe.

Initializing with a list of `names` means generating automatically all
possible combination of `True` and `False`



**Arguments**:

- `names`: Name of the columns.
- `df`: Initial Pandas' dataframe.

**Raises**:

- `UserWarning`: If the initial `df` and `names` are specified simultaneously,
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

<a name=".pyTruthTable.pyTruthTable.PyTruthTable.set_default_spacing"></a>
#### set\_default\_spacing

```python
 | set_default_spacing()
```

By default, all symbols are spaced from the variable name.

---

<a name=".pyTruthTable.pyTruthTable.PyTruthTable.set_no_spacing"></a>
#### set\_no\_spacing

```python
 | set_no_spacing()
```

Remove spaces from column's name. By default, all symbols are spaced from the variable name.

**Examples**:

  
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

<a name=".pyTruthTable.pyTruthTable.PyTruthTable.set_default_symbols"></a>
#### set\_default\_symbols

```python
 | set_default_symbols()
```

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

<a name=".pyTruthTable.pyTruthTable.PyTruthTable.set_text_symbols"></a>
#### set\_text\_symbols

```python
 | set_text_symbols()
```

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

**Examples**:

  
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

<a name=".pyTruthTable.pyTruthTable.PyTruthTable.generator"></a>
#### generator

```python
 | generator(names=[])
```

Generate a combination of `True` and `False` columns given a list of `names`.

**Arguments**:

- `names`: Name of the columns.

**Returns**:

A dataframe with a binary combination using the list `names` .

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

<a name=".pyTruthTable.pyTruthTable.PyTruthTable.append"></a>
#### append

```python
 | append(operation, a_in, b_in="", name="")
```

Make a logical `operation` with column `a_in` and `b_in`. The new column will automatically append to the main dataframe.
The new column name can be specified with `name`.

`a_in` and `b_in` can be either a column name or number.


**Arguments**:

- `operation`: Logical operation to be executed
- `a_in`: First column. (Left side)
- `b_in`: Second column. (Right side)

**Raises**:

- `NameError`: Input column does not exist.
- `NameError`: Operation does not exist.
- `ValueError`: The operation needs `b_in` to also be specified

---

<a name=".pyTruthTable.pyTruthTable.PyTruthTable.append_df"></a>
#### append\_df

```python
 | append_df(a_dataframe)
```

Append a custom dataframe to your truth table. The number of rows of `a_dataframe` must always match the current truth table.

**Arguments**:

- `a_dataframe`: Dataframe to append

**Raises**:

- `TypeError`: The parameter should be a dataframe
- `RuntimeError`: Number of rows of dataframe must match with current truth table

---

<a name=".pyTruthTable.pyTruthTable.PyTruthTable.column"></a>
#### column

```python
 | column(operation, a_in, b_in="", name="")
```

Return a column of logical `operation` with column `a_in` and `b_in`. The new column will NOT append to the main dataframe.
The new column name can be specified with `name`.

`a_in` and `b_in` can be either a column name or number.


**Arguments**:

- `operation`: Logical operation to be executed
- `a_in`: First column. (Left side)
- `b_in`: Second column. (Right side)

**Raises**:

- `NameError`: Input column does not exist.
- `NameError`: Operation does not exist.
- `ValueError`: The operation needs `b_in` to also be specified

---

