<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: دربارهٔ parameterها و argumentها (بخش اول)](Part.2.D.1-args.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: نام دیگر و function بی‌نام](Part.2.D.3-lambda.md)

</div>

<!-- reading-navigation:end -->


# دربارهٔ parameterها و argumentها (بخش دوم)

## positional parameter برای دریافت چند مقدار

اگر هنگام تعریف، پیش از یک *positional parameter* علامت ستاره، یعنی `*`، بگذارید، آن parameter می‌تواند چند مقدار دریافت کند. سپس درون function می‌توانید این مقدارها را با loopِ `for ... in ...` یکی‌یکی پردازش کنید.

نام انگلیسی این حالتِ تک‌ستاره‌ای «Arbitrary Positional Arguments» است؛ فعلاً منظور از آن argumentهای positional با تعداد دلخواه است.

حالتِ دوستاره‌ای هم داریم که کمی بعد به آن می‌رسیم. نام انگلیسی آن «Arbitrary Keyword Arguments» است؛ یعنی argumentهای keyword با تعداد دلخواه.

> بعضی کتاب‌های چینی، «Arbitrary Positional Arguments» را چیزی شبیه «argumentهای positional متغیر» ترجمه کرده‌اند. در واقع، در چنین جاهایی هر ترجمهٔ چینی می‌تواند فهم مطلب را دشوار کند. این یکی هنوز بد نیست؛ حتی دیده‌ام «Arbitrary Keyword Arguments» را با تعبیری شبیه «argumentهای keyword خودسرانه» ترجمه کرده‌اند! به نظرم چنین ترجمه‌ای حتماً ابهامی در ذهن خواننده ایجاد می‌کند که توضیح دادنش هم آسان نیست.
>
> بنابراین، **پس از گذر از مرحلهٔ مقدماتی، تا جای ممکن فقط از انگلیسی استفاده کردن** راهبرد خوبی است. شاید اوایل کمی دشوار باشد، اما بعداً خیال شما را راحت‌تر می‌کند و عمرتان را طولانی‌تر! بله، زمان و زندگی کمتری را هدر دادن، در واقع مثل این است که عمر بیشتری داشته باشید!

> **یادداشت مترجم — توضیح تکمیلی:** positional argument بر اساس جایگاهش در فراخوانی به parameter مربوط متصل می‌شود؛ keyword argument با نام مشخص می‌شود. در تعریف زیر، names مقدارهای positional دریافتی را در یک tuple جمع می‌کند. tuple مجموعه‌ای مرتب از مقدارهاست که ساختار خودِ آن تغییرپذیر نیست. منبع: [فهرست argumentها با تعداد دلخواه در آموزش رسمی Python](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists).

```python
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')
say_hi()
say_hi('ann')
say_hi('mike', 'john', 'zeo')
```

    Hi, ann!
    Hi, mike!
    Hi, john!
    Hi, zeo!

خطِ `say_hi()` هیچ خروجی‌ای ندارد. چون هنگام فراخوانی هیچ مقداری به function نداده‌اید، در زمان اجرای کد درون آن، مقدار `name in names` برابر `False` است و کد داخل loopِ `for` اجرا نمی‌شود.

> **یادداشت مترجم — توضیح تکمیلی:** توضیح جملهٔ قبل در متن اصلی دقیق نیست: for شرطِ عضویتِ name in names را ارزیابی نمی‌کند؛ بلکه از iterable عضو می‌گیرد و هر عضو را به name می‌دهد. اینجا names یک tuple خالی است، پس هیچ عضوی وجود ندارد و بدنهٔ loop اصلاً اجرا نمی‌شود. منبع: [دستور for در مرجع رسمی](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement).

درون function با parameterِ `names` مانند یک container رفتار می‌شود؛ وگرنه نمی‌شد از `for ... in ...` برای پردازش آن استفاده کرد. هنگام فراخوانی هم می‌توان عضوهای یک container را به Arbitrary Positional Arguments داد؛ کافی است در فراخوانی، پیش از argument علامت `*` بگذاریم:

```python
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')

names = ('mike', 'john', 'zeo')
say_hi(*names)
```

    Hi, mike!
    Hi, john!
    Hi, zeo!

در واقع، چون functionِ `say_hi(*names)` درون خودش مقدارهای دریافتی را مانند یک container پردازش می‌کند، هنگام فراخوانی هم هر containerی را به همین شکل به آن بدهیم، به همین شیوه پردازش می‌شود:

```python
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')

a_string = 'Python'
say_hi(*a_string)

a_range = range(10)
say_hi(*a_range)

a_list = list(range(10, 0, -1))
say_hi(*a_list)

a_dictionary = {'ann':2321, 'mike':8712, 'joe': 7610}
say_hi(*a_dictionary)
```

    Hi, P!
    Hi, y!
    Hi, t!
    Hi, h!
    Hi, o!
    Hi, n!
    Hi, 0!
    Hi, 1!
    Hi, 2!
    Hi, 3!
    Hi, 4!
    Hi, 5!
    Hi, 6!
    Hi, 7!
    Hi, 8!
    Hi, 9!
    Hi, 10!
    Hi, 9!
    Hi, 8!
    Hi, 7!
    Hi, 6!
    Hi, 5!
    Hi, 4!
    Hi, 3!
    Hi, 2!
    Hi, 1!
    Hi, ann!
    Hi, mike!
    Hi, joe!

> **یادداشت مترجم — توضیح تکمیلی:** علامت ستاره در فراخوانی، عمل unpacking را انجام می‌دهد: عضوهای یک iterable را به argumentهای جداگانه تبدیل می‌کند. iterable چیزی است که می‌توان عضوهایش را یکی‌یکی دریافت کرد؛ لازم نیست حتماً container باشد. در مورد dictionary، پیمایش معمول روی keyها انجام می‌شود و به همین دلیل مثال آخر نام‌ها را چاپ می‌کند، نه عددها را. منابع: [unpacking در آموزش رسمی](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists) و [پیمایش dictionary](https://docs.python.org/3/library/stdtypes.html#dict).

*وقتی parameterی برای دریافت چند مقدار positional تعریف می‌کنید، بهتر است نام آن درون function همیشه **جمع** باشد.* چون درون function معمولاً با loopِ `for` عضوهای tuple را پیمایش می‌کنیم، صورت جمع نام به خوانایی کد کمک زیادی می‌کند؛ به خط دوم برنامه‌های بالا توجه کنید. این جزئیات برای کسانی که زبان مادری‌شان چینی است، اغلب «طاقت‌فرسا» به نظر می‌رسد، چون اسم‌ها در چینی صورت جمع ندارند؛ اما باید به آن عادت کرد. به همین دلیل، نام‌گذاری variableها با پین‌یین هم قطعاً برای آینده دردسر درست می‌کند…

> **یادداشت مترجم — توضیح تکمیلی:** پین‌یین (Pinyin) روشی برای نوشتن تلفظ واژه‌های چینی با حروف لاتین است. اشارهٔ نویسنده به عادت بعضی برنامه‌نویسان چینی در نام‌گذاری است.

**توجه:** در هر function فقط یک parameter می‌تواند چند مقدار positional دریافت کند؛ و اگر positional parameterهای دیگری هم وجود داشته باشند، این parameter باید پس از همهٔ آن‌ها قرار بگیرد.

```python
def say_hi(greeting, *names):
    for name in names:
        print(f'{greeting}, {name.capitalize()}!')

say_hi('Hello', 'mike', 'john', 'zeo')
```

    Hello, Mike!
    Hello, John!
    Hello, Zeo!

## تعیین مقدار پیش‌فرض برای بعضی parameterها

هنگام تعریف function می‌توان برای بعضی parameterها مقدار پیش‌فرض گذاشت. به parameterهای دارای مقدار پیش‌فرض، keyword argument هم گفته می‌شود. از دید «استفاده‌کنندهٔ» function، این parameterها «اختیاری» می‌شوند.

> **یادداشت مترجم — توضیح تکمیلی:** متن اصلی در اینجا اصطلاح‌ها را دقیق تفکیک نکرده است. داشتن مقدار پیش‌فرض با keyword بودن argument یکی نیست. parameter دارای مقدار پیش‌فرض را می‌توان در فراخوانی حذف کرد؛ keyword argument یعنی مقداری که با نام داده می‌شود. در مثال زیر، capitalized پس از parameterِ ستاره‌دار آمده، پس keyword-only است؛ یعنی برای دادن مقدار به آن باید نامش را بنویسید. keyword-only parameter الزاماً مقدار پیش‌فرض ندارد. منبع: [parameterهای ویژه در آموزش رسمی Python](https://docs.python.org/3/tutorial/controlflow.html#special-parameters).

```python
def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hello', 'mike', 'john', 'zeo')
say_hi('Hello', 'mike', 'john', 'zeo', capitalized=True)
```

    Hello, mike!
    Hello, john!
    Hello, zeo!
    Hello, Mike!
    Hello, John!
    Hello, Zeo!

## keyword parameter برای دریافت چند مقدار

دیدیم که می‌توان positional parameterی تعریف کرد که چند مقدار دریافت کند؛ نام این حالت «Arbitrary Positional Argument» است.

به همین ترتیب می‌توان keyword parameterی برای دریافت چند مقدار تعریف کرد: Arbitrary Keyword Argument.

```python
def say_hi(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')

say_hi(mike='Hello', ann='Oh, my darling', john='Hi')
```

    Hello, mike!
    Oh, my darling, ann!
    Hi, john!

چون درون function برای پردازش Arbitrary Keyword Argument دریافتی، یک dictionary را پیمایش می‌کنیم، هنگام فراخوانی نیز می‌توانیم مستقیماً از dictionary استفاده کنیم:

```python
def say_hi(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')

a_dictionary = {'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'}
say_hi(**a_dictionary)

say_hi(**{'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'})
```

    Hello, mike!
    Oh, my darling, ann!
    Hi, john!
    Hello, mike!
    Oh, my darling, ann!
    Hi, john!

اینکه درون function کدام شیوهٔ پیمایش را برای پردازش این dictionary به کار ببرید، انتخاب خودتان است:

```python
def say_hi_2(**names_greetings):
    for name in names_greetings:
        print(f'{names_greetings[name]}, {name}!')
say_hi_2(mike='Hello', ann='Oh, my darling', john='Hi')
```

    Hello, mike!
    Oh, my darling, ann!
    Hi, john!

## ترتیب انواع parameter هنگام تعریف function

هنگام تعریف function، انواع مختلف parameter را با چه ترتیبی باید قرار داد؟ functionِ `say_hi()` را که پیش‌تر نوشتیم در نظر بگیرید:

```python
def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hi', 'mike', 'john', 'zeo')
say_hi('Welcome', 'mike', 'john', 'zeo', capitalized=True)
```

    Hi, mike!
    Hi, john!
    Hi, zeo!
    Welcome, Mike!
    Welcome, John!
    Welcome, Zeo!

اگر بخواهید برای parameterِ `greeting` هم مقدار پیش‌فرض تعیین کنید، چه باید کرد؟ به نظر می‌رسد می‌توان این‌طور نوشت:

```python
def say_hi(greeting='Hello', *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hi', 'mike', 'john', 'zeo')
say_hi('Welcome', 'mike', 'john', 'zeo', capitalized=True)
```

    Hi, mike!
    Hi, john!
    Hi, zeo!

    Welcome, Mike!
    Welcome, John!
    Welcome, Zeo!

اما با اینکه `greeting` مقدار پیش‌فرض دارد، هنگام فراخوانی این function باز هم باید مقدار آن را بدهید؛ وگرنه خروجی برخلاف انتظارتان خواهد بود:

```python
def say_hi(greeting='Hello', *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('mike', 'john', 'zeo')
```

    mike, john!
    mike, zeo!

پس `greeting` با وجود داشتن مقدار پیش‌فرض، آن‌طور که تصور می‌کردید «اختیاری» نیست! بنابراین باید این‌طور بنویسید:

```python
def say_hi(*names, greeting='Hello', capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('mike', 'john', 'zeo')
say_hi('mike', 'john', 'zeo', greeting='Hi')
```

    Hello, mike!
    Hello, john!
    Hello, zeo!
    Hi, mike!
    Hi, john!
    Hi, zeo!

علت این است که هنگام فراخوانی function با چند argument، Python باید طبق قواعد مشخص، یعنی ترتیب، تشخیص دهد هر argument از کدام نوع است:

> **ترتیب argumentها (Order of Arguments)**
> 1. Positional
> 1. Arbitrary Positional
> 1. Keyword
> 1. Arbitrary Keyword

بنابراین حتی اگر در تعریف بنویسید:

```python
def say_hi(greeting='Hello', *names, capitalized=False):
    ...
```

هنگام فراخوانی، چه بنویسید:
```python
say_hi('Hi', 'mike', 'john', 'zeo')
```

و چه بنویسید:
```python
say_hi('mike', 'john', 'zeo')
```

Python نخستین مقدار دریافتی را یک Positional Argument در نظر می‌گیرد؛ چون در تعریف، `greeting` پیش از Arbitrary Positional Arguments قرار گرفته است.

> **یادداشت مترجم — توضیح تکمیلی:** greeting در تعریفِ دارای مقدار پیش‌فرض واقعاً قابل حذف است؛ مثلاً فراخوانی بدون argument مجاز است، هرچند این function در آن حالت چیزی چاپ نمی‌کند. مشکل این است که نمی‌توانید اولین positional parameter را «رد کنید» و نخستین مقدار positional را مستقیماً به names بدهید؛ آن مقدار ابتدا به greeting می‌رسد. انتقال greeting به بعد از parameterِ ستاره‌دار آن را keyword-only می‌کند و مسئلهٔ مثال را حل می‌کند. فهرست چهارگانهٔ بالا نیز راهنمای ساده‌شدهٔ همین مثال‌هاست، نه تمام قواعد syntaxِ تعریف و فراخوانی در Python؛ positional-only parameterها و جزئیات دیگر در [آموزش رسمی parameterهای ویژه](https://docs.python.org/3/tutorial/controlflow.html#special-parameters) و [مرجع رسمی فراخوانی‌ها](https://docs.python.org/3/reference/expressions.html#calls) آمده‌اند.


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: دربارهٔ parameterها و argumentها (بخش اول)](Part.2.D.1-args.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: نام دیگر و function بی‌نام](Part.2.D.3-lambda.md)

</div>

<!-- reading-navigation:end -->
