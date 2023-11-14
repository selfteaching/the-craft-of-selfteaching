> - `random.randrange(1,1000)`表示随机产生一个1-1000的整数（含左侧1，但不含右侧1000）。
> - `for in range(10)`  将0-9依次遍历到i

案例1：打印出100以内的所有质数。

`
for i in range (2,100):
    if i == 2:
        print(i)
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)
   `
