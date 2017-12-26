
# http://scikit-learn.org/stable/modules/tree.html

from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
features = iris.feature_names

from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)

from sklearn import tree
for depth in range(1,10):
    tree_classifier = tree.DecisionTreeClassifier(max_depth=depth, random_state=0)
    if tree_classifier.fit(X,y).tree_.max_depth < depth:
        break
    score = np.mean(cross_val_score(tree_classifier, X, y, scoring='accuracy', cv=crossvalidation, n_jobs=1))
    print 'Depth: %i Accuracy: %.3f' % (depth,score)

# min_samples_leaf=3
# min_samples_split

### GRAPHIC OUTPUT
from sklearn.externals.six import StringIO  
import pydot 
dot_data = StringIO()
tree_classifier = tree.DecisionTreeClassifier(max_depth=4, random_state=0)
tree_classifier.fit(X,y)
tree.export_graphviz(tree_classifier, out_file=dot_data, feature_names=features, max_depth=4) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("Iris.pdf")
graph.write_png("9781118844182 fg2001.png")

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
titanic = pd.io.parsers.read_csv("Titanic.csv")
encoder = OneHotEncoder(sparse=False)
X = titanic[['sex','age','sibsp','parch','pclass']].values
y = titanic['survived'].values == 'survived'
tree_classifier = tree.DecisionTreeClassifier(max_depth=2, min_samples_split=467, min_samples_leaf=10, random_state=0)

df = pd.concat([
pd.get_dummies(titanic['sex']),
titanic[['age']],
], join='outer', axis=1)

tree_classifier.fit(df,y)

### GRAPHIC OUTPUT
from sklearn.externals.six import StringIO  
import pydot 
dot_data = StringIO() 
tree.export_graphviz(tree_classifier, out_file=dot_data, feature_names=df.columns, max_depth=2) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("Titanic.pdf") 
graph.write_png("9781118844182 fg2001.png")

tree_classifier = tree.DecisionTreeClassifier(min_samples_split=30, min_samples_leaf=10, random_state=0)
tree_classifier.fit(X,y)
score = np.mean(cross_val_score(tree_classifier, X, y, scoring='accuracy', cv=crossvalidation, n_jobs=1))
print 'Accuracy: %.3f' % score

### GRAPHIC OUTPUT
from sklearn.externals.six import StringIO  
import pydot 
dot_data = StringIO() 
tree.export_graphviz(tree_classifier, out_file=dot_data, feature_names=features, max_depth=4) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("Iris simpler.pdf") 

from sklearn.datasets import load_boston
boston = load_boston()
X, y = boston.data, boston.target
features = boston.feature_names

from sklearn.tree import DecisionTreeRegressor
regression_tree = tree.DecisionTreeRegressor(min_samples_split=30, min_samples_leaf=10, random_state=0)
regression_tree.fit(X,y)
score = np.mean(cross_val_score(regression_tree, X, y, scoring='mean_squared_error', cv=crossvalidation, n_jobs=1))
print 'Mean squared error: %.3f' % abs(score)

### GRAPHIC OUTPUT
from sklearn.externals.six import StringIO  
import pydot 
dot_data = StringIO() 
tree.export_graphviz(regression_tree, out_file=dot_data, feature_names=features, max_depth=4) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("Boston.pdf") 

from sklearn.ensemble import BaggingClassifier
from sklearn import tree
tree_classifier = tree.DecisionTreeClassifier(random_state=0)
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)
bagging = BaggingClassifier(tree_classifier, max_samples=0.7, max_features=0.7, n_estimators=300)
scores = np.mean(cross_val_score(bagging, X, y, scoring='accuracy', cv=crossvalidation, n_jobs=1))
print 'Accuracy: %.3f' % score

from sklearn.datasets import load_digits
digit = load_digits()
X, y = digit.data, digit.target
print X.shape, y.shape

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)
RF_cls = RandomForestClassifier(n_estimators=300)
score = np.mean(cross_val_score(RF_cls, X, y, scoring='accuracy', cv=crossvalidation, n_jobs=1))
print 'Accuracy: %.3f' % score

from sklearn.learning_curve import validation_curve
train_scores, test_scores = validation_curve(RF_cls, X, y,
                                             'n_estimators', param_range=[10,50,100,200,300,500,800,1000,1500], 
                                             cv=crossvalidation, scoring='accuracy', n_jobs=1)
print 'mean cv accuracy %s' % np.mean(test_scores,axis=1)

import matplotlib.pyplot as plt
mean_test = np.mean(test_scores,axis=1)
#plt.plot([10,50,100,200,300,500,1000],mean_train,'ro--', label='Training')
plt.plot([10,50,100,200,300,500,800,1000,1500],mean_test,'bD-.', label='Cross-validation')
plt.grid()
plt.xlabel('Number of estimators') # adds label to x axis
plt.ylabel('accuracy') # adds label to y axis
plt.legend(loc='lower right', numpoints= 1)
plt.show()

X, y = boston.data, boston.target

from sklearn.ensemble import RandomForestRegressor
RF_rg = RandomForestRegressor (n_estimators=300, random_state=1)
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)
score = np.mean(cross_val_score(RF_rg, X, y, scoring='mean_squared_error', cv=crossvalidation, n_jobs=1))
print 'Mean squared error: %.3f' % abs(score)

from sklearn.ensemble import RandomForestClassifier
X, y = digit.data, digit.target
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)
RF_cls = RandomForestClassifier(n_estimators=300)
scorer = 'accuracy'

RF_cls = RandomForestClassifier(n_estimators=300).fit(X,y)
X = RF_cls.transform(X)
print X.shape
print RF_cls.feature_importances_

from sklearn import grid_search
search_grid =  {'max_features': [Xr.shape[1]/3, 'sqrt', 'log2', 'auto'], 'min_samples_leaf': [1, 2, 10, 30]}
search_func = grid_search.GridSearchCV(estimator=RF_cls, param_grid=search_grid, scoring=scorer, n_jobs=1, cv=crossvalidation)
search_func.fit(Xr,y)

print 'Best parameters: %s' % search_func.best_params_
print 'Best accuracy: %.3f' % search_func.best_score_

X, y = digit.data, digit.target

from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier(n_estimators=1000, learning_rate=0.01, random_state=1)
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)
score = np.mean(cross_val_score(ada, X, y, scoring='accuracy', cv=crossvalidation, n_jobs=1))
print 'Accuracy: %.3f' % score

X, y = digit.data, digit.target
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)

from sklearn.ensemble import GradientBoostingClassifier
GBC = GradientBoostingClassifier(n_estimators=300, subsample=1.0, max_depth=2, learning_rate=0.1, random_state=1)
score = np.mean(cross_val_score(GBC, X, y, scoring='accuracy', cv=crossvalidation, n_jobs=1))
print 'Accuracy: %.3f' % score

X, y = boston.data, boston.target

from sklearn.ensemble import GradientBoostingRegressor
GBR = GradientBoostingRegressor(n_estimators=1000, subsample=1.0, max_depth=3, learning_rate=0.01, random_state=1)
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)
score = np.mean(cross_val_score(GBR, X, y, scoring='mean_squared_error', cv=crossvalidation, n_jobs=1))
print 'Mean squared error: %.3f' % abs(score)

X, y = boston.data, boston.target
crossvalidation = KFold(n=X.shape[0], n_folds=5, shuffle=True, random_state=1)
GBR = GradientBoostingRegressor(n_estimators=1000, subsample=1.0, max_depth=3, learning_rate=0.01, random_state=1)

from sklearn import grid_search
search_grid =  {'subsample': [1.0, 0.9], 'max_depth': [2, 3, 5], 'n_estimators': [500 , 1000, 2000]}
search_func = grid_search.GridSearchCV(estimator=GBR, param_grid=search_grid, scoring='mean_squared_error', n_jobs=1, cv=crossvalidation)
search_func.fit(X,y)

print 'Best parameters: %s' % search_func.best_params_
print 'Best mean squared error: %.3f' % abs(search_func.best_score_)
