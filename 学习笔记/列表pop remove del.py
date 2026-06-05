import random
n=3
a_list=[random.randrange(65,91) for i in range(n)]
print(a_list)

#插入
a_list.insert(1,'example')
print(a_list)

#删除
#remove去除example，如果有多个，只去除第一个
a_list.remove('example')
print(a_list)

#pop删除并返回被删除的值
p=a_list.pop(2)
print(a_list)
print(p)

#pop del 和remove的区别
a_list.insert(2,'example')
a_list.insert(2,'example')
a_list.insert(2,'example')
print(a_list)
del a_list[2]
print(a_list) 

print(a_list.remove('example'))# 返回None
print(a_list)

#del直接删除了数列中元素，pop删除并返回被删除的值，remove删除第一个元素，并返回None

