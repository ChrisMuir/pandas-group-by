# pandas-group-by

My first formal Python package. Using [this](https://python-packaging.readthedocs.io/en/latest/) tutorial as a guideline.

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
    "fixed": [1, 1, 1, 1, 1, 1], 
    "color": ["brown", "orange", "brown", "orange", "brown", "orange"], 
    "animal": [np.nan, "dog", "cat", "cat", "dog", "cat"]
})
```

Doing a `pandas.DataFrame.groupby()` operation on data that contains `NaN` values, 
the missing values are dropped during the call to `groupby()`.
```py
test = df.groupby("animal", as_index = False)["fixed"].agg([np.sum])
print(test)
```
```
        sum
animal     
cat       3
dog       2
```

# If we use the custom `group_by()` function on the same data set that contains 
`NaN` values, it will preserve the missing values and list them in the summary 
stats table.
```py
test = group_by(df, "animal", as_index = False)["fixed"].agg([np.sum])
print(test)
```
```
        sum
animal     
NaN       1
cat       3
dog       2
```

`group_by()` is designed to take all of the same optional args as `pandas.DataFrame.groupby()`. 
This example is using args `as_index` and `squeeze`.
```py
test = group_by(df, "animal", as_index = False, squeeze = True)
print(test)
```
```
        sum
animal     
NaN       1
cat       3
dog       2
```

`group_by()` can also take multiple column headers as args. Add `color` as an example.
```py
test = group_by(df, ["animal", "color"], as_index = False)["fixed"].agg([np.sum])
print(test)
```
```
               sum
animal color      
NaN    brown     1
cat    brown     1
       orange    2
dog    brown     1
       orange    1
```