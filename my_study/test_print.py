import sys
import os

name = "Ann"
age = 22
print(f'{name} is {age} years old')

print('hello', 'world')
print('hello', 'world', sep=' ', end='\n')
print('hello', 'world', sep='~', end='\n')

f = open('./test.txt', 'w+')
print('hello', 'world', sep='~', end='\n', file=f, flush=False)
f.close()
