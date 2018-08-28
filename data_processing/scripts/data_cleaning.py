import pandas as pandas
import numpy as numpy
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer

cols = ['sentiment','id','date','query_string','user','content']
df = pandas.read_csv('./data_processing/data/training_data.16000.csv',header=None, names=cols, encoding = "ISO-8859-1", low_memory=False)

# removes unnecessary columns
df.drop(['query_string', 'date'],axis=1, inplace=True)

# replace null with "None"
df = df.where(pandas.notnull(df), "None")

# decode html symbols
df['content']=df['content'].apply(lambda data:BeautifulSoup(data , 'lxml').get_text())

# remove unnecessary white space
def remove_whitespace(data):
    tok = WordPunctTokenizer()
    words = tok.tokenize(data)
    return " ".join(words).strip()

df['content']=df['content'].apply(lambda data: remove_whitespace(data))

# save id as integers
df['id']=df['id'].astype(int)

# save file as CSV 
df.to_csv('./data_processing/data/result.csv', encoding='ISO-8859-1', index=False, header=False)
    
