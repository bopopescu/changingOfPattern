import argparse
import io
import os
import math
import numpy as np

from google.cloud import vision

# Instantiates a client
vision_client = vision.Client()

#send image to api
def sendImage(filename):
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    filename)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()
	    image = vision_client.image(
	        content=content)

	    image = vision_client.image(content=content)

	    props = image.detect_properties()

	    #array with 1st pattern
	    j1 = []
	    for score in props.colors:
	        j1.append(score.score)
	        # print(j1)

	return j1

j1Num = sendImage('pattern.jpg')
# convert array as a numpy array
j1 = np.array(j1Num)
print("j1:")
print(j1)

j2Num = sendImage('pattern0.0.jpg')
j2 = np.array(j2Num)
print ("j2")
print j2

# transpose the 1st array
j1T = j1.transpose()

# multiply arrays and take a root square -> size of an arrays
arrayMul = np.dot(j1, j1T)
arraySize1 = math.sqrt(arrayMul)
print("size of the 1st array:", arraySize1)

#transpose 2nd array
j2T = j2.transpose()
# print j2
#print (j2T)

#distance between 2 arrays
print("distance between arrays:")
arraySub = np.subtract(j2, j1)
print arraySub

print ("distance between transposed arrays:")
arraySub2 = np.subtract(j2T, j1T)
print arraySub2

# multiply distances and take a root square - > distance between 2 arrays:
arraysTrMul = np.dot(arraySub, arraySub2)
distance = math.sqrt(arraysTrMul)
print("distance between 2 arrays:", distance)

# % of changes -> distance / size
percChanges = distance / arraySize1 * 100
print(percChanges, "%")

# if pattern is changed more that 5% alert
if percChanges > 20:
    print("pattern changed more than 20%")
elif percChanges == 0:
	print("no changes")
else:
	print("less than 20%")
