for a in range(12):
    print(f'value of a:{a}')
#python中for循环的用法更直接，取代了其他语言中使用的计数器形式

#使用list的方式打印range循环的整数数列
print(list(range(10)))
#为range传递两个参数start，end
print(list(range(2,10)))
#step步长，每隔几个整数打印一次
for i in range(1,10,3):
    print(i)
#负数步长
print(list(range(0,-10,-1)))

