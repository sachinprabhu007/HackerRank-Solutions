import numpy as np 
n,m = map(int,input().split())
a = np.array([input().split() for _ in range(n)],dtype = int)
print(np.max(np.min(a,axis=1),axis=None))
