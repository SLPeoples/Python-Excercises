
import numpy as np
from scipy.stats.stats import pearsonr
np.random.seed(101)
normal = np.random.normal(loc=0.0, scale= 1.0, size=1000)
print 'Mean: %0.3f Median: %0.3f Variance: %0.3f' % (np.mean(normal), np.median(normal), np.var(normal))

outlying = normal.copy()
outlying[0] = 50.0
print 'Mean: %0.3f Median: %0.3f Variance: %0.3f' % (np.mean(outlying), np.median(outlying), np.var(outlying))
print 'Pearson''s correlation coefficient: %0.3f p-value: %0.3f' % pearsonr(normal,outlying)

from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

X,y = diabetes.data, diabetes.target

import pandas as pd
pd.options.display.float_format = '{:.2f}'.format
df = pd.DataFrame(X)
print df.describe()

box_plots = df.boxplot()

from sklearn.preprocessing import StandardScaler
Xs = StandardScaler().fit_transform(X)
o_idx = np.where(np.abs(Xs)>3)
# .any(1) method will avoid duplicating 
print df[(np.abs(Xs)>3).any(1)] 

from scipy.stats.mstats import winsorize
Xs_w = winsorize(Xs, limits=(0.05, 0.95))

Xs_c = Xs.copy()
Xs_c[o_idx] = np.sign(Xs_c[o_idx]) * 3

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from pandas.tools.plotting import scatter_matrix
dim_reduction = PCA()
Xc = dim_reduction.fit_transform(scale(X))

print 'variance explained by the first 2 components: %0.1f%%' % (sum(dim_reduction.explained_variance_ratio_[:2]*100))
print 'variance explained by the last 2 components: %0.1f%%' % (sum(dim_reduction.explained_variance_ratio_[-2:]*100))

df = pd.DataFrame(Xc, columns=['comp_'+str(j) for j in range(10)])
first_two = df.plot(kind='scatter', x='comp_0', y='comp_1', c='DarkGray', s=50)
last_two  = df.plot(kind='scatter', x='comp_8', y='comp_9', c='DarkGray', s=50)

print 'variance explained by the first 3 components: %0.1f%%' % (sum(dim_reduction.explained_variance_ratio_[:3]*100))
scatter_first = scatter_matrix(pd.DataFrame(Xc[:,:3], columns=['comp1','comp2','comp3']), 
                         alpha=0.3, figsize=(15, 15), diagonal='kde',  marker='o', grid=True)

scatter_last = scatter_matrix(pd.DataFrame(Xc[:,-2:], columns=['comp9','comp10']), 
                         alpha=0.3, figsize=(15, 15), diagonal='kde',  marker='o', grid=True)

outlying = (Xc[:,-1] < -0.3) | (Xc[:,-2] < -1.0)
print df[outlying] 

from sklearn.cluster import DBSCAN
DB = DBSCAN(eps=2.5, min_samples=25, random_state=101)
DB.fit(Xc)

from collections import Counter
print Counter(DB.labels_)

print df[DB.labels_==-1] 

from sklearn import svm
outliers_fraction = 0.01 # 
nu_estimate = 0.95 * outliers_fraction + 0.05

auto_detection = svm.OneClassSVM(kernel="rbf", gamma=0.01, degree=3, nu=nu_estimate)
auto_detection.fit(Xc)

evaluation = auto_detection.predict(Xc)

print df[evaluation==-1] 

inliers  = Xc[evaluation==+1,:]
outliers = Xc[evaluation==-1,:]

from matplotlib import pyplot as plt
import pylab as pl

inlying  = plt.plot(inliers[:,0],inliers[:,1], 'o', markersize=2, color='g', alpha=1.0, label='inliers')
outlying = plt.plot(outliers[:,0],outliers[:,1], 'o', markersize=5, color='k', alpha=1.0, label='outliers')
plt.scatter(outliers[:,0],
           outliers[:,1],
           s=100, edgecolors="k", facecolors="none")
plt.xlabel('Component 1 ('+str(round(dim_reduction.explained_variance_ratio_[0],3))+')')
plt.ylabel('Component 2'+'('+str(round(dim_reduction.explained_variance_ratio_[1],3))+')')
plt.xlim([-7,7])
plt.ylim([-6,6])
plt.legend((inlying[0],outlying[0]),('inliers','outliers'),numpoints=1,loc='best')
plt.title("")
plt.show()
