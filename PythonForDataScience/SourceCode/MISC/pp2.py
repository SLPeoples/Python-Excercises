
from skimage.io import imread
from skimage.transform import resize 
from matplotlib import pyplot as plt
import matplotlib.cm as cm

example_file = (
    "http://blog.johnmuellerbooks.com/" +
    "wp-content/uploads/2015/04/Layer-Hens.jpg")
image = imread(example_file, as_grey=True)
print image

image2 = resize(image, (50, 50), mode='nearest')
print image2

%matplotlib inline
plt.imshow(image, cmap=cm.gray)
plt.show()
