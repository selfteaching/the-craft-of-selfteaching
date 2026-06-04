def say_hi(greetings,*names,capitalized=False):
    for name in names:
        if capitalized:
            name=name.capitalize()
        print(f'{greetings},{name}!')
say_hi('Hello','mike','john','zeo')    
say_hi('Hello','mike','john','zeo',capitalized=True)