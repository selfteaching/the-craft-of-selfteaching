import os
with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\with test-file.txt','w') as f:
    f.write('first line\nsecond line\n third line\n')

with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\with test-file.txt','r') as f:
    for line in f.readlines():
        print(line)
file_name=r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\学习笔记\with test-file.txt'

if os.path.exists(file_name):
    os.remove(file_name)
    print(f'{file_name} deleted')
else:
    print(f'{file_name} does not exists')

# 用with语句块的另外一个好处就是不用写file.close()了
    
# with ... as ...