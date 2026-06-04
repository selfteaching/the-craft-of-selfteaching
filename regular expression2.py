
import re
with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\regex-target-text-sample.txt','r') as f:
    str=f.read()

pttn=r'go+gle'
a=re.findall(pttn,str)
print(a)
pttn=r'go{2,5}gle'
b=re.findall(pttn,str)
print(b)
pttn=r'colou?red'
c=re.findall(pttn,str)
print(c)
pttn=r'520*'
d=re.findall(pttn,str)
print(d)
