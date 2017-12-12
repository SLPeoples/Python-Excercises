
with open("Colors.txt", 'rb') as open_file:
    print 'Colors.txt content:\n' + open_file.read()

with open("Colors.txt", 'rb') as open_file:
    for observation in open_file:
        print 'Reading Data: ' + observation

n = 3
with open("Colors.txt", 'rb') as open_file:
    for j, observation in enumerate(open_file):
        if j % n==0:
            print('Reading Line: ' + str(j) + 
            ' Content: ' + observation)

from random import random
sample_size = 0.25
with open("Colors.txt", 'rb') as open_file:
    for j, observation in enumerate(open_file):
        if random()<=sample_size:
            print('Reading Line: ' + str(j) + 
            ' Content: ' + observation)

import pandas as pd
color_table = pd.io.parsers.read_table("Colors.txt")
print color_table

import pandas as pd
titanic = pd.io.parsers.read_csv("Titanic.csv")
X = titanic[['age']]
#X = titanic[['age']].values
print X

import pandas as pd
xls = pd.ExcelFile("Values.xls")
trig_values = xls.parse('Sheet1', index_col=None, 
                        na_values=['NA'])
#trig_values = pd.read_excel("Values.xls", 'Sheet1', index_col=None, na_values=['NA'])
print trig_values

from skimage.io import imread
from skimage.transform import resize 
from matplotlib import pyplot as plt
import matplotlib.cm as cm

example_file = ("http://upload.wikimedia.org/" +
    "wikipedia/commons/7/7d/Dog_face.png")
image = imread(example_file, as_grey=True)
plt.imshow(image, cmap=cm.gray)
plt.show()

print("data type: %s, shape: %s" % 
      (type(image), image.shape))

image2 = image[5:70,0:70]
plt.imshow(image2, cmap=cm.gray)
plt.show()

image3 = resize(image2, (30, 30), mode='nearest')
plt.imshow(image3, cmap=cm.gray)
print("data type: %s, shape: %s" % 
      (type(image3), image3.shape))

image_row = image3.flatten()
print("data type: %s, shape: %s" % 
      (type(image_row), image_row.shape))

from lxml import objectify
import pandas as pd

xml = objectify.parse(open('XMLData.xml'))
root = xml.getroot()
df = pd.DataFrame(columns=('Number', 'String', 'Boolean'))

for i in range(0,4):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(['Number', 'String', 'Boolean'], 
                   [obj[0].text, obj[1].text, 
                    obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)
    
print df
