Big data is defined as a collection of datasets that is so huge that it
becomes difficult to process using traditional techniques. The manipulation
of big data differentiates statistical problems, which are based on small
samples, from data science problems. You typically use traditional statistical
techniques on small problems and data science techniques on big problems.
Data may be viewed as big because it consists of many examples, and this is
the first kind of big that spontaneously comes to mind. Analyzing a database
of millions of customers and interacting with them all simultaneously is really
challenging, but that isn’t the only possible perspective of big data.
Another potential view of big data relates to its production and velocity, that
is, the time dimension. Even if your observations are few, producing data
points for an extended time frame results in a huge stack of information. The
dataset reports each instant’s persistency or change of your cases.
A third view of big data is data dimensionality, which refers to how many
aspects of the cases an application tracks. Data with high dimensionality may
offer many features (variables) — often hundreds or thousands of them. And
that may turn into a real problem. Even if you’re observing only a few cases for a
short time, dealing with too many features can make most analysis intractable.
The complexity of working with so many dimensions drives the necessity
for various data techniques to filter the information — keeping the data that
seems to solve the problem better. The filter reduces dimensionality by
removing redundant information in high-dimension datasets.
The focus in this chapter is on reducing data dimensions when the data has
too many repetitions of the same information. You can view this reduction as
a kind of information compression, which is similar to compressing files on a
hard disk in order to save space.
You don’t have to type the source code for this chapter manually. In fact,
it’s a lot easier if you use the downloadable source (see the Introduction
for download instructions). The source code for this chapter appears in the
P4DS4D; 14; Reducing Dimensionality.ipynb source code file.