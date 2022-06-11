import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import string
import nltk
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('./twitter_data.csv')
print(df.head())
print(df.info())
