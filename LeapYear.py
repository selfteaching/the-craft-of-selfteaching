def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
        if year % 100 == 0:
            if year % 400 != 0:
                r = False
    return r

print(is_leap(4) is True)
print(is_leap(200) is True)
print(is_leap(220) is True)
print(is_leap(400) is True)
