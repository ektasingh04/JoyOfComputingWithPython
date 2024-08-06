#save ur data in an excel file-- imprt pandas gives easy to use ds-- imprt nltk to process human language
#nltk gives sentiment analysis-- positive or negative or neutral texts
#use VADER- valence aware dictionary and sentiment reasoning.. takes into acc the intensty of sentiment
#download vader lexicon-acts as a dict here
#cnvrt excel to data frame with pandas (a 2d strucuture in form of table)

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')
file='datafile.xlsx'
xl=pd.ExcelFile(file)  #read from excel
dfs=xl.parse(xl.sheet_names[0])  #frst colm has data  so 0- parsing to data frame
dfs=list(dfs['Timeline']) #removes blank rows from df
print(dfs)

#without file
dfs=["i am happy.",'I am sad','life is hard','work hard','saturday,march 3,2023 at 7.34pm UTC+05:30']

sid=SentimentIntensityAnalyzer()
#skips the timeline of info
str1="UTC+05:30"  #indian timeline
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])