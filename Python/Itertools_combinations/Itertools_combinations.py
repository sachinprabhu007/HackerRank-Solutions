
from itertools import * 

if __name__ == '__main__':
    s,n = input().split()
    for i in range(1,int(n)+1):
        print('\n'.join(''.join(w) for w in list(combinations(sorted(s),i))))