import random
n=3
a_list=[random.randrange(65,91) for i in range(n)]
b_list=[chr(random.randrange(65,91)) for i in range(n)]
print(a_list)
print(b_list)
c_list=a_list+b_list+a_list*2
print(c_list)

print()
#根据索引提取（Slicing）
print(c_list[3])    #返回索引值为3的元素值
print(c_list[:])    #返回整个列表
print(c_list[5:])   #返回从索引为5开始到列表末尾的所有元素
print(c_list[:3])   #返回从列表开头到索引为3的所有元素
print(c_list[2:6])  #从索引2开始，直到索引6之前（不包括6）

print(c_list)
#根据索引删除
del c_list[3] #del是一个命令
print(c_list)
del c_list[5:8] #删除最新的c_list列表对应的[5,8)
print(c_list)  
#根据索引替换
c_list[1:5:2]=['a',2]   #索引1开始，5结束，2step替换一次，依次替换['a',2]
print(c_list)
