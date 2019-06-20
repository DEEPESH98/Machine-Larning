'''create 2D numpy  based array with given conditions:

i)   take input from user in terms of dimension like (3x2 or 6x7)
ii)   fill this numpy array with random number
iii)  store this array in a file
'''

import numpy as np

c=[]

a=int(input("Enter number of rows = "))
b=int(input("Enter number of columns =  "))

print("your {}x{} matrix = ".format(a,b))
#store in a list
c=(np.random.randint(2,size=(a,b)))

print(c)
