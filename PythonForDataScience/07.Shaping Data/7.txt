
from lxml import objectify
import pandas as pd
from distutils import util

xml = objectify.parse(open('XMLData.xml'))
root = xml.getroot()
df = pd.DataFrame(columns=('Number', 'Boolean'))

for i in range(0,4):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(['Number', 'Boolean'], 
                   [obj[0].pyval, 
                    bool(util.strtobool(obj[2].text))]))
    row_s = pd.Series(row)
    row_s.name = obj[1].text
    df = df.append(row_s)
    
print type(df.ix['First']['Number'])
print type(df.ix['First']['Boolean'])

from lxml import objectify
import pandas as pd
from distutils import util

xml = objectify.parse(open('XMLData.xml'))
root = xml.getroot()

data = zip(map(int, root.xpath('Record/Number')), 
           map(bool, map(util.strtobool, 
                map(str, root.xpath('Record/Boolean')))))

df = pd.DataFrame(data, 
                  columns=('Number', 'Boolean'), 
                  index=map(str, 
                        root.xpath('Record/String')))

print df
print type(df.ix['First']['Number'])
print type(df.ix['First']['Boolean'])

import sklearn.feature_extraction.text as ext
from nltk import word_tokenize          
from nltk.stem.porter import PorterStemmer

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
vect = ext.CountVectorizer(tokenizer=tokenize, 
                           stop_words='english')
vec = vect.fit(vocab)

sentence1 = vec.transform(['George loves swimming too!'])

print vec.get_feature_names()
print sentence1.toarray()

import re

data1 = 'My phone number is: 800-555-1212.'
data2 = '800-555-1234 is my phone number.'

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

dmatch1 = pattern.search(data1).groups()
dmatch2 = pattern.search(data2).groups()

print dmatch1
print dmatch2

from sklearn.datasets import fetch_20newsgroups
import sklearn.feature_extraction.text as ext

categories = ['comp.graphics', 'misc.forsale', 
              'rec.autos', 'sci.space']
twenty_train = fetch_20newsgroups(subset='train',
                                  categories=categories, 
                                  shuffle=True, 
                                  random_state=42)

count_vect = ext.CountVectorizer()
X_train_counts = count_vect.fit_transform(
    twenty_train.data)

print X_train_counts.shape

from sklearn.datasets import fetch_20newsgroups
import sklearn.feature_extraction.text as ext

categories = ['sci.space']

twenty_train = fetch_20newsgroups(subset='train', 
        categories=categories, 
        remove=('headers', 'footers', 'quotes'),
        shuffle=True, 
        random_state=42)

count_chars = ext.CountVectorizer(analyzer='char_wb', 
        ngram_range=(3,3), 
        max_features=10).fit(twenty_train['data'])
count_words = ext.CountVectorizer(analyzer='word', 
        ngram_range=(2,2),
        max_features=10,
        stop_words='english').fit(twenty_train['data'])
X = count_chars.transform(twenty_train.data)

print count_words.get_feature_names()
print X[1].todense()
print count_words.get_feature_names()

from sklearn.datasets import fetch_20newsgroups
import sklearn.feature_extraction.text as ext

categories = ['sci.space']

twenty_train = fetch_20newsgroups(subset='train', 
        categories=categories, 
        remove=('headers', 'footers', 'quotes'),                  
        shuffle=True, 
        random_state=42)

count_vect = ext.CountVectorizer()
X_train_counts = count_vect.fit_transform(
    twenty_train.data)

tfidf = ext.TfidfTransformer().fit(X_train_counts)
X_train_tfidf = tfidf.transform(X_train_counts)

print X_train_tfidf.shape

import networkx as nx

G = nx.cycle_graph(10)
A = nx.adjacency_matrix(G)

print(A.todense())

import matplotlib.pyplot as plt
nx.draw_networkx(G)
plt.show()

G.add_edge(1,5)
nx.draw_networkx(G)
plt.show()
