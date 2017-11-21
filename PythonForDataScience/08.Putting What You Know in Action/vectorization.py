#Samuel L. Peoples
import numpy as np

#introducing vectorization
def vectors():
    dataset = np.array([[2, 4, 6, 8, 3, 2, 5],
                        [7, 5, 3, 1, 6, 8, 0],
                        [1, 3, 2, 1, 0, 0, 8]])
    #prints the max of each row, [8,8,8] subtracting the min from each row [2,0,0]
    print (np.max(dataset, axis=1) - np.min(dataset, axis=1))
    
    a = np.array([15.0, 20.0, 22.0, 75.0, 40.0, 35.0])
    print (a)
    #componentwise multiplication
    a = a*.01
    print (a)
    
    #vector multiplication
    a = np.array([2, 4, 6, 8])
    b = np.array([[1, 2, 3, 4],
                  [2, 3, 4, 5],
                  [3, 4, 5, 6],
                  [4, 5, 6, 7]])
    #dot product using vector
    c = np.dot(a, b)
    print (c)
    
    a = np.array([[2, 4, 6, 8],
                  [1, 3, 5, 7]])
    b = np.array ([[1, 2],
                   [2, 3],
                   [3, 4],
                   [4, 5]])
    #simple matrix transformations
    c = np.dot(a, b)
    print (c)

def main():
    vectors()
if __name__ == "__main__": main()