def say_hi(greetings,*names):
    for name in names:
        print(f'{greetings},{name.capitalize()}!')
say_hi('Hello','mike','john','jack')
