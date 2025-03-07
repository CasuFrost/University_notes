import numpy as np
#set seed for random generator 
np.random.seed(0)

x1 = np.random.randint(10, size=6) #array of 6 element from 0 to 10
x2 = np.random.randint(10, size = (3,4)) #multidimensional array specified as a tuple
x3 = np.random.randint(10, size = (3,4,5))

#Let's see how to access to the numpy-array's properties

print(f'the dimension of x3 is {x3.ndim}') #access number of array's dimension with parameter 'nteam'

print(f'the total number of elements in x3 is {x3.size}') #with 'size' we have the total number of elements inside the array

#Accessing the array element
print(x1[3])
print(x2[1,2])
print(x3[1,3,2])


#slicing arrays 
x4 = x1[3:6]
print(x4)
