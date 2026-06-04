
import re
with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\regex-target-text-sample.txt','r') as f:
    str=f.read()
pttn=r'beg[iau]ns?'
s=re.findall(pttn,str)
print(s)

