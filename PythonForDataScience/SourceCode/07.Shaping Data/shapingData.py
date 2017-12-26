#Samuel L. Peoples
from lxml import objectify
import pandas as pd
from distutils import util
import sklearn.feature_extraction.text as ext
#Downloads a dataset!
from sklearn.datasets import fetch_20newsgroups
import networkx as nx
import matplotlib.pyplot as plt

#import nltk
#if you get an nltk error, just download it!
#nltk.download()
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import re

#XML and HTML Parsing
def xmlHTML():
    xml = objectify.parse(open('books.xml'))
    root = xml.getroot()
    df = pd.DataFrame(columns=('author', 'title','genre','price','publish_date'))
    for i in range(0,6):
        obj = root.getchildren()[i].getchildren()
        row = dict(zip(['author', 'title','genre','price','publish_date'],
                       [obj[0].pyval,obj[1].pyval,obj[2].pyval,float(obj[3].pyval),obj[4].pyval]))
        rows = pd.Series(row)
        rows.name = obj[1].text
        df = df.append(rows)

    #prints the first entry
    print(df.ix[0])
    print(type(df.ix[0]))
    print()
    #prints the first entry's first row and type
    print((df.ix[0][0]))
    print(type(df.ix[0][0]))
    #second row
    print((df.ix[0][1]))
    print(type(df.ix[0][1]))
    #shows that the float type was entered correctly
    print((df.ix[0][3]))
    print(type(df.ix[0][3]))

#stemming and stopping
def stemStop():
    
    stemmer = PorterStemmer()
    def stem_tokens(tokens, stemmer):
        stemmed = []
        for item in tokens:
            stemmed.append(stemmer.stem(item))
            return stemmed
    def tokenize(text):
        tokens = word_tokenize(text)
        stems = stem_tokens(tokens, stemmer)
        return stems
    vocab = ['Sam loves swimming so he swims all the time']
    vect = ext.CountVectorizer()
    vec = vect.fit(vocab)
    sentence1 = vec.transform(['George loves swimming too!'])
    #prints the vocabulary list
    print (vec.get_feature_names())
    #prints the elements of 'George loves swimming too!' which appear in the list
    #(0,2) is loves, and (0,5) is swimming, so it reports out
    print (sentence1)
    #Prints an array of elements which appear in list
    #Since it is alphabetic, 'all'=0, 'he'=0,'loves'=1, 'sam'=0,'so'=0,'swimming'=1,
    #'swims'=0,'the=0,'time=0' so the array is [[0,0,1,0,0,1,0,0,0]]
    print (sentence1.toarray())
    print('end of sentence 1')
    #Displays 2 instances of so, 1 instance of swims, 1 instance of time, even with the exclamation.
    sentence2 = vec.transform(['Michael so so swims time!'])
    print (sentence2)
    print (sentence2.toarray())

def regExStuff():
    data1 = 'My phone number is: 800-555-1212.'
    data2 = '800-555-1234 is my phone number.'
    data3 = '(888)555-1234 is my phone number.'
    data4 = 'Give me a ringalingding at 888.555.0134'
    data5 = 'Call 888 555 0000 please'
    #pattern is (\d (digits){3}(in triplets))(in parenthesis), -...-(in quads)
    #(?:\S|\s) matches any single whitespace or nonwhitespace character 
    pattern = re.compile(r'(\d{3})(?:\S|\s)(\d{3})(?:\S|\s)(\d{4})')
    #groups items into array
    dmatch1 = pattern.search(data1).groups()
    dmatch2 = pattern.search(data2).groups()
    print (dmatch1)
    print (dmatch2)
    #Demonstrates that it finds many phone number formats
    dmatch3 = pattern.search(data3).groups()
    dmatch4 = pattern.search(data4).groups()
    print (dmatch3)
    print (dmatch4)
    #even whitespace
    dmatch5 = pattern.search(data5).groups()
    print (dmatch5) 
    
def bagOfWords():
    categories = ['comp.graphics', 'misc.forsale','rec.autos', 'sci.space']
    # fetch_20newsgroups() loads the dataset into memory.
    twenty_train = fetch_20newsgroups(subset='train',categories=categories,shuffle=True,random_state=42)
    count_vect = ext.CountVectorizer()
    X_train_counts = count_vect.fit_transform(twenty_train.data)
    #This is the size of our bag of words
    print (X_train_counts.shape)
    
    #now lets look at the science and space categories
    categories = ['sci.space']
    #we use the subest provided by the book
    twenty_train = fetch_20newsgroups(subset='train',categories=categories,
                                      remove=('headers', 'footers', 'quotes'),shuffle=True,random_state=42)
    #We tokenize with analyzer which  determines how the application creates the ngrams
    count_chars = ext.CountVectorizer(analyzer='char_wb',ngram_range=(3,3),max_features=10).fit(twenty_train['data'])
    count_words = ext.CountVectorizer(analyzer='word',ngram_range=(2,2),max_features=10,
                                      stop_words='english').fit(twenty_train['data'])
    X = count_chars.transform(twenty_train.data)
    # top ten trigrams for characters from the document
    print (count_chars.get_feature_names())
    #The second is the n-gram for the first document.It shows the frequency of the top ten trigrams.
    print (X[1].todense())
    # top ten trigrams for words
    print (count_words.get_feature_names())
     
    # Term Frequency times Inverse Document Frequency (TF-IDF) transformation
    #TF-IDF helps you to locate the most important word or n-grams and exclude
    #the least important ones. It is also very helpful as an input for linear models,
    #because they work better with TF-IDF scores than word counts.
    tfidf = ext.TfidfTransformer().fit(X_train_counts)
    X_train_tfidf = tfidf.transform(X_train_counts)
    print (X_train_tfidf.shape)            

#Graphing and networkX
def graphing():
    # creates a graph using the cycle_graph() template. The graph contains ten nodes.
    G = nx.cycle_graph(10)
    #Calling adjacency_matrix() creates the adjacency matrix from the graph. 
    A = nx.adjacency_matrix(G)
    print(A.todense())
    #let's draw that 10-node graph
    nx.draw_networkx(G)
    plt.show()
    #now let's add an edge between nodes 1 and 5!
    G.add_edge(1,5)
    nx.draw_networkx(G)
    plt.show()
    #notice the dense matrix shows a new value of 1 at [1,5] and [5,1]
    print()
    A = nx.adjacency_matrix(G)
    print(A.todense())
    
    
def main():
    #xmlHTML()
    #stemStop()
    #regExStuff()
    #bagOfWords()
    graphing()
    
if __name__ == "__main__": main()