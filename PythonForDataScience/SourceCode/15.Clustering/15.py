
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.data
ground_truth = digits.target

#print digits.DESCR

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
pca = PCA(n_components=40)
Cx = pca.fit_transform(scale(X))
print 'Explained variance %0.3f' % sum(pca.explained_variance_ratio_)

from sklearn.cluster import KMeans
clustering = KMeans(n_clusters=10, n_init=10, random_state=1)
clustering.fit(Cx)

import numpy as np
import pandas as pd
ms = np.column_stack((ground_truth,clustering.labels_))
df = pd.DataFrame(ms, columns = ['Ground truth','Clusters'])
pd.crosstab(df['Ground truth'], df['Clusters'], margins=True)

# How good is the results?
from sklearn import metrics
metrics.adjusted_rand_score(ground_truth,clustering.labels_)

dist = clustering.fit_transform(Cx)
print np.min(dist,axis=0)
print np.argmin(dist,axis=0)

import matplotlib.pyplot as plt
for k,img in enumerate(np.argmin(dist,axis=0)):
    cluster = clustering.labels_[img]
    plt.subplot(2, 5, cluster)
    plt.imshow(digits.images[img],cmap='binary',interpolation='none')
    plt.title('cl '+str(cluster))
plt.show()

inertia = list()
delta_inertia = list()
for k in range(1,21):
    clustering = KMeans(n_clusters=k, n_init=10, random_state=1)
    clustering.fit(Cx)
    if inertia:
        delta_inertia.append(inertia[-1] - clustering.inertia_)
    inertia.append(clustering.inertia_)

len([k for k in range(1,21)])

import matplotlib.pyplot as plt
plt.figure()
plt.plot([k for k in range(2,21)], delta_inertia, 'ko-')
plt.xlabel('Number of clusters')
plt.ylabel('Rate of change of inertia')
plt.show()

from sklearn.cluster import MiniBatchKMeans
batch_clustering = MiniBatchKMeans(n_clusters=10, random_state=1)

batch = 100
guessed_labels = list()
inertia = 0
for row in range(0,len(Cx),batch):
    if row+batch < len(Cx):
        feed = Cx[row:row+batch,:]
    else:
        feed = Cx[row:,:]
    batch_clustering.partial_fit(feed)
    # We have to stack results in a list, because MiniBatchKMean
    # does not take track of all the batches
    guessed_labels.append(batch_clustering.labels_)
    inertia += batch_clustering.inertia_

# NumPy hstack turns a list of arrays into an array
# by inspecting the variable guess_labels you can know 
# the assigned cluster
guessed_labels = np.hstack(guessed_labels)

print "Kmeans inertia: %0.1f\nMiniBatchKmeans inertia: %0.1f" % (clustering.inertia_,inertia)


# How good is the results?
from sklearn import metrics
metrics.adjusted_rand_score(ground_truth,guessed_labels)

from sklearn.cluster import AgglomerativeClustering
# Affinity = {“euclidean”, “l1”, “l2”, “manhattan”, “cosine”}
# Linkage = {“ward”, “complete”, “average”}
Hclustering = AgglomerativeClustering(n_clusters=10, affinity='euclidean', linkage='ward')
Hclustering.fit(Cx)

ms = np.column_stack((ground_truth,Hclustering.labels_))
df = pd.DataFrame(ms, columns = ['Ground truth','Clusters'])
pd.crosstab(df['Ground truth'], df['Clusters'], margins=True)

# How good is the results?
from sklearn import metrics
metrics.adjusted_rand_score(ground_truth,Hclustering.labels_)

from sklearn.cluster import DBSCAN
from collections import Counter
for e in range(10,50, 1):
    l = float(e)/10.
    DB = DBSCAN(eps=l, min_samples=25, random_state=1)
    DB.fit(Cx)
    print l, unique(DB.labels_)
    print Counter(DB.labels_)

from sklearn.cluster import DBSCAN
DB = DBSCAN(eps=4.35, min_samples=25, random_state=1)
DB.fit(Cx)

from collections import Counter
print Counter(DB.labels_)

import matplotlib.pyplot as plt
for k,cl in enumerate(np.unique(DB.labels_)):
    if cl >= 0:
        example = np.min(np.where(DB.labels_==cl))
        plt.subplot(2, 3, k)
        plt.imshow(digits.images[example],cmap='binary',interpolation='none')
        plt.title('cl '+str(cl))
plt.show()

ms = np.column_stack((ground_truth,DB.labels_))
df = pd.DataFrame(ms, columns = ['Ground truth','Clusters'])
pd.crosstab(df['Ground truth'], df['Clusters'], margins=True)

import numpy as np
A = np.array([165, 55, 70])
B = np.array([185, 60, 30])

D = (A-B)
D = D**2
D = np.sqrt(np.sum(D))

print D
