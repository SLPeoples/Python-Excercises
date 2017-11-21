#Samuel L. Peoples
import random
import pandas as pd

from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm


#Basic file reading
def printContents():
    with open('colors.txt', 'r') as input:
        print ('colors.txt content:\n'+ input.read())
#Streaming
def streamContents():
    with open('colors.txt', 'r') as input:
        for obs in input:
            print ('reading: '+ obs)
            
#sampling
def sampleContents():
    n = 2
    with open('colors.txt', 'r') as input:
        for j, obs in enumerate(input):
            if j % n ==0:
                print ('reading: '+str(j) +' content ' +obs)
#random Sampling
def randomSample():
    sampleSize = 25
    print('indication')
    with open('colors.txt', 'r') as input:
        for j, obs in enumerate(input):
            if random.randint(1,100) <= sampleSize:
                print ('reading: '+str(j) +' content ' +obs)
#pandas
#Reads data from table, csv, and xls
def pandaStuff():
   colorTable = pd.io.parsers.read_table("colors.txt")
   #print(colorTable)
   assetTable = pd.io.parsers.read_csv('csvSample.csv')
   #print(assetTable)
   #print(assetTable[['EN']])
   xls = pd.ExcelFile("xls5k.xls")
   values = xls.parse('Sample-spreadsheet-file', index_col = 1, na_values=['NA'])
   #print(values)
   xlsTable = pd.read_excel('xls5k.xls')
   #print(xlsTable)

#skimage
#Opens a file and manipulates an image from the web
def skimageStuff():
    exFile = ("https://goo.gl/8vdzVi")
    image = imread(exFile, as_grey=True)
    plt.imshow(image,cmap=cm.gray)
    plt.show()
    print("dataType: %s, shape: %s" %(type(image), image.shape))
    image2 = image[149:644,870:1324]
    plt.imshow(image2,cmap=cm.gray)
    plt.show()
    image3 = resize(image2, (200,200), mode='edge')
    plt.imshow(image3,cmap=cm.gray)
    plt.show()
    print("dataType: %s, shape: %s" %(type(image3), image3.shape))
    imgRow = image3.flatten()
    print("dataType: %s, shape: %s" %(type(imgRow), imgRow.shape))


def main():
    #printContents()
    #streamContents()
    #sampleContents()
    #randomSample()
    #randomSample()
    #randomSample()
    #randomSample()
    #pandaStuff()
    #skimageStuff()

if __name__ == "__main__": main()