def say_hi(**names_greetings):
    for name,greetings in names_greetings.items():
        print(f'{name},{greetings}')
say_hi(mike='hello',ann='my daring',john='Hi')

#直接使用字典的迭代方式：分别定义变量来接收key-value
def say_hi1(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')
        
a_dictionary = {'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'}
say_hi1(**a_dictionary)

say_hi1(**{'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'})

#在函数内部，选择不同的方式去迭代字典：循环时直接保存key-value到变量，再索引取出
def say_hi_2(**names_greetings):
    for name in names_greetings:
        print(f'{names_greetings[name]}, {name}!')
say_hi_2(mike='Hello', ann='Oh, my darling', john='Hi')
