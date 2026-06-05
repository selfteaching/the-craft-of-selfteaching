#str.find(sub[,start[,end]])
print("example str.find():")
s="""Simple is better than complex.
Complex is better than complicated."""
print(s.lower().find('mpl'))
print(s.lower().find('mpl',10))
print(s.lower().find('mpl',10,20))
# 没有找到就返回-1

print("example str.rfind():")
#str.rfind(sub[,start[,end]])
#返回最后sub出现的位置，find是最早出现的位置
print(s.lower().rfind('mpl'))
print(s.lower().rfind('mpl',10))
print(s.lower().rfind('mpl',10,20))

print('Example str.index():')
#str.index(sub[,start[,end]])
#作用与find相同，如果没找到，就触发ValueError异常
print(s.lower().index('mpl'))
print(s.lower().index('mpl',10))
#str.rindex(sub[,start[,end]])
#作用与rfind相同，如果没找到，就触发ValueError异常
print(s.lower().rindex('mpl'))
