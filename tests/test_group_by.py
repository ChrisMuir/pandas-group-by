#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from pandas_group_by import group_by
from pandas import DataFrame
from numpy import nan

class run_tests(TestCase):
    def test_group_by(self):
        # Create test data frame.
        df = DataFrame({
            "color": ["brown", "orange", "brown", "orange", "brown", "orange"], 
            "animal": [nan, "dog", "cat", "cat", "dog", "cat"]
        })
        
        res = group_by(df, "animal").size()
        
        self.assertTrue(res.index.name == "animal")
        self.assertTrue("NaN" in res.index.values)
        self.assertTrue(res["NaN"] == 1)