# pandas-group-by

My first formal Python package. Using [this](https://python-packaging.readthedocs.io/en/latest/) tutorial as a guideline.

This package exposes one function, `group_by()`. Purpose of this function is to 
provide a drop-in replacement for `pandas.DataFrame.groupby()` that will keep 
`NaN` values in the output as a group. Currently, the Pandas `groupby()` function 
will drop `NaN`'s from the set of groups, and I don't see a native way around this.
`group_by()` can take all of the same optional input arguments as the Pandas version. 
It can also group by multiple columns.

## Installation

Clone this repo locally.
```sh
git clone https://github.com/ChrisMuir/pandas-group-by.git
```

Install using `pip`.
```sh
cd pandas-group-by
pip install .
```

## Example Useage

```py
from pandas_group_by import group_by
import pandas as pd
import numpy as np
```

Create a data frame, upon which we will run some examples.
```py
df = pd.DataFrame({
    "color": ["brown", "orange", "brown", "orange", "brown", "orange"], 
    "animal": [np.nan, "dog", "cat", "cat", "dog", "cat"]
})
```

Doing a `pandas.DataFrame.groupby()` operation on data that contains `NaN` values, 
the missing values are dropped during the call to `groupby()`.
```py
test = df.groupby("animal").size()
print(test)
```
```
animal
cat    3
dog    2
dtype: int64
```

If we use the custom `group_by()` function on the same data set that contains 
`NaN` values, it will preserve the missing values and list them in the summary 
stats table.
```py
test = group_by(df, "animal").size()
print(test)
```
```
animal
NaN    1
cat    3
dog    2
dtype: int64
```

`group_by()` is designed to take all of the same optional args as `pandas.DataFrame.groupby()`. 
This example is using args `as_index` and `squeeze`.
```py
test = group_by(df, "animal", as_index = False, squeeze = True).size()
print(test)
```
```
animal
NaN    1
cat    3
dog    2
dtype: int64
```

`group_by()` can also take multiple column headers as args. Add `color` as an example.
```py
test = group_by(df, ["animal", "color"]).size()
print(test)
```
```
animal  color 
NaN     brown     1
cat     brown     1
        orange    2
dog     brown     1
        orange    1
dtype: int64
```