cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    x, y = 0, 1 
    for i in range(n):
        yield x
        x,y = y, x+y

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))