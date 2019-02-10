import numpy as np
m,n,p = map(int,input().split())
print(np.array([input().split() for _ in range(m+n)],int))
