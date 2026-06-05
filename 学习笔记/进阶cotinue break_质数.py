#写法一：print(n)属于语句块for i in range(2,n):
for n in range(2,100):
    if n==2:
        print(n)
        continue
    for i in range(2,n):
        if (n%i)==0:
            break
    print(n)
    #相当于只针对for-break的执行了一次print(n)
#写法二：print(n)不属于语句块for i in range(2,n):
for n in range(2,100):
    if n==2:
        print(n)
        continue
    for i in range(2,n):
        if (n%i)==0:
            break
        print(n) 
        #相当于针对每个i都执行了一次print(n)