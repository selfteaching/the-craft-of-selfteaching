import os
f=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\删除文件test-file.txt','w')
print(f.name)
f.close()#关闭文件，否则无法删除文件
if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted')
else:
    print(f'{f.name} does not exist')
