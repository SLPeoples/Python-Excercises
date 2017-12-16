
from sklearn.datasets import load_boston
boston = load_boston()
X, y = boston.data,boston.target

from sklearn.linear_model import LinearRegression
hypothesis = LinearRegression(normalize=True)
hypothesis.fit(X,y)

print hypothesis.coef_
