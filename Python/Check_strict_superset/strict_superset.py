a=set(map(int,input().split()))
n=input()
flag=0
for i in range(n):
    b=set(map(int, input().split()))
    if len(b.difference(a))!=0: 
        flag=1
    else:
        if len(b)==len(a):
            flag=1
if flag==0:
    print "True"
else:
    print "False"