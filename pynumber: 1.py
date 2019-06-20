import numpy as np

c=[]

a=int(input("Enter number of rows = "))
b=int(input("Enter number of columns =  "))

print("your {}x{} matrix = ".format(a,b))
#store in a list
c=(np.random.randint(2,size=(a,b)))

print(c)
