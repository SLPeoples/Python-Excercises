Python Exercises completed from Python for Data Science by John Paul Mueller and Luca Massaron.
Use of Anaconda, Canopy, pythonxy, and WinPython.
Conducts a review of python covering
	Numbers and logic
	Strings, Dates, Functions
	Loops, sets, lists, and tuples
	Iterators and dictionaries
Exercises covering streaming and sampling data; accessing, managing, and interacting with relational
databases and NoSQL databases, as well as data from the web.
Exercises in numpy and pandas
Validation of data
Manipulation of categorical variables
Dealing with missing data
Filtering data
Uses of Matloplib and visualizations as well as Ipython, algorithms, and regression trees.

Table of Contents

Introduction 1

About This Book 1

Foolish Assumptions 2

Icons Used in This Book 3

Beyond the Book 4

Where to Go from Here 5

Part I: Getting Started with Python for Data Science 7

Chapter 1: Discovering the Match between Data Science and Python 9

Defining the Sexiest Job of the 21st Century 11

Considering the emergence of data science 11

Outlining the core competencies of a data scientist 12

Linking data science and big data 13

Understanding the role of programming 13

Creating the Data Science Pipeline 14

Preparing the data 14

Performing exploratory data analysis 15

Learning from data 15

Visualizing 15

Obtaining insights and data products 15

Understanding Python’s Role in Data Science 16

Considering the shifting profile of data scientists 16

Working with a multipurpose, simple, and efficient language 17

Learning to Use Python Fast 18

Loading data 18

Training a model 18

Viewing a result 20

Chapter 2: Introducing Python’s Capabilities and Wonders 21

Why Python? 22

Grasping Python’s core philosophy 23

Discovering present and future development goals 23

Working with Python 24

Getting a taste of the language 24

Understanding the need for indentation 25

Working at the command line or in the IDE 25

Performing Rapid Prototyping and Experimentation 29

Considering Speed of Execution 30

Visualizing Power 32

Using the Python Ecosystem for Data Science 33

Accessing scientific tools using SciPy 33

Performing fundamental scientific computing using NumPy 34

Performing data analysis using pandas 34

Implementing machine learning using Scikit ]learn 35

Plotting the data using matplotlib 35

Parsing HTML documents using Beautiful Soup 35

Chapter 3: Setting Up Python for Data Science 37

Considering the Off ]the ]Shelf Cross ]Platform Scientific Distributions 38

Getting Continuum Analytics Anaconda 39

Getting Enthought Canopy Express 40

Getting pythonxy 40

Getting WinPython 41

Installing Anaconda on Windows 41

Installing Anaconda on Linux 45

Installing Anaconda on Mac OS X 46

Downloading the Datasets and Example Code 47

Using IPython Notebook 47

Defining the code repository 48

Understanding the datasets used in this book 54

Chapter 4: Reviewing Basic Python 57

Working with Numbers and Logic 59

Performing variable assignments 60

Doing arithmetic 61

Comparing data using Boolean expressions 62

Creating and Using Strings 65

Interacting with Dates 66

Creating and Using Functions 68

Creating reusable functions 68

Calling functions in a variety of ways 70

Using Conditional and Loop Statements 73

Making decisions using the if statement 73

Choosing between multiple options using nested decisions 74

Performing repetitive tasks using for 75

Using the while statement 76

Storing Data Using Sets, Lists, and Tuples 77

Performing operations on sets 77

Working with lists 78

Creating and using Tuples 80

Defining Useful Iterators 81

Indexing Data Using Dictionaries 82

Part II: Getting Your Hands Dirty with Data 83

Chapter 5: Working with Real Data 85

Uploading, Streaming, and Sampling Data 86

Uploading small amounts of data into memory 87

Streaming large amounts of data into memory 88

Sampling data 89

Accessing Data in Structured Flat ]File Form 90

Reading from a text file 91

Reading CSV delimited format 92

Reading Excel and other Microsoft Office files 94

Sending Data in Unstructured File Form 95

Managing Data from Relational Databases 98

Interacting with Data from NoSQL Databases 100

Accessing Data from the Web 101

Chapter 6: Conditioning Your Data 105

Juggling between NumPy and pandas 106

Knowing when to use NumPy 106

Knowing when to use pandas 106

Validating Your Data 107

Figuring out what’s in your data 108

Removing duplicates 109

Creating a data map and data plan 110

Manipulating Categorical Variables 112

Creating categorical variables 113

Renaming levels 114

Combining levels 115

Dealing with Dates in Your Data 116

Formatting date and time values 117

Using the right time transformation 117

Dealing with Missing Data 118

Finding the missing data 119

Encoding missingness 119

Imputing missing data 120

Slicing and Dicing: Filtering and Selecting Data 122

Slicing rows 122

Slicing columns 123

Dicing 123

Concatenating and Transforming 124

Adding new cases and variables 125

Removing data 126

Sorting and shuffling 127

Aggregating Data at Any Level 128

Chapter 7: Shaping Data 131

Working with HTML Pages 132

Parsing XML and HTML 132

Using XPath for data extraction 133

Working with Raw Text 134

Dealing with Unicode 134

Stemming and removing stop words 136

Introducing regular expressions 137

Using the Bag of Words Model and Beyond 140

Understanding the bag of words model 141

Working with n ]grams 142

Implementing TF ]IDF transformations 144

Working with Graph Data 145

Understanding the adjacency matrix 146

Using NetworkX basics 146

Chapter 8: Putting What You Know in Action 149

Contextualizing Problems and Data 150

Evaluating a data science problem 151

Researching solutions 151

Formulating a hypothesis 152

Preparing your data 153

Considering the Art of Feature Creation 153

Defining feature creation 153

Combining variables 154

Understanding binning and discretization 155

Using indicator variables 155

Transforming distributions 156

Performing Operations on Arrays 156

Using vectorization 157

Performing simple arithmetic on vectors and matrices 157

Performing matrix vector multiplication 158

Performing matrix multiplication 159

Part III: Visualizing the Invisible 161

Chapter 9: Getting a Crash Course in MatPlotLib 163

Starting with a Graph 164

Defining the plot 164

Drawing multiple lines and plots 165

Saving your work 165

Setting the Axis, Ticks, Grids 166

Getting the axes 167

Formatting the axes 167

Adding grids 168

Defining the Line Appearance 169

Working with line styles 170

Using colors 170

Adding markers 172

Using Labels, Annotations, and Legends 173

Adding labels 174

Annotating the chart 174

Creating a legend 175

Chapter 10: Visualizing the Data 179

Choosing the Right Graph 180

Showing parts of a whole with pie charts 180

Creating comparisons with bar charts 181

Showing distributions using histograms 183

Depicting groups using box plots 184

Seeing data patterns using scatterplots 185

Creating Advanced Scatterplots 187

Depicting groups 187

Showing correlations 188

Plotting Time Series 189

Representing time on axes 190

Plotting trends over time 191

Plotting Geographical Data 193

Visualizing Graphs 195

Developing undirected graphs 195

Developing directed graphs 197

Chapter 11: Understanding the Tools 199

Using the IPython Console 200

Interacting with screen text 200

Changing the window appearance 202

Getting Python help 203

Getting IPython help 205

Using magic functions 205

Discovering objects 207

Using IPython Notebook 208

Working with styles 208

Restarting the kernel 210

Restoring a checkpoint 210

Performing Multimedia and Graphic Integration 212

Embedding plots and other images 212

Loading examples from online sites 212

Obtaining online graphics and multimedia 212

Part IV: Wrangling Data 215

Chapter 12: Stretching Python’s Capabilities 217

Playing with Scikit ]learn 218

Understanding classes in Scikit ]learn 218

Defining applications for data science 219

Performing the Hashing Trick 222

Using hash functions 223

Demonstrating the hashing trick 223

Working with deterministic selection 225

Considering Timing and Performance 227

Benchmarking with timeit 228

Working with the memory profiler 230

Running in Parallel 232

Performing multicore parallelism 232

Demonstrating multiprocessing 233

Chapter 13: Exploring Data Analysis 235

The EDA Approach 236

Defining Descriptive Statistics for Numeric Data 237

Measuring central tendency 238

Measuring variance and range 239

Working with percentiles 239

Defining measures of normality 240

Counting for Categorical Data 241

Understanding frequencies 242

Creating contingency tables 243

Creating Applied Visualization for EDA 243

Inspecting boxplots 244

Performing t ]tests after boxplots 245

Observing parallel coordinates 246

Graphing distributions 247

Plotting scatterplots 248

Understanding Correlation 250

Using covariance and correlation 250

Using nonparametric correlation 252

Considering chi ]square for tables 253

Modifying Data Distributions 253

Using the normal distribution 254

Creating a Z ]score standardization 254

Transforming other notable distributions 254

Chapter 14: Reducing Dimensionality 257

Understanding SVD 258

Looking for dimensionality reduction 259

Using SVD to measure the invisible 260

Performing Factor and Principal Component Analysis 261

Considering the psychometric model 262

Looking for hidden factors 262

Using components, not factors 263

Achieving dimensionality reduction 264

Understanding Some Applications 264

Recognizing faces with PCA 265

Extracting Topics with NMF 267

Recommending movies 270

Chapter 15: Clustering 273

Clustering with K ]means 275

Understanding centroid ]based algorithms 275

Creating an example with image data 277

Looking for optimal solutions 278

Clustering big data 281

Performing Hierarchical Clustering 282

Moving Beyond the Round-Shaped Clusters: DBScan 286

Chapter 16: Detecting Outliers in Data 289

Considering Detection of Outliers 290

Finding more things that can go wrong 291

Understanding anomalies and novel data 292

Examining a Simple Univariate Method 292

Leveraging on the Gaussian distribution 294

Making assumptions and checking out 295

Developing a Multivariate Approach 296

Using principal component analysis 297

Using cluster analysis 298

Automating outliers detection with SVM 299

Part V: Learning from Data 301

Chapter 17: Exploring Four Simple and Effective Algorithms 303

Guessing the Number: Linear Regression 304

Defining the family of linear models 304

Using more variables 305

Understanding limitations and problems 307

Moving to Logistic Regression 307

Applying logistic regression 308

Considering when classes are more 309

Making Things as Simple as Naïve Bayes 310

Finding out that Naïve Bayes isn’t so naïve 312

Predicting text classifications 313

Learning Lazily with Nearest Neighbors 315

Predicting after observing neighbors 316

Choosing your k parameter wisely 317

Chapter 18: Performing Cross ]Validation, Selection, and Optimization 319

Pondering the Problem of Fitting a Model 320

Understanding bias and variance 321

Defining a strategy for picking models 322

Dividing between training and test sets 325

Cross ]Validating 328

Using cross ]validation on k folds 329

Sampling stratifications for complex data 329

Selecting Variables Like a Pro 331

Selecting by univariate measures 331

Using a greedy search 333

Pumping Up Your Hyperparameters 334

Implementing a grid search 335

Trying a randomized search 339

Chapter 19: Increasing Complexity with Linear and Nonlinear Tricks 341

Using Nonlinear Transformations 341

Doing variable transformations 342

Creating interactions between variables 344

Regularizing Linear Models 348

Relying on Ridge regression (L2)349

Using the Lasso (L1) 349

Leveraging regularization 350

Combining L1 & L2: Elasticnet 350

Fighting with Big Data Chunk by Chunk 351

Determining when there is too much data 351

Implementing Stochastic Gradient Descent 351

Understanding Support Vector Machines 354

Relying on a computational method 355

Fixing many new parameters 358

Classifying with SVC 360

Going nonlinear is easy 365

Performing regression with SVR 366

Creating a stochastic solution with SVM 368

Chapter 20: Understanding the Power of the Many 373

Starting with a Plain Decision Tree 374

Understanding a decision tree 374

Creating classification and regression trees 376

Making Machine Learning Accessible 379

Working with a Random Forest classifier 381

Working with a Random Forest regressor 382

Optimizing a Random Forest 383

Boosting Predictions 384

Knowing that many weak predictors win 384

Creating a gradient boosting classifier 385

Creating a gradient boosting regressor 386

Using GBM hyper ]parameters 387

Part VI: The Part of Tens 389

Chapter 21: Ten Essential Data Science Resource Collections 391

Gaining Insights with Data Science Weekly 392

Obtaining a Resource List at U Climb Higher 392

Getting a Good Start with KDnuggets 392

Accessing the Huge List of Resources on Data Science Central 393

Obtaining the Facts of Open Source Data Science from Masters 394

Locating Free Learning Resources with Quora 394

Receiving Help with Advanced Topics at Conductrics 394

Learning New Tricks from the Aspirational Data Scientist 395

Finding Data Intelligence and Analytics Resources at AnalyticBridge 396

Zeroing In on Developer Resources with Jonathan Bower 396

Chapter 22: Ten Data Challenges You Should Take 397

Meeting the Data Science London + Scikit ]learn Challenge 398

Predicting Survival on the Titanic 399

Finding a Kaggle Competition that Suits Your Needs 399

Honing Your Overfit Strategies 400

Trudging Through the MovieLens Dataset 401

Getting Rid of Spam Emails 401

Working with Handwritten Information 402

Working with Pictures 403

Analyzing Amazon.com Reviews 404

Interacting with a Huge Graph 405

Index 407