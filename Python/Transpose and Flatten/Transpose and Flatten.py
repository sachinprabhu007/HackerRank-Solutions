import numpy as np 
my_array  = np.array([input().split() for _ in range(int(input().split()[0]))],int)
print(my_array.transpose())
print(my_array.flatten())