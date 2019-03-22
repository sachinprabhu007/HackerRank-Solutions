

import re
pattern = r'#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3}'
for i in range(int(input())):
    match = re.findall(pattern, input()[1:])
    if match:
        print('\n'.join(match))