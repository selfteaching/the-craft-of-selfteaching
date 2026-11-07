<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: چرا از نوشتن function شروع کنیم؟](Part.2.C.why-start-from-writing-functions.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: دربارهٔ parameterها و argumentها (بخش دوم)](Part.2.D.2-aargs.md)

</div>

<!-- reading-navigation:end -->


# دربارهٔ parameterها و argumentها (بخش اول)

پیش‌تر هم گفتیم که از نظر ساختار، هر function یک برنامهٔ کامل است؛ چون بخش‌های اصلی یک برنامه ورودی، پردازش و خروجی هستند:

> * می‌تواند **ورودی** داشته باشد؛ یعنی مقدارهایی را که از بیرون از طریق parameterها به آن داده می‌شود دریافت کند.
> * می‌تواند **پردازش** داشته باشد؛ یعنی درون آن کدی باشد که کار مشخصی انجام دهد؛ به‌ویژه بتواند بر اساس «ورودی»، «خروجی» تولید کند.
> * می‌تواند **خروجی** داشته باشد؛ یعنی مقداری را به بیرون برگرداند…

بنابراین، به نظر من پس از یاد گرفتن کمی از مبانی، نخستین چیزی که باید یاد گرفت «چگونه function بنویسیم» است؛ این نقطهٔ شروع بهتری خواهد بود.

ممکن است به نظر برسد مطالب این فصل تا حدی با [فصل functionها در Part1.E.4](Part.1.E.4.functions.md) هم‌پوشانی دارد. اما هدف این دو فصل متفاوت است:

> * [فصل functionها در Part1.E.4](Part.1.E.4.functions.md) فقط برای این بود که خواننده بتواند مستندات functionها را «بخواند».
> * این فصل برای آن است که خواننده دست‌به‌کار شود و برای خودش یا دیگران function بنویسد…

> **یادداشت مترجم — توضیح تکمیلی:** parameter نامی است که در تعریف function برای دریافت ورودی می‌نویسید؛ argument مقداری است که هنگام فراخوانی به آن می‌دهید. در متن اصلی، یک واژه برای هر دو به کار رفته است؛ در این ترجمه، بسته به منظور جمله، از اصطلاح دقیق‌تر استفاده می‌شود. برای نمونه، در تعریفِ نخستین مثالِ دریافت سال در ادامه، year یک parameter است و عددی که هنگام فراخوانی داده می‌شود argument است. منبع: [واژه‌نامهٔ رسمی Python](https://docs.python.org/3/glossary.html#term-parameter).

## نام‌گذاری function

حتی اگر function درون خودش هیچ کاری نکند، باز هم باید نامی داشته باشد. پس از نام هم پرانتز `()` می‌آید تا روشن شود که با function سروکار داریم، نه صرفاً یک variable.

برای تعریف function از keywordِ `def` استفاده می‌کنیم. کد زیر functionی تعریف می‌کند که هیچ کاری انجام نمی‌دهد:

```python
def do_nothing():
    pass

do_nothing()
```

برای نام‌گذاری functionها، و همین‌طور variableها، چند نکتهٔ پایه را باید رعایت کرد:

> - نخست، نام نمی‌تواند با رقم شروع شود. برای شروع نام می‌توان از حروف بزرگ و کوچک و underscore، یعنی `_`، استفاده کرد.
>
> - دوم، نام نباید فاصله داشته باشد. یا واژه‌ها را با underscore به هم وصل کنید، مثل `do_nothing`، یا از [Camel Case](https://en.wikipedia.org/wiki/Camel_case) استفاده کنید، مثل `doNothing`. استفاده از underscore بیشتر توصیه می‌شود.
>
> - سوم، نام نباید یکی از keywordها باشد. فهرست keywordهای Python چنین است:

|     -      | Python     | Keyword    | List       |     -      |
| ---------- | ---------- | ---------- | ---------- | ---------- |
| `and`      | `as`       | `assert`   | `async`    | `await`    |
| `break`    | `class`    | `continue` | `def`      | `del`      |
| `elif`     | `else`     | `except`   | `False`    | `finally`  |
| `for`      | `from`     | `global`   | `if`       | `import`   |
| `in`       | `is`       | `lambda`   | `None`     | `nonlocal` |
| `not`      | `or`       | `pass`     | `raise`    | `return`   |
| `True`     | `try`      | `while`    | `with`     | `yield`    |

هر زمان بخواهید، می‌توانید با کد زیر فهرست keywordها را بررسی کنید:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import keyword
keyword.kwlist               # 列出所有关键字
keyword.iskeyword('if')      # 查询某个词是不是关键字
```

    ['False',
     'None',
     'True',
     'and',
     'as',
     'assert',
     'async',
     'await',
     'break',
     'class',
     'continue',
     'def',
     'del',
     'elif',
     'else',
     'except',
     'finally',
     'for',
     'from',
     'global',
     'if',
     'import',
     'in',
     'is',
     'lambda',
     'nonlocal',
     'not',
     'or',
     'pass',
     'raise',
     'return',
     'try',
     'while',
     'with',
     'yield']
    
    True

> **یادداشت مترجم — توضیح تکمیلی:** keyword واژه‌ای است که Python برای syntax خود معنای ویژه‌ای به آن داده است. فهرست و خروجی بالا متعلق به محیط زمان نگارش کتاب‌اند؛ نسخه‌های جدیدتر ممکن است soft keyword هم داشته باشند، یعنی واژه‌هایی که فقط در بافت‌های مشخص معنای ویژه دارند. فهرست متناسب با نسخهٔ نصب‌شده را با moduleِ keyword بررسی کنید. همچنین قواعد کامل نام‌گذاری، حروف مجاز Unicode را هم در بر می‌گیرد. منابع: [مستندات keyword](https://docs.python.org/3/library/keyword.html) و [قواعد نام‌ها و keywordها](https://docs.python.org/3/reference/lexical_analysis.html#names).

برای آگاهی از نکته‌های بیشتر دربارهٔ نام‌گذاری functionها و variableها، این منابع را ببینید:

> * [PEP 8 -- Style Guide for Python Code: Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)
> * [PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)
>
> توجه: PEPs کوتاه‌شدهٔ Python Enhancement Proposals، یعنی پیشنهادهای بهبود Python است: https://www.python.org/dev/peps/

## functionی که هیچ argumentی دریافت نمی‌کند

هنگام تعریف function می‌توانید آن را طوری بنویسید که هیچ argumentی نگیرد؛ بااین‌حال، هنگام فراخوانی همچنان باید پرانتز `()` را پس از نامش بنویسید:

```python
def do_something():
    print('This is a hello message from do_something().')

do_something()
```

    This is a hello message from do_something().

## function بدون دستور return

لازم نیست درون function حتماً دستور `return` وجود داشته باشد؛ برای نمونه، functionِ `do_something()` در بالا چنین دستوری ندارد. اما اگر در function مقداری برای بازگشت مشخص نشده باشد، مقدار بازگشتی آن `None` خواهد بود. وقتی `None` در جایگاه یک مقدار Boolean ارزیابی شود، مانند `False` رفتار می‌کند.

به همین دلیل، نتیجهٔ فراخوانی یک function را همیشه می‌توان مبنای بررسی در یک دستور شرطی قرار داد:

```python
def do_something():
    print('This is a hello message from do_something().')

if not do_something():                # 由于该函数名称的缘故，这一句代码的可读性很差……
    print("The return value of 'do_something()' is None.")
```

    This is a hello message from do_something().
    The return value of 'do_something()' is None.

اگر `if not do_something(): ` را به زبان عادی بیان کنیم، می‌شود: «اگر مقدار بازگشتیِ `do_something()` درست محسوب نمی‌شود، آنگاه…»

## دریافت مقدار از بیرون

بیایید functionی برای تشخیص سال کبیسه بنویسیم و نامش را `is_leap()` بگذاریم. این function یک سال را به‌عنوان argument می‌گیرد؛ اگر سال کبیسه باشد `True` و در غیر این صورت `False` برمی‌گرداند.

طبق تعریف سال کبیسه:

> * سال باید مضربی از ۴ باشد.
> * سالی که بر ۱۰۰ بخش‌پذیر باشد اما بر ۴۰۰ بخش‌پذیر نباشد، کبیسه نیست.

پس باید از میان سال‌های بخش‌پذیر بر ۴، آن‌هایی را کنار بگذاریم که بر ۱۰۰ بخش‌پذیرند اما بر ۴۰۰ بخش‌پذیر نیستند.

> **یادداشت مترجم — توضیح تکمیلی:** منظور این مثال، سال کبیسه در تقویم میلادیِ Gregorian است، نه تقویم هجری خورشیدی. مستندات [moduleِ calendar](https://docs.python.org/3/library/calendar.html) نیز مبنای تقویم مورد استفاده در Python را توضیح می‌دهد.

```python
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False
    return leap

is_leap(7)
is_leap(12)
is_leap(100)
is_leap(400)
```

    False
    True
    False
    True

```python
# 另外一个更为简洁的版本，理解它还挺练脑子的
# cpython/Lib/datetime.py
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
_is_leap(300)
```

    False

> **یادداشت مترجم — توضیح تکمیلی:** comment چینیِ بالای مثال می‌گوید این نسخه کوتاه‌تر است و فهمیدن آن تمرین ذهنی خوبی است؛ خط بعد هم به منبع آن در CPython اشاره دارد. همهٔ commentهای کد در این ترجمه عیناً حفظ شده‌اند.

یک function می‌تواند هم‌زمان چند argument دریافت کند. برای نمونه، می‌توانیم functionی بنویسیم که عددهای دنبالهٔ فیبوناچی را میان دو عدد چاپ کند؛ بزرگ‌تر از یک عدد و کوچک‌تر از عدد دیگر. برای این کار باید دو parameter تعریف کنیم و هنگام فراخوانی نیز دو argument بدهیم:

```python
def fib_between(start, end):
    a, b = 0, 1
    while a < end:
        if a >= start:
            print(a, end=' ')
        a, b = b, a + b

fib_between(100, 10000)
```

    144 233 377 610 987 1597 2584 4181 6765

> **یادداشت مترجم — توضیح تکمیلی:** در توصیف اصلی «بزرگ‌تر از» آمده، اما کد با شرط `a >= start` خودِ کران آغازین را هم شامل می‌شود؛ کران پایانی شامل نمی‌شود. متن و کد اصلی برای روشن ماندن این تفاوت حفظ شده‌اند.

البته می‌توان این function را طوری هم نوشت که به‌جای چاپ کردن، یک list برگرداند:

```python
def fib_between(start, end):
    r = []
    a, b = 0, 1
    while a < end:
        if a >= start:
            r.append(a)
        a, b = b, a + b
    return r

fib_between(100, 10000)
```

    [144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

## scopeِ variableها

کد زیر اغلب تازه‌کارها را سردرگم می‌کند:

```python
def increase_one(n):
    n += 1
    return n

n = 1
print(increase_one(n))
# print(n)
```

    2

پس از فراخوانی `increase_one(n)`، مقدار `n` دقیقاً چقدر است؟ یا دقیق‌تر بپرسیم: خروجیِ `print(n)` پس از آن چه باید باشد؟

خروجی `1` است.

در جریان اجرای برنامه، variableها به **global variable** و **local variable** تقسیم می‌شوند.

> نخست، هر بار که functionی فراخوانی می‌شود، محدودهٔ تازه‌ای برای آن ایجاد می‌شود و variableهای درون آن local هستند. بنابراین، حتی اگر نام یک variable درون function با نام یک global variable بیرون از آن یکی باشد، این دو یک variable نیستند؛ فقط نام یکسانی دارند.
>
> دوم، و مهم‌تر اینکه هنگام فراخوانی function از بیرون، به بیان دقیق، خودِ variable منتقل نمی‌شود، بلکه *مقدار* آن منتقل می‌شود. یعنی هنگام فراخوانی `increase_one(n)`، چیزی که به local variableی با نامِ تصادفاً یکسانِ `n` داده می‌شود، مقدارِ global variableِ `n`، یعنی `1` است.
>
> سپس کدِ `increase_one()` اجرا می‌شود. پس از `n += 1`، مقدار ذخیره‌شده در local variableِ `n` برابر `2` می‌شود. دستور `return` همین مقدار را برمی‌گرداند؛ بنابراین خروجیِ `print(increase_one(n))` مقدار بازگشتی function، یعنی `2` است.
>
> اما مقدار global variableِ `n` عوض نشده است؛ چون local variableِ `n` با مقدار `2` و global variableِ `n` با مقدارِ همچنان `1`، فقط هم‌نام‌اند و یک variable نیستند.

> **یادداشت مترجم — توضیح تکمیلی:** scope محدوده‌ای است که یک نام در آن قابل دسترسی است. توضیح بالا دربارهٔ local بودن همهٔ variableها ساده‌سازی شده است؛ برای نمونه، دستورهای global و nonlocal قواعد جداگانه‌ای دارند. همچنین argumentها با «اشتراک object» منتقل می‌شوند: نامِ parameter به همان object داده‌شده متصل می‌شود، نه لزوماً به یک کپی مستقل از آن. در این مثال، عدد صحیح immutable است و افزایش دادن local variable، نام بیرونی را تغییر نمی‌دهد. مثال list در ادامه تفاوت را نشان می‌دهد. منابع: [تعریف function در آموزش رسمی](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) و [قواعد نام‌گذاری و اتصال نام‌ها](https://docs.python.org/3/reference/executionmodel.html#binding-of-names). دو اشتباه تایپیِ نام function در نثر اصلی، یعنی do_somthing و increase، در توضیحات این ترجمه با نام درستِ مثال‌ها نوشته شده‌اند؛ کدها تغییر نکرده‌اند.

شاید لازم باشد توضیح بالا را چند بار بخوانید. اگر پس از چند بار خواندن ابهام برطرف شود، دیگر از این بابت مشکلی نخواهید داشت؛ اما اگر ابهام باقی بماند یا نکتهٔ اصلی را درست درک نکنید، بعدها بارها گرفتار همین مسئله می‌شوید و زمان زیادی از دست می‌دهید.

بااین‌حال، یک حالت نیازمند توجه ویژه است: وقتی مقداری که به function داده می‌شود یک containerِ mutable، مثل list، باشد و درون function روی آن کار کنید:

```python
def be_careful(a, b):
    a = 2
    b[0] = 'What?!'

a = 1
b = [1, 2, 3]
be_careful(a, b)
a, b
```

    (1, ['What?!', 2, 3])

بنابراین عادت نسبتاً خوبی است که اگر مقدار ورودی یک list است، پیش از کار کردن روی آن درون function، یک کپی از آن بسازید:

```python
def be_careful(a, b):
    a = 2
    b_copy = b.copy()
    b_copy[0] = 'What?!'

a = 1
b = [1, 2, 3]
be_careful(a, b)
a, b
```

    (1, [1, 2, 3])

> **یادداشت مترجم — توضیح تکمیلی:** mutable یعنی محتوای object را می‌توان تغییر داد. کپی گرفتن وقتی مناسب است که قصد ندارید list اصلی را تغییر دهید؛ بعضی functionها عمداً ورودی را تغییر می‌دهند. همچنین copy در این مثال یک shallow copy می‌سازد: خودِ list تازه است، اما اگر عضوهای آن objectهای mutable باشند، آن عضوها همچنان مشترک‌اند. منبع: [مستندات رسمی copy](https://docs.python.org/3/library/copy.html).


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: چرا از نوشتن function شروع کنیم؟](Part.2.C.why-start-from-writing-functions.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: دربارهٔ parameterها و argumentها (بخش دوم)](Part.2.D.2-aargs.md)

</div>

<!-- reading-navigation:end -->
