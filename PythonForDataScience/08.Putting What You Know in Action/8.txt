
import numpy as np
dataset = np.array([[2, 4, 6, 8, 3, 2, 5], 
                    [7, 5, 3, 1, 6, 8, 0], 
                    [1, 3, 2, 1, 0, 0, 8]])
print np.max(dataset, axis=1) - np.min(dataset, axis=1)

import numpy as np
a = np.array([15.0, 20.0, 22.0, 75.0, 40.0, 35.0])
a = a*.01
print a

import numpy as np
a = np.array([2, 4, 6, 8])
b = np.array([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6],
              [4, 5, 6, 7]])
c = np.dot(a, b)
print c

import numpy as np

a = np.array([[2, 4, 6, 8],
              [1, 3, 5, 7]])
b = np.array ([[1, 2],
              [2, 3],
              [3, 4],
              [4, 5]])
c = np.dot(a, b)
print c
