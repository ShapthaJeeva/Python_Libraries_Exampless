import numpy as np

# single-dimensional array
n1 = np.array([10, 20, 30, 40])
print(n1) 
print(type(n1)) 

# multi-dimensional array
n2 = np.array([[10,20,30,40],[40,30,20,10]])
print(n2)

# initializing numpy array with zeros
n3 = np.zeros((5,5))
print(n3)

# initializing numpy array with same number
n4 = np.full((2,2),9)
print(n4)

# initializing numpy array within a range
n5 = np.arange(10,20)
print(n5)

n6 = np.arange(10,50,5)
print(n6)

# initializing numpy array with random numbers
n7 = np.random.randint(1,100,5)
print(n7)

# checking te shape of an array
print(n2.shape)
n2.shape = (4,2)
print(n2.shape)
print(n2)

n8 = np.array([10,20,30])
n9 = np.array([40,50,60])

print(np.vstack((n8,n9)))  # vstack()
print(np.hstack((n8,n9)))  # hstack()
print(np.column_stack((n8,n9)))  # column_stack()

N1 = np.array([10,20,30,40,50,60])
N2 = np.array([50,60,70,80,90])

print(np.intersect1d(N1,N2))  # intersection
print(np.setdiff1d(N1,N2))    # difference
print(np.setdiff1d(N2,N1))

# Addition
N3 = np.array([10,20])
N4 = np.array([30,40])

print(np.sum([N3,N4]))
print(np.sum([N3,N4],axis=0))
print(np.sum([N3,N4],axis=1))

nn1 = np.array([10,20,30])
nn1 = nn1+1
print(nn1)

nn2 = np.array([10,20,30])
nn2 = nn2*2
print(nn2)

nn3 = np.array([10,20,30])
nn3 = nn3-1
print(nn3)

nn4 = np.array([10,20,30])
nn4 = nn4/2
print(nn4)

nn5 = np.array([10,20,30,40,50,60])
print(np.mean(nn5))    # Mean
print(np.std(nn5))     # Standard deviation
print(np.median(nn5))  # Median

# Matrix
nn6 = np.array([[1,2,3],[4,5,6],[7,8,9]])
nn7 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(nn6)
print(nn6[0])
print(nn6[:,1])
print(nn6[1,2])

# Transpose
print(nn6.transpose())

# Matrix Multiplication
print(nn6.dot(nn7))
print(nn7.dot(nn6))

nn8 = np.array([10,20,30,40,50,60])
np.save('my_numpy',nn8)               # Saving NumPy array

nn9 = np.load('my_numpy.npy')         # Loading NumPy array
print(nn9)