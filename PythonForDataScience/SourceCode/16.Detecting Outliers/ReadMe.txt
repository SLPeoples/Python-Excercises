Errors happen when you least expect, and that’s also true in regard to
your data. In addition, data errors are difficult to spot, especially when
your dataset contains many variables of different types and scale (a high-
dimensionality data structure).
Data errors can take a number of forms. For example, the values may be
systematically missing on certain variables, erroneous numbers could appear
here and there, and the data could include outliers. A red flag has to be
raised when the following characteristics are met:
? Missing values on certain groups of cases or variables imply that some
specific cause is generating the error.
? Erroneous values depend on how the application has produced or
manipulated the data. For instance, you need to know whether the
application has obtained data from a measurement instrument. External
conditions and human error can affect the reliability of instruments.
? The case is apparently valid, but quite different from the usual values
that characterize that variable. When you can’t explain the reason for
the difference, you could be observing an outlier.
Among the illustrated errors, the trickiest problem to solve is when your
dataset has outliers, because you don’t always have a unique definition of
outliers, or a clear reason to have them in your data. As a result, much is left
to your investigation and evaluation. The good news is that Python offers you
quite a few tools for spotting outliers and other kinds of unexpected values,
so at least you won’t be looking for a needle in a haystack.
You don’t have to type the source code for this chapter manually. In fact,
it’s a lot easier if you use the downloadable source (see the Introduction
for download instructions). The source code for this chapter appears in the
P4DS4D; 16; Outliers.ipynb source code file.