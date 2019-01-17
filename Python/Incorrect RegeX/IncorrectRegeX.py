import re 
n = int(input())
for i in range(n):
    m = input()
    try:
        re.compile(m)
        print('True')
    except:
        print('False')