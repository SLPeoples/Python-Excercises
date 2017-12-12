
from nltk.classify import NaiveBayesClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

positive_tweets = [('Flowers smell good', 'positive'),
                   ('Birds are beautiful', 'positive'),
                   ('This is going to be a great day', 'positive'),
                   ('I love my bff', 'positive'),
                   ('This restaurant has great food', 'positive')]

negative_tweets = [('Onions smell bad', 'negative'),
                   ('Garbage is ugly', 'negative'),
                   ('Nothing has gone right today', 'negative'),
                   ('I hate my boss', 'negative'),
                   ('This restaurant has terrible food', 'negative')]

test_tweets = [('Singing makes me happy', 'positive'),
               ('Blue skies are nice', 'positive'),
               ('I love spring', 'positive'),
               ('Coughing makes me sad', 'negative'),
               ('Cloudy skies are depressing', 'negative'),
               ('I hate winter', 'negative')]

X_train, y_train = zip(*positive_tweets+negative_tweets)

X_test, y_test = zip(*test_tweets)

tfidfvec = TfidfVectorizer(lowercase=True)
vectorized = tfidfvec.fit_transform(X_train)

sentiment_classifier = LogisticRegression()
sentiment_classifier.fit(vectorized,y_train)

vectorized_test = tfidfvec.transform(X_test)
prediction = list(sentiment_classifier.predict(vectorized_test))
probabilities = list(sentiment_classifier.predict_proba(vectorized_test)[:,1])

print 'correct labels : %s %s %s %s %s %s' % y_test
print 'prediction     : %s %s %s %s %s %s' % tuple(prediction)
print 'proba positive : %0.6f %0.6f %0.6f %0.6f %0.6f %0.6f' % tuple(probabilities)
