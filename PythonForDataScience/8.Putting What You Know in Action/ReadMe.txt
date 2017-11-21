Previous chapters have all been preparatory in nature. You have discovered
how to perform essential data science tasks using Python. In addition,
you spent time working with the various tools that Python provides to
make data science tasks easier. All this information is essential, but it doesn’t
help you see the big picture — where all the pieces go. This chapter shows
you how to employ the techniques you discovered in previous chapters to
solve real data science problems.
This chapter isn’t the end of the journey — it’s the beginning. Think of previous
chapters in the same way as you think about packing your bags, making
reservations, and creating an itinerary before you go on a trip. This chapter
is the trip to the airport, during which you start to see everything come
together.
The chapter begins by looking at the aspects you normally have to consider
when trying to solve a data science problem. You can’t just jump in and
start performing an analysis; you must understand the problem first, as well
as consider the resources (in the form of data, algorithms, computational
resources) to solve it. Putting the problem into a context, a setting of a sort,
helps you understand the problem and define how the data relates to that
problem. The context is essential because, like language, context alters the
meaning of both the problem and its associated data. For example, when you
say, “I have a red rose” to your significant other, the meaning behind the sentence
has one connotation. If you say the same sentence to a fellow gardener,
the connotation is different. The rose is a sort of data and the person you’re
speaking to is the context. There is no meaning to saying, “I have a red rose.”
unless you know the context in which the statement is made. Likewise, data
has no meaning; it doesn’t answer any question until you know the context in 
which the data is used. Saying “I have data” expresses a question, “What does
the data mean?”
In the end, you’ll need one or more datasets. Two dimensional data tables
(datasets) consist of cases (the rows) and features (the columns). You can
also refer to features as variables when using a statistical terminology. The
features you decide to use for any given dataset determine the kinds of analysis
you can perform, the ways in which you can manipulate the data, and
ultimately the sorts of results you obtain. Determining what sorts of features
you can create from source data and how you must transform the data to
ensure that it works for the analysis you want to perform is an essential part
of developing a data science solution.
After you get a picture of what your problem is, the resources you have to
solve it, and the inputs you need to work with to solve it, you’re ready to
perform some actual work. The last section of this chapter shows you how to
perform simple tasks efficiently. You can usually perform tasks using more
than one methodology, but when working with big data, the fastest routes are
better. By working with arrays and matrices to perform specific tasks, you’ll
notice that certain operations can take a long time unless you leverage some
computational tricks. Using computational tricks is one of the most basic
forms of manipulation you perform, but knowing about them from the beginning
is essential. Applying these techniques paves the road to later chapters
when you start to look at the magic that data science can truly accomplish in
helping you see more in the data you have than is nominally apparent.
You don’t have to type the source code for this chapter manually. In fact,
it’s a lot easier if you use the downloadable source (see the Introduction
for download instructions). The source code for this chapter appears in the
P4DS4D; 08; Operations on Arrays and Matrices.ipynb source
code file.