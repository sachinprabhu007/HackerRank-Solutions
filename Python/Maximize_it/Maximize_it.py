#K,M = map(int,input().split())
#print (sum([max(list(map(int,input().strip().split()[1:])))**2 for _ in range(K)])%M)

import itertools

k, m = map(int, input().split())

print(max(sum(j) % m for j in itertools.product(*((int(i) ** 2 for i in input().split()[1:]) for _ in range(k)))))
