#ord()函数，直接使用字母的ASCII进行计算
print(f"a的ASCII码：{ord('a')}")
#a--97,即对应到1为ord('a')-96
#以knowledge为例：
word='knowledge'
sum=0
for char in word:
    sum+=ord(char)-96
print(f'knowledge的ASCII:{sum}')
#把以上计算过程打包为一个函数
def sum_of_word(word):
    sum=0
    for char in word:
        sum+=ord(char)-96
    # print(f"{word}对应的ASCII：{sum}")
    return sum
sum_of_word('attitude')
sum_of_word('hello')
#导入下载的字典，把字典的内容遍历，同时对字典的内容进行函数调用：
# with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\words_alpha.txt','r') as file:
#     for word in file.readlines():#遍历读取文件的返回列表
#         if sum_of_word(word)==100:
#             print(word)
#查找问题：打印出第一个单词的每个字母，定位问题：
# with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\words_alpha.txt','r') as file:
#     for word in file.readlines():#遍历读取文件的返回列表
#         if sum_of_word(word)==100:
#             print(word)
#             for c in word:
#                 print(c,ord(c)-96)
#             break
#如果使用list(word)打印结果则更为直观：'a', 'b', 's', 't', 'r', 'u', 's', 'e', 'n', 'e', 's', 's', 'e', 's', '\n'
#验证\n的ASCII：
# print(ord('\n')-96)
with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\results_test file.txt','w') as results:
    with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\words_alpha.txt','r') as file:
      for word in file.readlines():#遍历读取文件的返回列表
        #str.strip()删除字符串前后的空白字符
        if sum_of_word(word.strip())==100:
            # print(word)
            results.write(word)
with open(r'\Users\Administrator\Documents\GitHub\the-craft-of-selfteaching\words_alpha.txt','r') as file:
    lines=file.readlines()
    #repr显示原始字符
    first_line=lines[0]
    first_line_o=repr(lines[0])
    first_line1=lines[0].strip()
    print(f"readlines读取的第一个元素：{first_line}")
    print(f"readlines读取的第一个元素_原始数据：{first_line_o}")
    print(f"使用strip后:{first_line1}")
    #验证换行符的存在，查看字符串长度：
    print(len(first_line))
    print([ord(c) for c in first_line])

    