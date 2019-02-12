import numpy as np 
np.set_printoptions(sign=' ')
print(np.eye(*map(int, input().split())))

"""It 'unpacks' the elements in the list returned 
from [ int(x) for x in input().split() ]"""


