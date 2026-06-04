f=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\读写文件test-file.txt','w')
f.write('first line\nsecond line\nthird line')
f.close()

f=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\读写文件test-file.txt','r')
s=f.read()
print(s)
f.close()




