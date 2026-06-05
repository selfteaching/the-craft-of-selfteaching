#文本文件保存到某个变量之中，经常需要对字符串进行操作
#str.splitlines()
#str.split()
#str.partition()
s = """Name,Age,Location
John,18,New York
Mike,22,San Francisco
Janny,25,Miami
Sunny,21,Shanghai"""
print(s)
print(s.splitlines())
#s.splitlines()返回的是一个列表（List），由被拆分的每一行作为其中的元素。
#str.split()根据分隔符拆分
r=s.splitlines()[2]#取出返回值2的那一行
print(r)
print(r.split())#默认使用None分割（各种空白，比如，\t 和 \r 都被当作 None）
print(r.split(sep=","))#使用","分割
print(r.split(","))#使用","分割，也可以省略sep
print(r.split(",",maxsplit=0))#拆分0次，即不拆分
print(r.split(",",maxsplit=-1))#全部拆分
