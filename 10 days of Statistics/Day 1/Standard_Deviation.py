# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
X = [int(x) for x in input().strip().split()]

mean = sum(X)/n 
varience = sum(((x-mean) ** 2) for x in X) / n
stddev = varience ** 0.5

print('{0:0.1f}'.format(stddev))
