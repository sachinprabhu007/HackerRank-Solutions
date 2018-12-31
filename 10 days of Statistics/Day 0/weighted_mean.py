n=int(input())
x = list(map(float,input().split()))
w = list(map(float,input().split()))
y=0
for i in range(n):
    y=y+x[i]*w[i]
print('{:.1f}'.format(y/sum(w)))