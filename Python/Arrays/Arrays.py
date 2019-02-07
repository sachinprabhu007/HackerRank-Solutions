import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
   #revrser array first, convert to float array with numpy
   return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)