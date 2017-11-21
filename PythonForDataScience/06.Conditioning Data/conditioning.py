#Get, aggregate, create subsets, clean, and merge
from lxml import objectify
import pandas as pd
import numpy as np
import datetime as dt

#reads and manipulates xml file
def pandasStuff():
    xml = objectify.parse(open('books.xml'))
    root = xml.getroot()
    df = pd.DataFrame(columns=('author','title','genre','price','publish_date'))
    for i in range(0,6):
        obj = root.getchildren()[i].getchildren()
        row = dict(zip(['author','title','genre','price','publish_date'],
                       [obj[0].text,obj[1].text,obj[2].text,obj[3].text,obj[4].text,obj[5].text]))
        rows = pd.Series(row)
        rows.name = i
        df = df.append(rows)
    search = pd.DataFrame.duplicated(df)
    print(df)
    print('')
    print(df.drop_duplicates(subset = 'author'))
    print('')
    print(df.drop_duplicates(subset = 'genre'))

#Manipulation of a datamap through comparisons against a whole.
def dataMap():
    df = pd.DataFrame({'A': np.random.randint(10, size=10),
                       'B': np.random.randint(10, size=10),
                       'C': np.random.randint(10, size=10),
                       'D': np.random.randint(10, size=10),
                       'E': np.random.randint(10, size=10)})
    #print(df)
    #describes the dataset by comparing values from 'A' to the values from the rest of the data
    aGroup = df.groupby('A').describe()
    print(aGroup) 
    #print(aGroup.unstack().loc[:,(slice(None),['mean','count']),])

#categorical variables
def catVar():
    colors = pd.Series(['Blue','Red','Green'], dtype='category')
    data = pd.Series(pd.Categorical(['Yellow','Green','Red','Blue','Purple'],categories=colors.tolist()))
    find = pd.isnull(data)
    
    print(colors)
    print('')
    print(data)
    print('')
    print(find[find==True])
    
#renaming levels
def renLev():
    colors = pd.Series(['Blue','Red','Green'], dtype='category')
    data = pd.Series(pd.Categorical(['Red','Green','Red','Blue','Green'],categories=colors.tolist()))
    colors.cat.categories = ['Purple','Yellow','Black']
    data.cat.categories = colors.tolist()
    print(data)

#combining levels
def combineLev():
    colors = pd.Series(['Blue','Red','Green'], dtype='category')
    data = pd.Series(pd.Categorical(['Red','Green','Red','Blue','Green'],categories=colors.tolist()))
    data.cat.categories = ['BlueRed','Red','Green']
    print (data.ix[data.isin(['Red'])])
    #combined both blue and red
    data.ix[data.isin(['Red'])] = 'BlueRed'
    print (data)
    
#dates
def dateStuff():
    now = dt.datetime.now()
    timevalue = now + dt.timedelta(hours=2)
    print (str(now))
    print (now.strftime('%a, %d %B %Y'))
    print (timevalue.strftime('%H:%M:%S'))
    print (timevalue - now)
    
def main():
    #pandasStuff()
    #dataMap()
    #catVar()
    #renLev()
    #combineLev()
    dateStuff()
    
if __name__ == "__main__": main()