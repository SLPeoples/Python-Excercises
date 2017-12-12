
# coding: utf-8

# # Defining applications for data science

# http://scikit-learn.org/stable/developers/<BR>
# http://scikit-learn.org/stable/faq.html<BR>

# In[1]:


from sklearn.datasets import load_boston
boston = load_boston()
X, y = boston.data,boston.target
print X.shape, y.shape


# In[2]:


from sklearn.linear_model import LinearRegression
hypothesis = LinearRegression(normalize=True)
hypothesis.fit(X,y)


# In[3]:


print hypothesis.coef_


# In[4]:


import numpy as np
new_observation = np.array([1,0,1,0,0.5,7,59,6,3,200,20,350,4],dtype=float)
print hypothesis.predict(new_observation)


# In[5]:


hypothesis.score(X,y)


# In[6]:


#help(LinearRegression)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(X)
print scaler.transform(new_observation)


# # Performing the Hashing Trick

# ## Using hash functions

# In[7]:


print hash('Python')
print abs(hash('Python')) % 1000


# ## Demonstrating the hashing trick

# In[8]:


string_1 = 'Python for data science'
string_2 = 'Python for machine learning'

def hashing_trick(input_string, vector_size=20):
    feature_vector = [0] * vector_size
    for word in input_string.split(' '):
        index = abs(hash(word)) % vector_size
        feature_vector[index] = 1
    return feature_vector

print hashing_trick(input_string='Python for data science', vector_size=20)
print hashing_trick(input_string='Python for machine learning', vector_size=20)


# In[9]:


from scipy.sparse import csc_matrix
print csc_matrix([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0])


# In[10]:


# http://scikit-learn.org/stable/modules/feature_extraction.html
# http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html
from sklearn.feature_extraction.text import HashingVectorizer
sklearn_hashing_trick = HashingVectorizer(n_features=20, binary=True, norm=None)
hashed_text = sklearn_hashing_trick.transform(['Python for data science','Python for machine learning'])
hashed_text


# In[11]:


from sklearn.feature_extraction.text import CountVectorizer
one_hot_enconder = CountVectorizer()
one_hot_enconded = one_hot_enconder.fit_transform(['Python for data science','Python for machine learning'])


# In[12]:


print one_hot_enconder.vocabulary_


# In[13]:


sklearn_hashing_trick.transform(['New text has arrived'])


# In[14]:


one_hot_enconder.fit_transform(['New text has arrived'])


# # Performance testing

# In[15]:


get_ipython().magic('timeit l = [k for k in range(10**6)]')


# In[16]:


get_ipython().magic('timeit -n 20 -r 5 l = [k for k in range(10**6)]')


# In[17]:


get_ipython().run_cell_magic('timeit', '', 'l = list()\nfor k in range(10**6):\n    l.append(k)')


# In[18]:


from sklearn.feature_extraction.text import HashingVectorizer, CountVectorizer
sklearn_hashing_trick = HashingVectorizer(n_features=20, binary=True, norm=None) 
one_hot_enconder = CountVectorizer()
texts = ['Python for data science','Python for machine learning']


# In[19]:


get_ipython().magic('timeit one_hot_enconded = one_hot_enconder.fit_transform(texts)')


# In[20]:


get_ipython().magic('timeit hashing = sklearn_hashing_trick.transform(texts)')


# In[21]:


import timeit
cumulative_time = timeit.timeit("hashing = sklearn_hashing_trick.transform(texts)", 
                                 "from __main__ import sklearn_hashing_trick, texts", 
                                 number=10000)
print cumulative_time / 10000.0


# ## Memory profiler

# In[22]:


# Installation procedures from the command line:
# pip install psutil
# pip install memory_profiler


# In[23]:


# Initialization from IPython (to be repeat at every IPython start)
get_ipython().magic('load_ext memory_profiler')


# In[24]:


hashing = sklearn_hashing_trick.transform(texts)
get_ipython().magic('memit dense_hashing = hashing.toarray()')


# In[25]:


get_ipython().run_cell_magic('writefile', 'example_code.py', "from sklearn.feature_extraction.text import HashingVectorizer, CountVectorizer\ndef comparison_test():\n    sklearn_hashing_trick = HashingVectorizer(n_features=20, binary=True, norm=None) \n    one_hot_enconder = CountVectorizer()\n    texts = ['Python for data science','Python for machine learning']\n    one_hot_enconded = one_hot_enconder.fit_transform(texts)\n    hashing = sklearn_hashing_trick.transform(texts)")


# In[26]:


from example_code import comparison_test
get_ipython().magic('mprun -f comparison_test comparison_test()')


# # Demonstrating multiprocessing techniques

# In[ ]:


from sklearn.datasets import load_digits
digits = load_digits()
X, y = digits.data,digits.target
from sklearn.svm import SVC
from sklearn.cross_validation import cross_val_score


# In[ ]:


get_ipython().magic('timeit single_core_learning = cross_val_score(SVC(), X, y, cv=20, n_jobs=1)')


# In[ ]:


get_ipython().magic('timeit multi_core_learning = cross_val_score(SVC(), X, y, cv=20, n_jobs=-1)')

