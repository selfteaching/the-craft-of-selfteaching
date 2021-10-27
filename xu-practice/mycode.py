# %load mycode.py
# 当前这个 Code Cell 中的代码，保存在当前文件夹中的 mycode.py 文件中
# 以下的代码，是使用 Jupyter 命令 %load mycode.py 导入到当前 Code Cell 中的：

def is_prime(n):
    """
    Return a boolean value based upon
    whether the argument n is a prime number.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

def say_hi(*names, greeting='Hello', capitalized=False):
    """
    Print a string, with a greeting to everyone.
    :param *names: tuple of names to be greeted.
    :param greeting: 'Hello' as default.
    :param capitalized: Whether name should be converted to capitalzed before print. False as default.
    :returns: None
    """
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')