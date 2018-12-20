#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='pandas_group_by',
      version='0.0.1',
      description='An implementation of pandas.groupby() that will keep and display NaN as a group',
      url='http://github.com/ChrisMuir/pandas-group-by',
      author='Chris Muir',
      author_email='chrismuirrva@gmail.com',
      license='MIT',
      packages=['pandas_group_by'],
      zip_safe=False, 
      install_requires=['pandas', 'numpy'])
