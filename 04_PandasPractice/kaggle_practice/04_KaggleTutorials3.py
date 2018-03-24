#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

titanic = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv")

titanic.head(5)
titanic.describe
titanic.info
titanic.dtypes

titanic.columns
titanic.index

titanic.isnull().sum()