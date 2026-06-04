#向*Positional Arguments传递容器
def say_hi(*names):
    for name in names:
        print(f'Hi,{name}!')
def say_hi_1(**names):
    for key,values in names.items():
        print(f'Hi,{key}:{values}!')

names={"ann","jack","john"}
a_dictionary = {'ann': 2321, 'mike': 8712, 'joe': 7610}
say_hi(*names)
say_hi_1(**a_dictionary)