
import numpy as np
A = np.array([[1, 3, 4], [2, 3, 5], [1, 2, 3], [5, 4, 6]])
print(A)

U, s, Vh = np.linalg.svd(A, full_matrices=False)
print np.shape(U), np.shape(s),np.shape(Vh)
print s

print np.dot(np.dot(U, np.diag(s)), Vh) # Full matrix reconstruction

print np.round(np.dot(np.dot(U[:,:2], np.diag(s[:2])), Vh[:2,:]),1) # k=2 reconstruction

print np.round(np.dot(np.dot(U[:,:1], np.diag(s[:1])), Vh[:1,:]),1) # k=1 reconstruction

from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
X = sparse_random_matrix(100, 100, density=0.01, random_state=42)
svd = TruncatedSVD(n_components=5, random_state=42)
svd.fit(X) 
print(svd.explained_variance_ratio_) 
print(svd.explained_variance_ratio_.sum())
shape(svd.components_)

from sklearn.datasets import load_iris
from sklearn.decomposition import FactorAnalysis
iris = load_iris()
X = iris.data
Y = iris.target
factor = FactorAnalysis(n_components=4).fit(X)

import pandas as pd
print pd.DataFrame(factor.components_,columns=iris.feature_names)

from sklearn.decomposition import PCA
import pandas as pd
pca = PCA().fit(X)
print 'Explained variance by each component: %s' % pca.explained_variance_ratio_
print pd.DataFrame(pca.components_,columns=iris.feature_names)

from sklearn.datasets import fetch_olivetti_faces
dataset = fetch_olivetti_faces(shuffle=True, random_state=101)
train_faces = dataset.data[:350,:]
test_faces  = dataset.data[350:,:]
train_answers = dataset.target[:350]
test_answers = dataset.target[350:]

print dataset.DESCR

from sklearn.decomposition import RandomizedPCA
n_components = 25
Rpca = RandomizedPCA(n_components=n_components, whiten=True).fit(train_faces)
print 'Explained variance by %i components: %0.3f' % (n_components, np.sum(Rpca.explained_variance_ratio_))
compressed_train_faces = Rpca.transform(train_faces)
compressed_test_faces  = Rpca.transform(test_faces)

import matplotlib.pyplot as plt
photo = 17
print 'We are looking for face id=%i' % test_answers[photo]
plt.subplot(1, 2, 1)
plt.axis('off')
plt.title('Unknown face '+str(photo)+' in test set')
plt.imshow(test_faces[photo].reshape(64,64), cmap=plt.cm.gray, interpolation='nearest')

mask = compressed_test_faces[photo,] #Just the vector of value components of our photo
squared_errors = np.sum((compressed_train_faces - mask)**2,axis=1)
minimum_error_face = argmin(squared_errors)
most_resembling = list(np.where(squared_errors < 20)[0])
print 'Best resembling face in train test: %i' % train_answers[minimum_error_face]

import matplotlib.pyplot as plt
plt.subplot(2, 2, 1)
plt.axis('off')
plt.title('Unknown face '+str(photo)+' in test set')
plt.imshow(test_faces[photo].reshape(64,64), cmap=plt.cm.gray, interpolation='nearest')
for k,m in enumerate(most_resembling[:3]):
    plt.subplot(2, 2, 2+k)
    plt.title('Match in train set no. '+str(m))
    plt.axis('off')
    plt.imshow(train_faces[m].reshape(64,64), cmap=plt.cm.gray, interpolation='nearest')
plt.show()

import os
print os.getcwd()

from sklearn.datasets import fetch_20newsgroups
dataset = fetch_20newsgroups(shuffle=True, categories = ['misc.forsale'], remove=('headers', 'footers', 'quotes'), random_state=101)
print 'Posts: %i' % len(dataset.data)

print dataset.target_names

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
tfidf = vectorizer.fit_transform(dataset.data)

from sklearn.decomposition import NMF
n_topics = 5
nmf = NMF(n_components=n_topics, random_state=101).fit(tfidf)

feature_names = vectorizer.get_feature_names()
n_top_words = 15
for topic_idx, topic in enumerate(nmf.components_):
    print "Topic #%d:" % (topic_idx+1),
    print " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])

nmf = NMF(n_components=n_topics+100, random_state=101).fit(tfidf)
nmf.reconstruction_err_

import pandas as pd
from scipy.sparse import csr_matrix
users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=['user_id', 'gender', 'age', 'occupation', 'zip'])
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=['user_id', 'movie_id', 'rating', 'timestamp'])
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=['movie_id', 'title', 'genres'])
MovieLens = pd.merge(pd.merge(ratings, users), movies)

ratings_mtx_df = MovieLens.pivot_table(values='rating', rows='user_id', cols='title', fill_value=0)
movie_index = ratings_mtx_df.columns

from sklearn.decomposition import TruncatedSVD
recom = TruncatedSVD(n_components=10, random_state=101)
R = recom.fit_transform(ratings_mtx_df.values.T)

# 1196::Star Wars: Episode V - The Empire Strikes Back (1980)::Action|Adventure|Drama|Sci-Fi|War
star_wars_idx = list(movie_index).index('Star Wars: Episode V - The Empire Strikes Back (1980)')
print R[star_wars_idx]

import numpy as np
correlation_matrix = np.corrcoef(R)
P = correlation_matrix[star_wars_idx]
print list(movie_index[(P > 0.98) & (P < 1.0)])

star_wars_idx
