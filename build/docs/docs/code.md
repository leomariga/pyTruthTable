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

Example 1:

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

Example 2:

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

