# -*- coding: utf-8 -*-

"""
Building my first Python package, using this tutorial as a guide:
https://python-packaging.readthedocs.io/en/latest/


"""

from pandas.core.frame import DataFrame
from numpy import nan

## Custom function definition
def group_by(df, cols, **kwargs):
    # Input validations.
    if not isinstance(df, DataFrame):
        raise ValueError("arg 'df' must be a pandas data frame")
    if not isinstance(cols, str) and not isinstance(cols, list):
        raise ValueError("arg 'cols' must be column headers to group by, as a single string or a list of strings")
    if isinstance(cols, str):
        cols = [cols]
    if not all([n in df.columns for n in cols]):
        missings = ", ".join([n for n in cols if n not in df.columns])
        raise ValueError("All input 'cols' must appear as columns in 'df'\n"\
                         "The following input col strings are not columns in df:\n"\
                         "%s" % missings)
    
    # Perform grouping operation.
    res = df.groupby([df[col].replace(nan, "NaN") for col in cols], **kwargs)
    
    return res
