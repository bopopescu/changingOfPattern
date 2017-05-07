import math
import numpy as np


j1 = np.array([0.16772720217704773, 0.10754672437906265, 0.09320881217718124, 0.08764657378196716, 0.07854834944009781, 0.06587719172239304, 0.046421799808740616, 0.039439789950847626, 0.03939548134803772, 0.03825334459543228])
j2 = np.array([0.09233524650335312, 0.06628251820802689, 0.05964335799217224, 0.04267887398600578, 0.023968420922756195, 0.023834727704524994, 0.02015206776559353, 0.07860107719898224, 0.05157581344246864, 0.04732499644160271])
# j1M = np.matrix(j1).reshape(0, 10)
# print j1M

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
if percChanges > 0.05:
    print("pattern changed!")
