
import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<='+s+')([aeiou]{2,})'+ s, input(), re.I)
print('\n'.join(a or ['-1']))

# re.I in the last - case insesitive 
# <= - lookbehind assertion 
#it check if argument is true but does not consume it. In our case it checks whether there is consonant before vowels but does not count it into string -> that is why we print ee and not dee