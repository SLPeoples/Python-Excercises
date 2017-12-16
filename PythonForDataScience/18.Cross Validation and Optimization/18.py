
from sklearn.datasets import load_boston
boston = load_boston()
X, y = boston.data, boston.target
print X.shape, y.shape

print boston.DESCR

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
regression = LinearRegression()
regression.fit(X,y)
print 'Mean squared error: %.2f' % mean_squared_error(y_true=y, y_pred=regression.predict(X))

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)
print X_train.shape, X_test.shape

regression.fit(X_train,y_train)
print 'Train mean squared error: %.2f' % mean_squared_error(y_true=y_train, y_pred=regression.predict(X_train))

print 'Test mean squared error: %.2f' % mean_squared_error(y_true=y_test, y_pred=regression.predict(X_test))

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=6)
regression.fit(X_train,y_train)
print 'Train mean squared error: %.2f' % mean_squared_error(y_true=y_train, y_pred=regression.predict(X_train))
print 'Test mean squared error: %.2f' % mean_squared_error(y_true=y_test, y_pred=regression.predict(X_test))

from sklearn.cross_validation import cross_val_score

# sklearn.cross_validation.cross_val_score(estimator, X, y=None, scoring=None, cv=None, 
# n_jobs=1, verbose=0, fit_params=None, score_func=None, pre_dispatch='2*n_jobs')

crossvalidation = KFold(n=X.shape[0], n_folds=10, shuffle=True, random_state=1)
scores = cross_val_score(regression, X, y, scoring='mean_squared_error', cv=crossvalidation, n_jobs=1)
print 'Folds: %i, mean squared error: %.2f std: %.2f' % (len(scores),np.mean(np.abs(scores)),np.std(scores))

def cross_validation_loop(cross_validation_iterator):
    cv_mse = list()
    for nfold, (train_idx, test_idx) in enumerate(cross_validation_iterator):
            regression.fit(X[train_idx,:],y[train_idx])
            cv_mse.append(mean_squared_error(y_true=y[test_idx], y_pred=regression.predict(X[test_idx,:])))
    return nfold+1, np.abs(np.mean(cv_mse)), np.std(cv_mse)

from sklearn.cross_validation import KFold
crossvalidation = KFold(n=X.shape[0], n_folds=10, shuffle=True, random_state=1)
print '%i folds cross validation mean squared error: %.2f std: %.2f' % (cross_validation_loop(crossvalidation))

# cross_val_score -> automatic startification based on y classes

# sklearn.cross_validation.StratifiedKFold(y, n_folds=3, indices=None, shuffle=False, random_state=None)

import pandas as pd
df = pd.DataFrame(X, columns=boston.feature_names)
df['target'] = y
boxplot = df.boxplot('target', by='CHAS', return_type='axes')

from sklearn.cross_validation import StratifiedKFold
stratification = StratifiedKFold(y=X[:,3], n_folds=10, shuffle=True, random_state=1)
scores = cross_val_score(regression, X, y, scoring='mean_squared_error', cv=stratification, n_jobs=1)
print 'Stratified %i folds cross validation mean squared error: %.2f std: %.2f' % (len(scores),np.mean(np.abs(scores)),np.std(scores))

scores = cross_val_score(regression, X, y, scoring='mean_squared_error', cv=X.shape[0], n_jobs=1)
print 'Folds: %i, mean squared error: %.2f std: %.2f' % (len(scores),np.mean(np.abs(scores)),np.std(scores))

from sklearn.cross_validation import LeaveOneOut
LOO = LeaveOneOut(n=X.shape[0])
print 'Stratified %i folds cross validation mean squared error: %.2f std: %.2f' % (cross_validation_loop(LOO))        

from sklearn.cross_validation import ShuffleSplit
subsampling = ShuffleSplit(n=X.shape[0], n_iter=100, test_size=0.3, random_state=0)
print 'Subsampling %i fold cross validation mean squared error: %.2f std: %.2f' % (cross_validation_loop(subsampling))        

from sklearn.cross_validation import Bootstrap
boot = Bootstrap(n=X.shape[0], n_iter=300, test_size=0.2, random_state=0)
print 'Subsampling %i fold cross validation mean squared error: %.2f std: %.2f' % (cross_validation_loop(boot))    

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression # chi2, f_classif
Selector_f = SelectPercentile(f_regression, percentile=25)
Selector_f.fit(X,y)

for n,s in zip(boston.feature_names,Selector_f.scores_):
    print 'F-score: %3.2f\t for feature %s ' % (s,n)

from sklearn.feature_selection import RFECV
selector = RFECV(estimator=regression, cv=10, scoring='mean_squared_error')
selector.fit(X, y)
print("Optimal number of features : %d" % selector.n_features_)

print boston.feature_names[selector.support_]

from sklearn.ensemble import RandomForestRegressor
ensemble = RandomForestRegressor(n_estimators=100, oob_score=True)
ensemble.fit(X, y)
print 'Out of the bag score: %.3f' % ensemble.oob_score_
X_s = ensemble.transform(X)

import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
print X.shape, y.shape

from sklearn.neighbors import KNeighborsClassifier
# n_neighbors = 1 to 5
# weights  = uniform / distance
# p = 1 (manhattan distance), 2 (euclidean distance)

classifier = KNeighborsClassifier(n_neighbors=5, weights='uniform', metric= 'minkowski', p=2)
grid = {'n_neighbors': range(1,11), 'weights': ['uniform', 'distance'], 'p': [1,2]}
print 'Number of tested models: %i' % np.prod([len(grid[element]) for element in grid])
score_metric = 'accuracy'

from sklearn.cross_validation import cross_val_score
print 'Baseline with default parameters: %.3f' % np.mean(cross_val_score(classifier, X, y, cv=10, scoring=score_metric, n_jobs=1))

from sklearn.grid_search import GridSearchCV
search = GridSearchCV(estimator=classifier, param_grid=grid, 
                                       scoring=score_metric, n_jobs=1, refit=True, cv=10)
search.fit(X,y)

print 'Best parameters: %s' % search.best_params_
print 'CV Accuracy of best parameters: %.3f' % search.best_score_

search.grid_scores_

from sklearn.learning_curve import validation_curve
train_scores, test_scores = validation_curve(KNeighborsClassifier(weights='uniform', metric= 'minkowski', p=1), X, y, 
                                             'n_neighbors', param_range=range(1,11), cv=10, scoring='accuracy', n_jobs=1)

mean_train  = np.mean(train_scores,axis=1)
mean_test   = np.mean(test_scores,axis=1)

import matplotlib.pyplot as plt
plt.plot(range(1,11),mean_train,'ro--', label='Training')
plt.plot(range(1,11),mean_test,'bD-.', label='Cross-validation')
plt.grid()
plt.xlabel('Number of neighbors') # adds label to x axis
plt.ylabel('accuracy') # adds label to y axis
plt.legend(loc='upper right', numpoints= 1)
plt.show()

from sklearn.grid_search import RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=classifier, param_distributions=grid, n_iter=10, 
                                   scoring=score_metric, n_jobs=1, refit=True, cv=10, )
random_search.fit(X,y)

print 'Best parameters: %s' % random_search.best_params_
print 'CV Accuracy of best parameters: %.3f' % random_search.best_score_

from sklearn.datasets import load_boston
boston = load_boston()
X, y = boston.data, boston.target

from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression

grid = {'vselection__percentile':[25,50,75,100], 
        'model__n_neighbors': range(1,11), 'model__weights': ['uniform', 'distance'], 'model__p': [1,2]}
score_metric = 'mean_squared_error'

selector = SelectPercentile(f_regression)
regression = KNeighborsRegressor()
procedure = Pipeline(steps=[('vselection',selector),('model',regression)])
search = GridSearchCV(estimator=procedure, param_grid=grid, scoring=score_metric, n_jobs=1, refit=True, cv=10)
search.fit(X,y)

print 'Best parameters: %s' % search.best_params_
print 'CV Accuracy of best parameters: %.2f' % abs(search.best_score_)
