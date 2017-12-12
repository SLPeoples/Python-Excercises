
from sklearn import datasets
digits = datasets.load_digits()
X,y = digits.data, digits.target

import matplotlib.pyplot as plt
for k,img in enumerate(range(10)):
    plt.subplot(2, 5, k)
    plt.imshow(digits.images[img],cmap='binary',interpolation='none')
plt.show()

X[0]

import numpy as np
print np.min(X), np.max(X)

print X.shape

from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler
# We keep 30% random examples for test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
# We scale the data in the range [-1,1]
scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X_train)
X_train = scaling.transform(X_train)
X_test  = scaling.transform(X_test)

from sklearn.svm import SVC
# We balance the clasess so you can see how it works
learning_algo = SVC(kernel='linear', class_weight='auto')
cv_performance = cross_val_score(learning_algo, X_train, y_train, cv=10)
test_performance = learning_algo.fit(X_train, y_train).score(X_test, y_test)
print 'Cross-validation accuracy score: %0.3f, test accuracy score: %0.3f' % (np.mean(cv_performance),test_performance)

from sklearn.grid_search import GridSearchCV
learning_algo = SVC(class_weight='auto', random_state=101)
search_space = {'C': np.logspace(-3, 3, 7)}
gridsearch = GridSearchCV(learning_algo, param_grid=search_space, scoring='accuracy', refit=True, cv=10, n_jobs=-1)
gridsearch.fit(X_train,y_train)
cv_performance = gridsearch.best_score_
test_performance = gridsearch.score(X_test, y_test)
print 'Cross-validation accuracy score: %0.3f, test accuracy score: %0.3f' % (cv_performance,test_performance)
print 'Best C parameter: %0.1f' % gridsearch.best_params_['C']

from sklearn.grid_search import GridSearchCV
learning_algo = SVC(class_weight='auto', random_state=101)
search_space = [{'kernel': ['linear'], 'C': np.logspace(-3, 3, 7)},
                {'kernel': ['rbf'], 'degree':[2,3,4], 'C':np.logspace(-3, 3, 7), 'gamma': np.logspace(-3, 2, 6)}]
gridsearch = GridSearchCV(learning_algo, param_grid=search_space, scoring='accuracy', refit=True, cv=10, n_jobs=-1)
gridsearch.fit(X_train,y_train)
cv_performance = gridsearch.best_score_
test_performance = gridsearch.score(X_test, y_test)
print 'Cross-validation accuracy score: %0.3f, test accuracy score: %0.3f' % (cv_performance,test_performance)
print 'Best parametes: %s' % gridsearch.best_params_

print 'Best parametes: %s' % gridsearch.best_params_
# if you want to explore more, try: print gridsearch.grid_scores_

from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.grid_search import GridSearchCV

from sklearn import datasets
boston = datasets.load_boston()
X,y = boston.data, boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X_train)
X_train = scaling.transform(X_train)
X_test  = scaling.transform(X_test)

from sklearn.svm import SVR
learning_algo = SVR(random_state=101)
search_space = [{'kernel': ['linear'], 'C': np.logspace(-3, 2, 6), 'epsilon': [0, 0.01, 0.1, 0.5, 1, 2, 4]},
                {'kernel': ['rbf'], 'degree':[2,3], 'C':np.logspace(-3, 3, 7), 'gamma': np.logspace(-3, 2, 6), 'epsilon': [0, 0.01, 0.1, 0.5, 1, 2, 4]}]
gridsearch = GridSearchCV(learning_algo, param_grid=search_space, refit=True, scoring= 'r2', cv=10, n_jobs=-1)
gridsearch.fit(X_train,y_train)
cv_performance = gridsearch.best_score_
test_performance = gridsearch.score(X_test, y_test)
print 'Cross-validation accuracy score: %0.3f, test accuracy score: %0.3f' % (cv_performance,test_performance)
print 'Best parametes: %s' % gridsearch.best_params_

from sklearn.datasets import make_classification
import numpy as np
X,y = make_classification(n_samples=10**4, n_features=15, n_informative=10, random_state=101)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.svm import SVC, LinearSVC
slow_SVM = SVC(kernel="linear", random_state=101)
fast_SVM = LinearSVC(random_state=101, loss='l1')

slow_SVM.fit(X_train, y_train)
fast_SVM.fit(X_train, y_train)
print 'SVC test accuracy score: %0.3f' % slow_SVM.score(X_test, y_test)
print 'LinearSVC test accuracy score: %0.3f' % fast_SVM.score(X_test, y_test)

import timeit
X,y = make_classification(n_samples=10**4, n_features=15, n_informative=10, random_state=101)
print 'avg secs for SVC, best of 3: %0.1f' % np.mean(timeit.timeit("slow_SVM.fit(X, y)", "from __main__ import slow_SVM, X, y", number=1))
print 'avg secs for LinearSVC, best of 3: %0.1f' % np.mean(timeit.timeit("fast_SVM.fit(X, y)", "from __main__ import fast_SVM, X, y", number=1))

import timeit
X,y = make_classification(n_samples=10**5, n_features=15, n_informative=10, random_state=101)
print 'avg secs for SVC, best of 3: %0.1f' % np.mean(timeit.timeit("slow_SVM.fit(X, y)", "from __main__ import slow_SVM, X, y", number=1))
print 'avg secs for LinearSVC, best of 3: %0.1f' % np.mean(timeit.timeit("fast_SVM.fit(X, y)", "from __main__ import fast_SVM, X, y", number=1))

# http://www.quora.com/What-is-an-appropriate-grid-search-range-for-optimizing-the-parameter-epsilon-in-epsilon-support-vector-regression
# http://www.svms.org/parameters/
# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html

from sklearn.datasets import make_classification
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.svm import LinearSVC
import timeit

from sklearn.linear_model import SGDClassifier
X,y = make_classification(n_samples=10**6, n_features=15, n_informative=10, random_state=101)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
fast_SVM = LinearSVC(random_state=101, penalty='l2', loss='l1', dual=True)
fast_SVM.fit(X_train, y_train)
print 'LinearSVC test accuracy score: %0.3f' % fast_SVM.score(X_test, y_test)
print 'avg secs for LinearSVC, best of 3: %0.1f' % np.mean(timeit.timeit("fast_SVM.fit(X_train, y_train)", "from __main__ import fast_SVM, X_train, y_train", number=1))

stochastic_SVM = SGDClassifier(loss='hinge', n_iter=5, shuffle=True, random_state=101)
stochastic_SVM.fit(X_train, y_train)
print 'SGDClassifier test accuracy score: %0.3f' % stochastic_SVM.score(X_test, y_test)
print 'avg secs for SGDClassifier, best of 3: %0.1f' % np.mean(timeit.timeit("stochastic_SVM.fit(X_train, y_train)", "from __main__ import stochastic_SVM, X_train, y_train", number=1))
