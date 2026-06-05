import random
n=3
a_list=[random.randrange(65,91) for i in range(n)]
b_list=[chr(random.randrange(65,91)) for i in range(n)]
print(a_list)
c_list=a_list+b_list+a_list*2
print(c_list)

#appened()方法
c_list.append('100')
print(c_list)

#clear()方法
print(a_list)
a_list.clear()
print(a_list)

#copy()方法
d_list=c_list.copy()
print(d_list)
del d_list[6:8]
print(d_list)
print(c_list)

#.copy和赋值不同
e_list=d_list
del e_list[6:8]
print(e_list)   
print(d_list)   #对elist进行操作时，d_list也同步发生了变化
print(id(e_list) == id(d_list))  # 输出 True
# 证明e_list=d_list这里并非创建了一个列表，而是将两个列表指向了同一个内存地址，因此修改其中任何一个，两者会同时发生改变。

#在末尾追加一个列表
print(a_list)
print(c_list)
a_list.extend(c_list)
print(a_list)
#注意这里extend与append的差异：extend将列表中元素逐一添加到列表末尾，而append将c_list直接作为一整个子列表添加到目标列表末尾：[X,X,[A,B]]
#因此：append是将列表作为整体添加，extend是拆分列表，将其中元素逐一添加。

#在索引位置插入一个元素
print(a_list)
a_list.insert(1,'example')
print(a_list) #插入到索引位置，后续元素依次更新索引
a_list.insert(2,'exemple')
print(a_list)

# 报错：a_list.sort()，因为此时a_list中元素类型不统一

#排序
print(a_list)
a_list.reverse()
print(a_list)
# 注意reversereverse() 通过直接交换索引位置的元素完成反转，不触发任何比较操作。即使元素类型混杂，只要列表结构合法，反转就能正常执行。

x=a_list.reverse()
print(x)
#同时reverse()方法对当前序列进行操作，返回值为None，因此不能直接赋值给变量

