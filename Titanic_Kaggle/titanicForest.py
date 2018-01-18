"""
Titanic Binary Classification using Random Forests
Samuel L. Peoples
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
X_train = pd.read_csv('Data/train_wrangled_X.csv').values
y_train = pd.read_csv('Data/train_wrangled_y.csv').values
X_test = pd.read_csv('Data/test_wrangled.csv').values
y_test = pd.read_csv('Data/y_test_wrangled.csv').values

# Splitting the dataset into the Training set and Test set
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Feature Scaling
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("Accuracy: "+str((241+114)/(241+114+38+25)))
"""
[[241  25]
 [ 38 114]]
Accuracy: 84.93%
"""