'''create a numpy array of  8x2 as having number  in each cell between 
100 and 200 such that difference between each element is 5'''  


import numpy as np

#Enter value,range and difference
a1=np.arange(100,200,5)
#Reshape your array
arr=a1[0:16].reshape(8,2)

print(arr)
