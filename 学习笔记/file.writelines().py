#把列表写入到文件中
a_list=['first line test content\n','second line test content\n','third line test content\n']
f=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\writelines-test-file.txt','w')
f.writelines(a_list)
f.close()

f=open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\writelines-test-file.txt','r')
for line in f.readlines():
    print(line)
f.close()
