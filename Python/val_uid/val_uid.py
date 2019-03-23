import re
x = re.compile(r'(?!.*(.).*\1)(?=.*\d.*\d.*\d)(?=.*[A-Z].*[A-Z])[A-Za-z0-9]{10}')

t = int(input())

for _ in range(t):
    uid = input()
    if x.match(uid):
        print('Valid')
    else:
        print('Invalid')


"""
regex being expensive
precompiled regex.

 negative lookahead for removing duplicates
 positive lookahead for both uppercase and number constraints.
 exact character class for checking length.
"""
