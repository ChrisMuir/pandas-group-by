#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pandas_group_by',
      version='0.0.1',
      description='An implementation of pandas.groupby() that will keep and display NaN as a group',
      long_description=readme(),
      keywords='pandas groupby',
      url='http://github.com/ChrisMuir/pandas-group-by',
      author='Chris Muir',
      author_email='chrismuirrva@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['pandas', 'numpy'],
      test_suite='nose.collector',
      tests_require=['nose', 'pandas', 'numpy'])
