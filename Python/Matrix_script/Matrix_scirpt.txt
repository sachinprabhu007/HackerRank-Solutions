import re

N, M = map(int, input().split(' '))
m1 = []

for i in range(N):
    m1.append(input())

s = zip(*m1)
s = "".join(["".join(i) for i in s])

s = re.sub(r'(\w)[^\w]+(\w)', r'\1 \2', s)
print(s)



