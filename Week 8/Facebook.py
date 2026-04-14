import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

file='D:\\coding\\python\\Joy of computing using python\\Week 8\\data.xlsx'

xl=pd.ExcelFile(file)#read from excel
dfs=xl.parse(xl.sheet_names[0])#parsing the excel sheet to data frame
print(dfs.columns)  # check column names

# dfs=list(dfs['Timeline'])#removes the blank lines
print(dfs)