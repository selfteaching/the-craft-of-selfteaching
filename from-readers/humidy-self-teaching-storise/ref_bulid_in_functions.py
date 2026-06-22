# -*- coding:utf-8 -*-
"""
程序思路来自李笑来《自学是一门手艺》函数这一章
这里收集了这一章涉及的函数，这些都是python的标准内部函数，用于处理字符串，作为一个总结
"""
# @humidy-2023-7
# 收集书籍中涉及的相关函数集
# 添加可以运行的实例
# 代码通过pylint检测

if __name__ == '__main__':
    print("In: ord('c')")
    # ord( {需要转换的字符} )，返回值是对应的Unicode编码,这个函数只能接收单个字符作为参数
    # [官方注解]：Return the Unicode code point for a one-character string.
    test_char = 'c'
    print("Out: {}".format(ord(test_char)))

    # 为显示好看这里加了一行换行
    print()
    print("In: chr(65)")
    # chr( {需要转换的Unicode编码} ),返回值是对应的字符,这个函数只能接收一个Unicode编码作为参数
    # [官方注解]: Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
    test_code = 65
    print("Out: {}".format(chr(test_code)))

    # 为显示好看这里加了一行换行
    print()
    print("In: len('abc')")
    # len( {需要转换的字符串} ),返回值是对应的字符串的长度,这个函数只能接收一个字符串作为参数
    # [官方注解]:Return the number of items in a container.
    length = len('abcdefg')
    print("Out: {}".format(length))

    # 为显示好看这里加了一行换行
    print()
    print("In: upper('abc')")
    # upper( {需要转换的字符串} ),返回值是对应的字符串的大写形式,这个函数只能接收一个字符串作为参数
    # [官方注解]:Return a copy of the string converted to uppercase.
    upper_str = str.upper('abc')
    print("Out: {}".format(upper_str))

    # 为显示好看这里加了一行换行
    print()
    print("In: lower('ABC')")
    # lower( {需要转换的字符串} ),返回值是对应的字符串的小写形式,这个函数只能接收一个字符串作为参数
    # [官方注解]:Return a copy of the string converted to lowercase.
    lower_str = str.lower('ABC')
    print("Out: {}".format(lower_str))

    # 为显示好看这里加了一行换行
    print()
    print("In: swapcase('ABcDEfGH')")
    # swapcase( {需要转换的字符串} ),返回值是对应的字符串的大小写互换形式,这个函数只能接收一个字符串作为参数
    # [官方注解]:Convert uppercase characters to lowercase and lowercase characters to uppercase.
    swap_str = str.swapcase('ABcDEfGH')
    print("Out: {}".format(swap_str))

    # 为显示好看这里加了一行换行
    print()
    print("In: casefold('ABcDEfGH')")
    # casefold( {需要转换的字符串} ),返回值是可以将字符串中的大写字符转换为小写字符。效果和lower()相似
    # [官方注解]:Return a version of the string suitable for caseless comparisons.
    # 和lower()的区别，casefold()的方法可以将所有大写(包括非中英语的其他语言)转换为小写
    case_fold_str = str.casefold('ABcDEfGH')
    print("Out: {}".format(case_fold_str))

    # 为显示好看这里加了一行换行
    print()
    print("In: title('the captain geogre')")
    # title( {需要转换的字符串} ),返回值是对应的字符串的每个单词的首字母大写,其他小写.
    # [官方注解]:Return a version of the string where each word is titlecased.
    title_str = str.title('THE captain geogre')
    print("Out: {}".format(title_str))

    # 为显示好看这里加了一行换行
    print()
    print("In: capitlize('the captain geogre')")
    # capitlize( {需要转换的字符串} ),返回值是对应的字符串的首字母大写,其他小写.
    # [官方注解]:Return a version of the string where each word is capitalized.
    cap_str = str.capitalize('the captain geogre')
    print("Out: {}".format(cap_str))

    # 为显示好看这里加了一行换行
    print()
    print("In: count(\"She is a beautiful girl\",'e',1)")
    # count() 方法用于统计字符串里某个字符或子字符串出现的次数。可选参数为在字符串搜索的开始与结束位置。
    # [官方注解]:S.count(sub[, start[, end]]) -> int
    count_str = "She is a beautiful girl"
    count_res = str.count(count_str, 'e', 1)
    print("Out: {}".format(count_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: find(\"She is a beautiful girl\",'she')")
    # find() 方法检测字符串中是否包含子字符串,如果包含子字符串返回开始的索引值，否则返回-1
    # [官方注解]:S.find(sub[, start[, end]]) -> int
    find_str = "she is a beautiful girl, she is cue"
    find_res = str.find(find_str, 'she')
    print("Out: {}".format(find_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: rfind(\"she is a beautiful girl, she is cue\",'she')")
    # rfind() 方法检测字符串中是否包含子字符串,返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。
    # [官方注解]:S.rfind(sub[, start[, end]]) -> int
    # 注意和find()的区别，一个是开始，一个是最后
    rfind_str = "she is a beautiful girl, she is cue"
    rfind_res = str.rfind(find_str, 'she')
    print("Out: {}".format(rfind_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: index(\"She is a beautiful girl\",'she')")
    # index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内
    # 该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常
    # [官方注解]:S.index(sub[, start[, end]]) -> int
    # 注意和find()的区别，一个是找不到不报错，index()是找不到报错
    index_str = "she is a beautiful girl, she is cue"
    index_res = str.index(index_str, 'she')
    print("Out: {}".format(index_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: startswith(\"google is a popular search engine\",'google')")
    # startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False
    # [官方注解]:S.startswith(prefix[, start[, end]]) -> bool
    start_with_str = "google is a popular search engine"
    start_with_res = str.startswith(start_with_str, 'google')
    print("Out: {}".format(start_with_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: endswith(\"google is a popular search engine\",'engine')")
    # startswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False
    # [官方注解]:S.endswith(suffix[, start[, end]]) -> bool
    start_with_str = "google is a popular search engine"
    start_with_res = str.endswith(start_with_str, 'engine')
    print("Out: {}".format(start_with_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: replace(\"google is a popular search engine\",'popular','famous')")
    # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
    # [官方注解]:Return a copy with all occurrences of substring old replaced by new.
    replace_str = "google is a popular search engine"
    replace_res = str.replace(replace_str, 'popular', 'famous')
    print("Out: {}".format(replace_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: expandtabs(tabsize=8)")
    # expandtabs() 方法把字符串中的 tab 符号 \t 转为空格，tab 符号 \t 默认的空格数是 8
    # [官方注解]:Return a copy where all tab characters are expanded using spaces.
    expand_str = "runoob\t12345\tabc"
    expand_res = str.expandtabs(expand_str, tabsize=16)
    print("Out: {}".format(expand_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: strip('a')")
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    # [官方注解]:Return a copy of the string with leading and trailing whitespace removed.
    strip_str = "  runooba  "
    strip_res = str.strip(strip_str, 'a')
    print("Out: {}".format(strip_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"runoob\\n12345\\nabc\".splitlines()")
    # splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表。
    # [官方注解]:Return a list of the lines in the string, breaking at line boundaries.
    split_line_str = "runoob\n12345\nabc"
    split_line_res = str.splitlines(split_line_str)
    print("Out: {}".format(split_line_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"runoob12345abc\".split()")
    # split() 通过指定分隔符对字符串进行切片
    # [官方注解]:Return a list of the words in the string, using sep as the delimiter string.
    split_str = "runoob12345abc"
    split_res = str.split(split_str, 'o')
    print("Out: {}".format(split_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: '|'.join(['hello', 'world','hello','Hangzhou'])")
    # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
    # [官方注解]: Concatenate any number of strings.
    join_list = ['hello', 'world', 'hello', 'Hangzhou']
    join_res = str.join('|', join_list)
    print("Out: {}".format(join_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"runoob\".center(20,'*')")
    # center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。
    # [官方注解]:Return a centered string of length width.
    # Padding is done using the specified fill character
    center_str = "runoob"
    center_res = str.center(center_str, 20, '*')
    print("Out: {}".format(center_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"runoob\".ljust(20,'*')")
    # ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
    # [官方注解]: Return a left-justified string of length width.
    # Padding is done using the specified fill character (default is a space).
    left_just_str = "runoob"
    left_just_res = str.ljust(left_just_str, 20, '*')
    print("Out: {}".format(left_just_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"runoob\".rjust(20,'*')")
    # rjust() 方法返回一个原字符串右对齐,并使用空格填充至指定长度的新字符串。
    # [官方注解]:Return a right-justified string of length width.
    # Padding is done using the specified fill character (default is a space).
    right_just_str = "runoob"
    right_just_res = str.rjust(right_just_str, 20, '*')
    print("Out: {}".format(right_just_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"runoob\".zfill(20)")
    # zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
    # [官方注解]:Pad a numeric string with zeros on the left, to fill a field of the given width.
    # The string is never truncated.
    zfill_str = "runoob"
    zfill_res = str.zfill(zfill_str, 20)
    print("Out: {}".format(zfill_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"ak12345\".isalnum()")
    # isalnum() 方法检测字符串是否由字母和数字组成
    # [官方注解]:Return True if the string is an alpha-numeric string, False otherwise
    alpha_num_str = "ak12345"
    alpha_num_res = str.isalnum(alpha_num_str)
    print("Out: {}".format(alpha_num_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"dolphin\".isalpha()")
    # isalpha() 方法检测字符串是否由字母组成
    # [官方注解]:Return True if the string is an alphabetic string, False otherwise.
    alpha_str = "dolphin"
    alpha_res = str.isalpha(alpha_str)
    print("Out: {}".format(alpha_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"12345.6789\".isdecimal()")
    # isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象,python3中字符串均为unicode编码
    # 包括Unicode数字、双字节全角数字，不包括罗马数字、汉字数字、小数
    # [官方注解]:Return True if the string is a decimal string, False otherwise.
    decimal_str = "12345.6789"
    decimal_res = str.isdecimal(decimal_str)
    print("Out: {}".format(decimal_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"123456789\".isdigit()")
    # isdigit() 方法检测字符串是否只由数字组成，只对 0 和 正数有效
    # 包括Unicode数字、单字节数字、双字节全角数字，不包括罗马数字、汉字数字、小数
    # Return True if the string is a digit string, False otherwise.
    digit_str = "123456789"
    digit_res = str.isdigit(digit_str)
    print("Out: {}".format(digit_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"壹贰叁\".isnumeric()")
    # isnumeric() 是否所有字符均为数值字符
    # 包括Unicode数字、双字节全角数字、罗马数字、汉字数字，不包括小数
    # [官方注解]:Return True if the string is a numeric string, False otherwise.
    number_str = "壹贰叁"
    number_res = str.isnumeric(number_str)
    print("Out: {}".format(number_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"   \".isspace()")
    # isspace() 方法检测字符串是否只由空格组成
    # [官方注解]:Return True if the string is a whitespace string, False otherwise.
    space_str = "   "
    space_res = str.isspace(space_str)
    print("Out: {}".format(space_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"for\".isidentifier()")
    # isidentifier() 方法检测字符串是否符合标识符的规则,是否是Python合法的标识符
    # [官方注解]:Return True if the string is a valid Python identifier, False otherwise.
    # 这个函数没有对关键词进行判断
    identifier_str = "for"
    identifier_res = str.isidentifier(identifier_str)
    print("Out: {}".format(identifier_res))

    # 为显示好看这里加了一行换行
    print()
    print("In: \"what is your name?\".isprintable()")
    # isprintable() 方法检测字符串是否只由可打印字符组成
    # [官方注解]:Return True if the string is a printable string, False otherwise.
    printable_str = "what is your name?"
    printable_res = str.isprintable(printable_str)
    print("Out: {}".format(printable_res))
