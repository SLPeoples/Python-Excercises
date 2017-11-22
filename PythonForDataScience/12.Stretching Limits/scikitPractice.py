#Samuel L. Peoples
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import csc_matrix
import sklearn.feature_extraction.text as txt
import timeit

#Working with the boston dataset
def boston():
    boston = load_boston()
    x, y = boston.data,boston.target
    #both x and y have 506 entries where x has 13 features
    print (x.shape, y.shape)
    hypothesis = LinearRegression(normalize=True)
    hypothesis.fit(x,y)
    #Prints the 13 feature 
    print (hypothesis.coef_)
    #A hypothesis is a way to describe a learning algorithm trained with data. The
    #hypothesis defines a possible representation of y given X that you test for
    #validity. Therefore, it's a hypothesis in both scientific and machine-learning
    #language.
    
    #Here we define a new observation, and have to reshape because of errors thrown
    new_observation = np.array([1,0,1,0,0.5,7,59,6,3,200,20,350,4],dtype=float).reshape(1,-1)
    print (hypothesis.predict(new_observation))
    #In this case, score returns the coefficient of determination R^2 of the
    #prediction. R^2 is a measure ranging from 0 to 1, comparing our predictor
    #to a simple mean. Higher values show that the predictor is working well. 
    print(hypothesis.score(x,y))
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    #scales the features to be between 0 and 1.
    #In this case, the code applies the min and max values learned from X to the
    #new_observation variable, and returns a transformation
    scaler.fit(x)
    print (scaler.transform(new_observation))
    
#exercises in hashing
def hashTrick():
    #prints the hash of 'Hash'
    print(hash('Hash'))
    #Let's make that number smaller
    print(abs(hash('Hash')) % 1000)
    #Check the results using two strings
    def hashing_trick(input_string, vector_size=20):
        feature_vector = [0] * vector_size
        for word in input_string.split(' '):
            index = abs(hash(word)) % vector_size
            feature_vector[index] = 1
        return feature_vector 
    print(hashing_trick('Python for data science'))
    print (csc_matrix(hashing_trick('Python for data science')))
    print()
    print(hashing_trick('Python for machine learning'))
    print (csc_matrix(hashing_trick('Python for machine learning')))
    #Notice:
        #You don't know where each word is located. When it's important to be
        #able to reverse the process of assigning words to indexes, you must
        #store the relationship between words and their hashed value separately
        #(for example, you can use a dictionary where the keys are the hashed
        #values and the values are the words).
        #For small values of the vector_size function parameter (for example,
        #vector_size=10), many words overlap in the same positions in the list
        #representing the feature vector. To keep the overlap to a minimum, you
        #must create hash function boundaries that are greater than the number
        #of elements you plan to index later.
    #this does a similar encoding as above, but creates a matrix instead of two vectors
    one_hot_enconder = txt.CountVectorizer()
    one_hot_enconded = one_hot_enconder.fit_transform(['Python for data science','Python for machine learning'])
    #attribute error, new text arriving causes countVectorizer to fail
    #one_hot_enconded.transform(['New text has arrived'])
    print()
    print(one_hot_enconded)
    
    print()
    sklearn_hashing_trick = txt.HashingVectorizer(n_features=20, binary=True, norm=None)
    text_vector = sklearn_hashing_trick.transform(['Python for data science','Python for machine learning'])
    print(text_vector.astype)
        #<bound method _data_matrix.astype of <2x20 sparse matrix of type '<class 'numpy.float64'>'
        #with 8 stored elements in Compressed Sparse Row format>>
    print()
    print(sklearn_hashing_trick.transform(['New text has arrived']).astype)
        #<bound method _data_matrix.astype of <1x20 sparse matrix of type '<class 'numpy.float64'>'
        #with 4 stored elements in Compressed Sparse Row format>>
    #notice the number of features is 20, with 4 words in each for text_vector
    #notice the second print statemnet only has 4 words.
    #HashingVectorizer is the perfect function to use when your data can't fit
    #into memory and its features aren't fixed. In the other cases, consider using
    #the more intuitive CountVectorizer.

def timing():
    print(timeit.timeit( '[k for k in range(100)]', number = 1000))
    print('one-hot encoder: '+str(timeit.timeit('import sklearn.feature_extraction.text as txt;sklearn_hashing_trick = txt.HashingVectorizer(n_features=20, binary=True, norm=None);enconder = txt.CountVectorizer();texts = [\'Python for data science\',\'Python for machine learning\'];enconded = enconder.fit_transform(texts)', number = 1000)))
    print('hashing trick: '+str(timeit.timeit('import sklearn.feature_extraction.text as txt;sklearn_hashing_trick = txt.HashingVectorizer(n_features=20, binary=True, norm=None);enconder = txt.CountVectorizer();texts = [\'Python for data science\',\'Python for machine learning\'];hashing = sklearn_hashing_trick.transform(texts)', number = 1000)))
    #0.002080959412988048
    #one-hot encoder: 0.36095307685625666
    #hashing trick: 0.059929076202204334
    
   # In: import sklearn.feature_extraction.text as txt
   #...: sklearn_hashing_trick = txt.HashingVectorizer(n_features=20, binary=True, norm=None)
   #...: enconder = txt.CountVectorizer()
   #...: texts = ['Python for data science','Python for machine learning']
   #...: hashing = sklearn_hashing_trick.transform(texts)
   #...: %memit dense_hashing = hashing.toarray()
   #...:
   #     peak memory: 84.14 MiB, increment: 0.58 MiB
   #In []: %%writefile example_code.py
   #...: import sklearn.feature_extraction.text as txt
   #...: def comparison_test():
   #...:     sklearn_hashing_trick = txt.HashingVectorizer(n_features=20, binary=True, norm=None)
   #...:     one_hot_enconder = txt.CountVectorizer()
   #...:     texts = ['Python for data science','Python for machine learning']
   #...:     one_hot_enconded = one_hot_enconder.fit_transform(texts)
   #...:     hashing = sklearn_hashing_trick.transform(texts)
   #...: from example_code import comparison_test
   #...: %mprun f comparison_test comparison_test()
   #...:
   #    Overwriting example_code.py
    

def main():
    #boston()
    #hashTrick()
    timing()
    
if __name__ == "__main__": main()
