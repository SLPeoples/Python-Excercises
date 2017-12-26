
from sklearn.datasets import load_boston
from sklearn.preprocessing import scale
boston = load_boston()
X, y = scale(boston.data), boston.target
print X.shape, y.shape

from sklearn.linear_model import LinearRegression
regression = LinearRegression(normalize=True)
regression.fit(X,y)

print regression.score(X,y)

print [a+':'+str(round(b,1)) for a, b in zip(boston.feature_names, regression.coef_,)]

print boston.DESCR

from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data[:-1,:], iris.target[:-1]

from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression()
logistic.fit(X,y)
print 'Predicted class %s, real class %s' % (logistic.predict(iris.data[-1,:]),iris.target[-1])
print 'Probabilities for each class from 0 to 2: %s' % logistic.predict_proba(iris.data[-1,:])

from sklearn.datasets import load_digits
digits = load_digits()
X, y = digits.data[:1700,:], digits.target[:1700]
tX, ty = digits.data[1700:,:], digits.target[1700:]

from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier
OVR = OneVsRestClassifier(logistic).fit(X,y)
OVO = OneVsOneClassifier(logistic).fit(X,y)
print 'One vs rest accuracy: %.3f' % OVR.score(tX,ty)
print 'One vs one accuracy: %.3f' % OVO.score(tX,ty)

LR = LogisticRegression()
LR.fit(X,y)
print 'One vs rest accuracy: %.3f' % LR.score(tX,ty)

from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))
newsgroups_test = fetch_20newsgroups(subset='test', remove=('headers', 'footers', 'quotes'))

print 'number of posts in training: %i' % len(newsgroups_train.data)
D={word:True for post in newsgroups_train.data for word in post.split(' ')}
print 'number of distinct words in training: %i' % len(D)
print 'number of posts in test: %i' % len(newsgroups_test.data)

from sklearn.naive_bayes import BernoulliNB, MultinomialNB
Bernoulli = BernoulliNB(alpha=0.01)
Multinomial = MultinomialNB(alpha=0.01)

from sklearn.feature_extraction.text import HashingVectorizer, TfidfVectorizer
multinomial_hashing_trick = HashingVectorizer(stop_words='english', binary=False, norm=None, non_negative=True)
binary_hashing_trick = HashingVectorizer(stop_words='english', binary=True, norm=None, non_negative=True)

Multinomial.fit(multinomial_hashing_trick.transform(newsgroups_train.data),newsgroups_train.target)
Bernoulli.fit(binary_hashing_trick.transform(newsgroups_train.data),newsgroups_train.target)
from sklearn.metrics import accuracy_score
for m,h in [(Bernoulli,binary_hashing_trick), (Multinomial,multinomial_hashing_trick)]:
    print 'Accuracy for %s: %.3f' % (m, accuracy_score(y_true=newsgroups_test.target, y_pred=m.predict(h.transform(newsgroups_test.data))))

from sklearn.datasets import load_boston
boston = load_boston()

from sklearn.naive_bayes import GaussianNB
Gaussian = GaussianNB()
y_ord = pd.cut(boston.target, bins=4, labels=False)
Gaussian.fit(boston.data,y_ord)
print np.corrcoef(Gaussian.predict(boston.data),boston.target)[0,1]

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
digits = load_digits()
pca = PCA(n_components=25)
pca.fit(digits.data[:1700,:])
X, y = pca.transform(digits.data[:1700,:]), digits.target[:1700]
tX, ty = pca.transform(digits.data[1700:,:]), digits.target[1700:]

from sklearn.neighbors import KNeighborsClassifier
kNN = KNeighborsClassifier(n_neighbors=5, p=2)
kNN.fit(X,y)

print 'Accuracy: %.3f' % kNN.score(tX,ty) 
print 'Prediction: %s actual: %s' % (kNN.predict(tX[:10,:]),ty[:10])

for k in [1,5,10,20,50,100,200]:
    kNN = KNeighborsClassifier(n_neighbors=k).fit(X,y)
    print 'for k=%3i accuracy is %.3f' % (k, kNN.score(tX,ty))
