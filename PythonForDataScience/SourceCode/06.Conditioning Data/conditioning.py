#Samuel L. Peoples
#Get, aggregate, create subsets, clean, and merge
from lxml import objectify
import pandas as pd
import numpy as np
import datetime as dt
from sklearn.preprocessing import Imputer

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
    #prints time right now
    print (str(now))
    #prints time as weekday, day, month, year
    print (now.strftime('%a, %d %B %Y'))
    #prints time + 2 hours
    print (timevalue.strftime('%H:%M:%S'))
    #prints time diff
    print (timevalue - now)
    
#finding missing data
def missingData():
    s = pd.Series([1, 2, 3, np.NaN, 5, 6, None])
    #prints s as table of bool tests of null
    #print (s.isnull())
    print()
    #prints just null values
    #print (s[s.isnull()])
    #Fills the null values with the mean of the series
    #print (s.fillna(int(s.mean())))
    print()
    #drops the null values alltogether
    #print (s.dropna())
    imp = Imputer(missing_values='NaN',strategy='mean', axis=0)
    imp.fit([1, 2, 3, 4, 5, 6, 7])
    #fills missings values simply, throws deprecated warning in anaconda v>.19
    x = pd.Series(imp.transform(s).tolist()[0])
    print (x)
    
#slicing rows
def slice():
    x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],],
                  [[11,12,13], [14,15,16], [17,18,19],],
                  [[21,22,23], [24,25,26], [27,28,29]]])
    #prints row 1
    print(x[0])
    #prints col 1
    print(x[:,0])
    
    #dicing
    #prints row 1, col 1
    print (x[1,1])
    #prints column 1 of column 1
    print (x[:,1,1])
    #prints the center element of each matrix
    print (x[1,:,1])
    #prints row 1 of column 1
    print (x[1:2, 1:2])
    
#transforming
def transforming():
    #creates a dataframe by column
    df = pd.DataFrame({'A': [2,3,1],
                       'B': [1,2,3],
                       'C': [5,3,4]})
    df1 = pd.DataFrame({'A': [4],
                        'B': [4],
                        'C': [4]})
    #appends df1 to df
    df = df.append(df1)
    #resets the index, otherwise df1 will have index 0
    df = df.reset_index(drop=True)
    print (df)
    #appends a different way
    df.loc[df.last_valid_index() + 1] = [5, 5, 5]
    print()
    print(df)
    #Appends a whole column
    df2 = pd.DataFrame({'D': [1, 2, 3, 4, 5]})
    df = pd.DataFrame.join(df, df2)
    print()
    print(df)
    #kills a row
    df = df.drop(df.index[[1]])
    print (df)
    #kills a col
    df = (df.drop('B', 1))
    print()
    print (df)
    
def sorting():
    df = pd.DataFrame({'B': [1,2,3,5,4,2,5],
                       'A': [2,1,2,3,3,5,4],
                       'C': [5,3,4,1,1,2,3]})
    #sorts values by column
    df = df.sort_values(by=['C'], ascending=[True])
    #resets the index
    df = df.reset_index(drop=True)
    print (df)
    index = df.index.tolist()
    np.random.shuffle(index)
    #shuffles the indecies for random selection
    df = df.ix[index]
    #resets the index, comment out to keep original
    #df = df.reset_index(drop=True)
    print()
    print (df)
    
#Arbitrary level aggregation
def anyLev():
    #Creates a grouped dataFrame displaying sum, mean, and variance by Map
    df = pd.DataFrame({'Map': [0,0,0,1,1,2,2],'Values': [1,2,3,5,4,2,5]})
    df['Sum'] = df.groupby('Map')['Values'].transform(np.sum)
    df['Mean'] = df.groupby('Map')['Values'].transform(np.mean)
    df['Variance'] = df.groupby('Map')['Values'].transform(np.var)
    print (df)
          
def main():
    #pandasStuff()
    #dataMap()
    #catVar()
    #renLev()
    #combineLev()
    #dateStuff()
    #missingData()
    #slice()
    #transforming()
    #sorting()
    anyLev()

if __name__ == "__main__": main()