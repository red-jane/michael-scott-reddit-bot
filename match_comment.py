import pandas as pd
import re
import snowballstemmer

DF = pd.read_csv("quotes.csv")

def process_string(string):
    reg = re.compile('[^a-zA-Z ]')
    string = reg.sub('', string.lower())
    stemmer = snowballstemmer.stemmer('english')
    return stemmer.stemWords(string.split())

def get_quote(comment): 
    for row in DF.sample(frac=1).iterrows():
        keywords = row[1][1]
        for keyword in keywords.split(", "):
            kw = process_string(keyword)
            if set(kw) <= set(process_string(comment)):
                print('MATCHED : %s'%( keyword))
                return row[1][0]

