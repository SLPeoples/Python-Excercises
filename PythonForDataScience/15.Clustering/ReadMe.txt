One of the basic abilities that humans have exercised since primitive
times is to divide the known world into separate classes where individual
objects share common features deemed important by the classifier.
Starting with primitive cave dwellers classifying the natural world they lived
in, distinguishing plants and animals useful or dangerous for their survival, we
arrive at modern times in which marketing departments classify consumers
into target segments and then act with proper marketing plans.
Classifying is crucial to our process of building new knowledge because, by
gathering similar objects, we can
? Mention all the items in a class by the same denomination
? Summarize relevant features by an exemplificative class type
? Associate particular actions or recall specific knowledge automatically
Dealing with big data streams today requires the same classificatory ability,
but on a different scale. To spot unknown groups of signals present in the
data, we need specialized algorithms that are both able to learn how to assign
examples to certain given classes (the supervised approach) and to spot new
interesting classes that we weren’t aware of (unsupervised learning).
Even though your main routine as a data scientist will be to put into practice
your predictive skills, you’ll also have to provide useful insight into possible
structured information present in your data. For example, you’ll often need
to locate new features in order to strengthen the predictive power of your
models, find an easy way to make complex comparisons inside the data, and
discover communities in social networks.
A data-driven approach to classification, called clustering, will prove to be
of great help in achieving success for your data project when you need to
provide new insights from scratch.
Clustering techniques are a set of unsupervised classification methods that
can create meaningful classes by directly processing your data, without any
previous knowledge or hypothesis about the groups that may be present. If
all supervised algorithms need labeled examples (class labels), unsupervised
ones can figure out by themselves what the most appropriate labels could be.
There are a few kinds of clustering techniques. You can distinguish between
them using the guidelines in the following list:
? Assigning every example to a unique group (partitioning) or to multiple
ones (fuzzy clustering)
? Determining the heuristic — that is, the rule of thumb — that they use to
figure out whether an example is part of a group
? Specifying how they quantify the difference between observations, that
is, the so-called distance measure
Most of the time you use partition-clustering techniques (a data point can be
part of only one group, so the groups don’t overlap; their membership is
distinct) and among partitioning methods, you use K-means the most. But
other useful methods are mentioned in this chapter, which are based on
agglomerative methods and on data density.
Agglomerative methods link data points into clusters based on their distance.
Data density approaches take advantage of the idea that groups are very
dense and continuous, so if you notice a decrease in density when exploring
a part of a group of points, it could mean that you arrived at one of its
borders.
Because you normally don’t know what you’re looking for, different methods
can provide you with different solutions and points of view on the data. The
secret of a successful clustering is to try as many of the recipes as possible,
compare the results, and try to find a reason why you can consider certain
observations as a group in respect to others.
You don’t have to type the source code for this chapter manually. In fact,
it’s a lot easier if you use the downloadable source (see the Introduction
for download instructions). The source code for this chapter appears in the
P4DS4D; 15; Clustering.ipynb source code file.