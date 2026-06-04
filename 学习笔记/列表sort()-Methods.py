import random
n=10
a_list=[random.randrange(1,100) for i in range(n)]
print(f'a_list comprehends {len(a_list)} random numbers:\n',a_list)

a_list.sort()
print('the list sorted:\n',a_list)
#sort()函数默认升序排列
#降序排列，修改参数reverse=True
a_list.sort(reverse=True)
print('the list sorted reversely:\n',a_list)

#对列表内部的字符串元素也可以进行排序
c_list=[chr(random.randrange(65,91)) for i in range(n)]
print(f'c_list comprehends {len(c_list)} random letters:\n',c_list)

c_list.sort()
print('the list sorted:\n',c_list)

c_list.sort(reverse=True)
print('the list sorted reversely:\n',c_list)

print(c_list)

d_list=[chr(random.randrange(65,91))+\
        chr(random.randrange(97,123))\
              for i in range(n)]
#在代码行末加上\，表示换行

print(f'd_list comprehends {len(d_list)} random letters:\n',d_list)

d_list.sort()
print('the list sorted:\n',d_list)

d_list.sort(key=str.lower,reverse=True)
print('the list sorted reversely:\n',d_list)
