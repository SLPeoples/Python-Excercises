Data science applications require data by definition. It would be nice if
you could simply go to a data store somewhere, purchase the data you
need in an easy-open package, and then write an application to access that
data. However, data is messy. It appears in all sorts of places, in many different
forms, and you can interpret it in many different ways. Every organization
has a different method of viewing data and stores it in a different manner as
well. Even when the data management system used by one company is the
same as the data management system used by another company, the chances
are slim that the data will appear in the same format or even use the same
data types. In short, before you can do any data science work, you must discover
how to access the data in all its myriad forms. Real data requires a lot
of work to use and fortunately, Python is up to the task of manipulating it as
needed.
This chapter helps you understand the techniques required to access data
in a number of forms and locations. For example, memory streams represent
a form of data storage that your computer supports natively; flat files exist
on your hard drive; relational databases commonly appear on networks
(although smaller relational databases, such as those found in Access, could
appear on your hard drive as well); and web-based data usually appears on
the Internet. You won’t visit every form of data storage available (such as
that stored on a point-of-sale, or POS, system). Quite possibly, an entire book
on the topic wouldn’t suffice to cover the topic of data formats in any detail. 
However, the techniques in this chapter do demonstrate how to access
data in the formats you most commonly encounter when working with
real-world data.
The Scikit-learn library includes a number of toy datasets (small datasets
meant for you to play with). These datasets are complex enough to perform a
number of tasks, such as experimenting with Python to perform data science
tasks. Because this data is readily available, and making the examples too
complicated to understand is a bad idea, this book relies on these toy datasets
as input for many of the examples. Even though the book does use these
toy datasets for the sake of reducing complexity and making the examples
clearer, the techniques that the book demonstrates work equally well on
real-world data that you access using the techniques shown in this chapter.
You don’t have to type the source code for this chapter in by hand. In fact,
it’s a lot easier if you use the downloadable source (see the Introduction
for download instructions). The source code for this chapter appears in the
P4DS4D; 05; Dataset Load.ipynb source code file.
It’s essential that the Colors.txt, Titanic.csv, Values.xls, and
XMLData.xml files that come with the downloadable source code appear in
the same folder (directory) as your IPython Notebook files. Otherwise, the
examples in the following sections fail with an input/output (IO) error. The
file location varies according to the platform you’re using. For example, on a
Windows system, you find the notebooks stored in the C:\Users\Username\
My Documents\IPython Notebooks folder, where Username is your
login name. To make the examples work, simply copy the four files from the
downloadable source folder into your IPython Notebook folder.
