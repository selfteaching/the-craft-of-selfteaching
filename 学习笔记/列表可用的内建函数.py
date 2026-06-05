import random
n=3
#生成3个随机数
a_list=[random.randrange(65,91) for i in range(n)]
b_list=[chr(random.randrange(65,91)) for i in range(n)]
print(a_list)
print(b_list)
#操作列表
c_list=a_list+b_list+a_list*2
print(c_list)

#内建函数操作len()、max()、min()、sum()
print(len(c_list))
print(max(b_list))
print(min(b_list))
# 根据Unicode码比较
print('X' not in b_list)