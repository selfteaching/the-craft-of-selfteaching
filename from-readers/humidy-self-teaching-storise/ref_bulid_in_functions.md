# 字符串函数收集

&emsp;&emsp;写这个文档思路来自李笑来《自学是一门手艺》函数这一章

&emsp;&emsp;这里收集了这一章涉及的函数，这些都是python的标准内部函数，用于处理字符串，作为读书学习的一个总结.

&emsp;&emsp;为什么选择的是字符串函数，我个人觉得是简单、标准、通用和完整。引用书中的描述：
>&emsp;&emsp;在任何一本编程书籍中，关于字符串的内容总是很长，就好像每本英语语法书中，关于动词的内容总是占全部内容的至少三分之二。
> 这也没什么办法，因为程序的主要功能就是完成人机交互，人们所用的就是字符串而不是二进制数字。

&emsp;&emsp;收集的函数列表如下，添加了例子和注释,方便查阅:
```python
ord(str) #获取一个字符串的Unicode码
chr(int) #获取一个Unicode码对应的字符
len(str) #获取字符串的长度
str.lower(str) #将字符串转换为小写
str.upper(str) #将字符串转换为大写
str.swapcase(str) #将字符串中的大写字母转化为小写,小写字母转化为大写（交换字符串中的大小写）
str.isupper(str) #判断字符串是否是大写

# 特别注意islower和casefold的区别
str.islower(str) #判断字符串是否是小写
str.casefold(str) #将字符串中的大写字符转换为小写字符
# 和lower()的区别，casefold()的方法可以将所有大写(包括非中英语的其他语言)转换为小写

str.title(str) # 字符串的每个单词的首字母大写,其他小写
str.capitalize(str) #将字符串的第一个单词的首字母大写,其他小写
str.count(sub[, start[, end]]) #统计字符串中子字符串的个数
str.find(sub[, start[, end]]) #从字符串中查找子字符串的起始位置
str.rfind(sub[, start[, end]]) #从字符串中查找子字符串的最后一个位置
str.index(sub[, start[, end]]) #从字符串中查找子字符串的起始位置,并返回该位置
str.startswith(prefix[, start[, end]]) #判断字符串是否以指定的前缀开头
str.endswith(suffix[, start[, end]]) #判断字符串是否以指定的后缀结尾
str.replace(old[, new[, count]]) #用新的字符串替换字符串中的子字符串
str.expandtabs(tabsize) #将字符串中的tab字符用指定大小的空格替换
str.strip(chars) #去除字符串两边的字符（默认空白字符）
str.splitliness(keepends) #按照字符串中的换行符进行分割，形成新的列表
str.split(sep[, maxsplit]) #按照指定的分隔符分割字符串
str.join(seq)  #将一个序列中的元素用指定的分隔符连接起来
str.center(width[, fillchar]) #将字符串居中,并用指定的字符填充
str.ljuststr.ljust(width[, fillchar]) #将字符串左对齐,并用指定的字符填充
str.rjust(width[, fillchar]) #将字符串右对齐,并用指定的字符填充
str.isalnum(str) #判断字符串是否是由字母或数字组成
str.isalpha(str) #判断字符串是否是由字母组成

# 特别注意isdecimal和isdigit、isnumeric的区别,详见ref_build_in_functions.py
str.isdecimal(str) #判断字符串是否是由decimal组成
# 包括Unicode数字、双字节全角数字，不包括罗马数字、汉字数字、小数
str.isdigit(str) #判断字符串是否是由digit组成
# 包括Unicode数字、单字节数字、双字节全角数字，不包括罗马数字、汉字数字、小数
str.isnumeric(str) #判断字符串是否是由numeric组成
# 包括Unicode数字、双字节全角数字、罗马数字、汉字数字，不包括小数

str.isspace(str) #判断字符串是否是由空白字符组成
str.isidentifier(str) #判断字符串是否是合法的标识符(不会剔除关键字)
str.isprintable(str) #判断字符串是否是由printable组成
```
&emsp;&emsp;总结：列举出这些函数，自己最大的收获是发现这里面有些函数是演进的关系，用于同一个目的，
或实现同一个功能，会存在多个不同的函数，好奇心让我去探究了一下这些函数的区别，想不到，
这个收集过程中的副产品，反而成为我梳理过程中最大的收获，有时候*抠抠细节*会成为学习中的点睛之笔。