import re 
rep_char = re.search(r'([a-zA-Z0-9]+)\1+',input())
print(rep_char.group(1) if rep_char else -1)

