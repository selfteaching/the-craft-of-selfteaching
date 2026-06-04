name='John'
age=23
print('{} is {} years old.'.format(name,age))
#不写占位符索引的情况下，默认占位符从0开始，即0，1，2，3...（占位符数量-1）
# 即'{}{}'.format(a,b)和'{0}{1}'.format(a,b)是一样的。

#'{0} is {2} years old.'.format(name,age)会报错，因为占位符索引超出了占位符数量。

#str.format()里可以直接写表达式...
print('{} is a grown up? {} '.format(name,age>=18))

#f-string
name='Jack'
age=25
print(f'{name} is {age} years old')
print(f'{name} is a grown up? {age>=18}')