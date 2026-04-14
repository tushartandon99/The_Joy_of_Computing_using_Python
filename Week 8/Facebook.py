import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

file='D:\\coding\\python\\Joy of computing using python\\Week 8\\data.xlsx'

xl=pd.ExcelFile(file)#read from excel
dfs=xl.parse(xl.sheet_names[0])#parsing the excel sheet to data frame
dfs = dfs['Timeline'].dropna().astype(str).tolist()#removes the blank lines
print(dfs)

sid=SentimentIntensityAnalyzer()
str1="UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])