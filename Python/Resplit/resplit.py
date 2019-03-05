regex_pattern = r""	# Do not delete 'r'.
import re
print(*filter(None, re.split(r'[.,]+', input())), sep='\n')