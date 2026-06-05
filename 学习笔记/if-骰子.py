import random
r=random.randrange(2,13)

if r==7:
    print('Draw')
elif r<11:
    print('Small')
elif r>7:
    print('Big!')

#模拟投飞了情况
e=random.randrange(0,13)

if e==7:
    print('Draw')
elif e>=2 and e<7:
    print('Small')
elif e>7:
    print('Big!')
else:
    print('投飞了')