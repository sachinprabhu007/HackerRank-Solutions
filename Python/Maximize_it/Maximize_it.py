K,M = map(int,input().split())
print (sum([max(list(map(int,input().strip().split()[1:])))**2 for _ in range(K)])%M)

