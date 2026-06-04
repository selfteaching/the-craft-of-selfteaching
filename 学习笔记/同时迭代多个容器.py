#zip函数
chars='abcdefghijklmnopqrstuvwxyz'
nums=range(1,27)
#注意range左闭右开
for c,n in zip(chars,nums):
    print(f"Let's assume {c} represents {n}.")