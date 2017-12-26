Chapter 6 demonstrates techniques for working with data as an entity —
as something you work with in Python. However, data doesn’t exist in
a vacuum. It doesn’t just suddenly appear within Python for absolutely no
reason at all. As demonstrated in Chapter 5, you load the data. However,
loading may not be enough — you may have to shape the data as part of
loading it. That’s the purpose of this chapter. You discover how to work with
a variety of container types in a way that makes it possible to load data from
a number of complex container types, such as HTML pages. In fact, you even
work with graphics, images, and sounds.
As you progress through the book, you discover that data takes all kinds of
forms and shapes. As far as the computer is concerned, data consists of 0s
and 1s. Humans give the data meaning by formatting, storing, and interpreting
it in a certain way. The same group of 0s and 1s could be a number, date,
or text, depending on the interpretation. The data container provides clues
as to how to interpret the data, so that’s why this chapter is so important to
you as a data scientist using Python to discover data patterns. You find that
you can discover patterns in places where you might have thought patterns
couldn’t exist.
You don’t have to type the source code for this chapter manually. In fact,
it’s a lot easier if you use the downloadable source (see the Introduction
for download instructions). The source code for this chapter appears in the
P4DS4D; 07; Shaping Data.ipynb source code file.
HTML pages contain data in a hierarchical format. You often find HTML content
in a strict HTML form or as XML. The HTML form can present problems
because it doesn’t always necessarily follow strict formatting rules. XML
does follow strict formatting rules because of the standards used to define it,
which makes it easier to parse. However, in both cases, you use similar techniques
to parse a page. The first section that follows describes how to parse
HTML pages in general.
Sometimes you don’t need all the data on a page. Instead you need specific
data, which is where XPath comes into play. You can use XPath to locate specific
data on the HTML page and extract it for your particular needs.