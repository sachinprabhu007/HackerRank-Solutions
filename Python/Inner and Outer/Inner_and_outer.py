import numpy as np

a = np.array(input().split() ,int)
b = np.array(input().split() ,int)
print(np.inner(a,b))
print(np.outer(a,b))


#A,B = [np.array([input().split()],int) for _ in range(2)]
#print(np.inner(A,B)[0][0],np.outer(A,B),sep="\n")

