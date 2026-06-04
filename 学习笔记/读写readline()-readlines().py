f=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\readline读写文件test-file.txt','w')
f.write('first line\nsecond line\nthird line')
f.close()

f=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\readline读写文件test-file.txt','r')
s=f.readline()
print(s)
s=f.readline()
print(s)
f.close()
#使用str.strip()：\n被去掉了
f1=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\readline读写文件test-file.txt','w')
f1.write('first line\nsecond line\nthird line\n')
f1.close()

f1=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\readline读写文件test-file.txt','r')
s1=f1.readline().strip()
print(s1)
s1=f1.readline().strip()
print(s1)
s1=f1.readline().strip()
print(s1)
f1.close()

#使用readlines()读取文件中的每一行，并作为一个列表返回
f2=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\readlines读写文件test-file.txt','w')
f2.write('first line\nsecond line\nthird line\n')
f2.close()

f2=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\readlines读写文件test-file.txt','r')
s2=f2.readlines()
print(s2)
for index, line in enumerate(s2):
#直接使用enumerate获取列表的索引和值，同时在for后面定义接收的变量：
    print(f'第{index+1}行：\n 内容：{line}')
f2.close()
