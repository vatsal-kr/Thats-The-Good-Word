# make all necessary imports
import gensim
import json
import pandas as pd
import numpy as np
from gensim.models.word2vec import Word2Vec
import gensim.downloader as api
import nltk
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

from utils import isplural, ttgw

# load the WordNet model
model = api.load('word2vec-google-news-300')

# load the suffix and prefix exceptions separately
exceptions_sufffix = pd.read_excel('WTGW_Exceptions.xlsx', sheet_name=1)
exceptions_prefix = pd.read_excel('WTGW_Exceptions.xlsx', sheet_name=0)

# create a mapping of the respective prefix and the clue passed
exceptions_prefix_dct={}
for i, row in exceptions_prefix.iterrows():
  exceptions_prefix_dct[str(row['Clue']).lower()] = row['Prefix']
