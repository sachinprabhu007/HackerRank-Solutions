import numpy as np 
n,m = map(int,input().split())
a = np.array([input().split() for _ in range(n)],dtype = int)
print(np.prod(np.sum(a,axis=0),axis=0))
