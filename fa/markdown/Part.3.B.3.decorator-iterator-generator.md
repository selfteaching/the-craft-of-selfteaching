<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: class — پیاده‌سازی در Python](Part.3.B.2.classes-2.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: Regular Expression](Part.3.B.4.regex.md)

</div>

<!-- reading-navigation:end -->


# ابزارهای function

> **یادداشت مترجم — وضعیت ترجمه:** متن کامل با [فصل اصلی به زبان چینی](../../markdown/Part.3.B.3.decorator-iterator-generator.md) تطبیق و از نظر معنا و کامل‌بودن بازبینی شده است؛ این نسخه نهایی نیست و فقط برای مطالعهٔ شخصی و محلی تهیه شده است. کدها، commentها و خروجی‌های ثبت‌شده بدون تغییر حفظ شده‌اند؛ ایرادهای منبع در یادداشت‌های جداگانه توضیح داده می‌شوند. مثال‌ها در این نوبت دوباره اجرا نشده‌اند. ساختار عنوان‌ها و مقصد لینک‌های محلی بررسی شده‌اند؛ نمایش نهایی راست‌به‌چپ و دسترس‌پذیری منابع بیرونی بررسی نشده است. این فصل تصویری ندارد. انتساب اثر به Li Xiaolai و مجوز اعلام‌شدهٔ کتاب، CC BY-NC-ND 3.0، محفوظ است؛ این ترجمه برای انتشار یا push عمومی تهیه نشده است.

این فصل دربارهٔ iterator، generator و decorator است؛ همهٔ این‌ها از ابزارهای کار با function هستند. بعضی‌ها آن‌ها را **DIG** می‌نامند؛ کوتاه‌شدهٔ Decorator، Iterator و Generator. هر سه برای تسلط واقعی بر Python کلیدی‌اند.

## iterator

همهٔ containerهایی که تا اینجا در Python دیده‌ایم iterable هستند؛ دقیق‌تر بگوییم، می‌توان با iteration تک‌تک عضوهایشان را پیمایش کرد:

> **یادداشت مترجم — توضیح تکمیلی:** پیش‌نیاز این بخش، آشنایی با function، class و loop است؛ برای مرور class می‌توانید به [فصل نخست classها](Part.3.B.1.classes-1.md) و [فصل دوم classها](Part.3.B.2.classes-2.md) مراجعه کنید. iterable چیزی است که می‌توان از آن iterator گرفت؛ iterator، objectای است که وضعیت پیمایش را نگه می‌دارد و با هر فراخوانی next عضو بعدی را می‌دهد. در iterator protocol، methodِ `__iter__` باید یک iterator برگرداند و methodِ `__next__` عضو بعدی را برمی‌گرداند یا پایان پیمایش را با StopIteration اعلام می‌کند. `__iter__` در خودِ iterator همان object را برمی‌گرداند. هر iterator یک iterable هم هست، اما هر iterable الزاماً iterator نیست؛ مثلاً list را می‌توان پیمایش کرد، ولی برای گرفتن عضوهایش با next ابتدا باید از آن iterator بگیرید. منبع: [Iterator Types در مستندات رسمی](https://docs.python.org/3/library/stdtypes.html#iterator-types).

```python
string = "this is a string."
list = ['item 1', 'item 2', 3, 5]
set = (1, 2, 3, 4, 5)
for c in string:
    print(c, end=', ')
print()
for L in list:
    print(L, end=', ')
print()
for s in set:
    print(s, end=', ')
print()
```

    t, h, i, s,  , i, s,  , a,  , s, t, r, i, n, g, .,
    item 1, item 2, 3, 5,
    1, 2, 3, 4, 5,

> **یادداشت مترجم — توضیح تکمیلی:** در مثال اصلی، مقدار variableای با نام set در واقع tuple است، نه set؛ نام یک variable نوع مقدار آن را تعیین نمی‌کند. همچنین نام‌های list و set در این محیط، نام builtinهای هم‌نام را می‌پوشانند؛ یعنی تا وقتی این نام‌گذاری برقرار باشد، مراجعه به این نام‌ها به مقدارهای بالا می‌رسد، نه به builtinهای اصلی. این نام‌ها برای وفاداری به منبع تغییر نکرده‌اند؛ در کد خودتان بهتر است نام‌های دیگری انتخاب کنید. منبع: [قواعد نام‌گذاری و binding](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding).

یک builtin function به نام iter وجود دارد که کارش تبدیل یک iterable به iterator است.

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

i = iter("Python")
type(i)
s = iter((1, 2, 3, 4, 5))
type(s)
L = iter(['item 1', 'item 2', 3, 5])
type(L)
```

    str_iterator
    
    tuple_iterator
    
    list_iterator

چطور از iterator استفاده کنیم؟ برای این کار functionای به نام next داریم:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

i = iter("Python")
next(i)
next(i)
next(i)
next(i)
next(i)
next(i)
# next(i) 前面已经到 'n' 了，再调用就会有 StopIteration 错误提示。
```

    'P'
    'y'
    't'
    'h'
    'o'
    'n'

در iterator به نام i در مجموع ۶ عضو وجود دارد. بنابراین، پس از شش بار فراخوانی next روی i، دیگر نمی‌توان آن را فراخواند؛ اگر دوباره فراخوانی شود، خطای StopIteration رخ می‌دهد.

> **یادداشت مترجم — توضیح تکمیلی:** منظور از «دیگر نمی‌توان فراخواند» این نیست که خودِ فراخوانی ممنوع یا نامعتبر است؛ فراخوانی بعدی مجاز است، اما چون iterator به پایان رسیده است، به‌جای عضو تازه، exceptionِ StopIteration را ایجاد می‌کند. این رفتار عادیِ پایان پیمایش است؛ for آن را مدیریت می‌کند. اگر argument دومِ next را به‌عنوان مقدار پیش‌فرض بدهید، پس از پایان پیمایش همان مقدار برگردانده می‌شود. comment چینیِ دست‌نخوردهٔ کد نیز می‌گوید: «تا اینجا به 'n' رسیده‌ایم؛ اگر دوباره next(i) را فراخوانی کنیم، پیام خطای StopIteration می‌گیریم.» منبع: [مستندات رسمی next](https://docs.python.org/3/library/functions.html#next).

حالا چطور خودمان یک iterator بنویسیم؟

iterator یک object است، پس برای نوشتن آن یک class می‌نویسیم. برای مثال، بیایید iteratorای به نام Counter برای شمردن بنویسیم:

```python
class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c

c = Counter(11, 20)
next(c)
next(c)
next(c)
for c in Counter(101, 105):
    print(c, end=', ')
type(Counter)
```

    11
    12
    13
    101
    102
    103
    104
    105
    
    type

> **یادداشت مترجم — توضیح تکمیلی:** خروجی ثبت‌شدهٔ منبع با کد بالا کاملاً سازگار نیست و عمداً اصلاح نشده است: در loop، argumentِ end باعث می‌شود عددهای 101 تا 105 در یک خط و با «ویرگول و فاصله» چاپ شوند، نه هرکدام در خطی جدا. همچنین نتیجهٔ type(Counter) نوعِ خودِ class را نشان می‌دهد که در این مثال type است؛ این عبارت نوعِ instanceای ساخته‌شده از Counter را نمی‌سنجد. خروجی‌ها از منبع نقل شده‌اند و گزارش اجرای دوباره نیستند. منبع: [مستندات print](https://docs.python.org/3/library/functions.html#print) و [مستندات type](https://docs.python.org/3/library/functions.html#type).

نکتهٔ اصلی اینجاست که دو function وجود دارند: `__iter__`(self) و `__next__`(self).

```python
def __iter__(self):
    return self
```

این دو خط، شیوهٔ قراردادیِ نوشتن آن هستند؛ با نوشتنشان، classِ Counter به‌عنوان یک Iterator شناخته می‌شود. اگر `__next__`(self) را هم داشته باشد، یک iterator کامل خواهیم داشت. علاوه بر for loop، می‌توان با while loop هم تمام عضوهای iterator را پیمایش کرد:

> **یادداشت مترجم — توضیح تکمیلی:** بیان بالا را باید در چارچوب iterator protocol خواند: داشتن `__iter__` به‌تنهایی برای iterator بودن کافی نیست؛ object باید `__next__` مناسب هم داشته باشد. در مثال زیر، try تلاش می‌کند عضو بعدی را بگیرد و except با دریافت StopIteration، loop را با break پایان می‌دهد.

```python
class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c

for c in Counter(101, 103):
    print(c, sep=', ')

c = Counter(201, 203)
while True:
    try:
        print(next(c), sep=', ')
    except StopIteration:
        break
```

    101
    102
    103
    201
    202
    203

## generator

آیا می‌توان Counter را با function نوشت، نه با class؟ بله؛ کافی است از generator استفاده کنیم.

> **یادداشت مترجم — توضیح تکمیلی:** generator function، functionای است که در بدنه‌اش yield دارد. فراخوانی آن یک generator object می‌سازد؛ این object خودش iterator است و بدنهٔ function را مرحله‌به‌مرحله اجرا می‌کند. بنابراین تقابل این بخش در واقع میان پیاده‌سازی دستیِ iterator با class و ساختن آن با generator function است، نه میان دو نوع کاملاً جدا از هم. منبع: [Generator functions در مستندات رسمی](https://docs.python.org/3/reference/expressions.html#generator-iterator-methods).

```python
def counter(start, stop):
    while start <= stop:
        yield start
        start += 1
for i in counter(101, 105):
    print(i)
```

    101
    102
    103
    104
    105

عجب! به نظر نمی‌رسد این یکی خیلی کوتاه‌تر و ساده‌تر است؟

البته کوتاه‌بودن کد اصل ماجرا نیست. این بار generator ساده‌تر به نظر می‌رسد، فقط چون مثال فعلی برای آن مناسب‌تر است. در موقعیت‌های متفاوت، استفاده از iterator و generator هرکدام مزیت‌های خودشان را دارند.

نکتهٔ کلیدی در اینجا دستور yield است. آشکارترین تفاوت آن با return این است که دستورهای پس از yield همچنان اجرا می‌شوند، اما دستورهای پس از return نادیده گرفته می‌شوند.

اما به‌دلیل همین تفاوت، هنگام نوشتن generator فقط می‌توان از yield استفاده کرد و نمی‌توان return به کار برد. حالا می‌توانید برگردید و در کد بالا yield را به return تغییر دهید و تفاوتشان را ببینید.

وقتی generator function با next فراخوانی شود، اجرا تا yield پیش می‌رود، یک مقدار تولید و برگردانده می‌شود؛ سپس دستورهای باقی‌مانده در بیرونِ next اجرا می‌شوند. دفعهٔ بعد که next فراخوانی شود، اجرا از محل همان yield که دفعهٔ پیش مقدار را برگردانده بود ادامه پیدا می‌کند… اگر فهمش دشوار است، چند بار بخوانید؛ بعد هم فکر کنید اگر در generator چند دستور yield داشته باشیم چه اتفاقی می‌افتد.

> **یادداشت مترجم — توضیح تکمیلی:** توضیح منبع در این چند جمله نیاز به دقت دارد. next روی generator object کار می‌کند، نه مستقیماً روی generator function. yield اجرا را معلق می‌کند و مقدار را به فراخواننده می‌دهد؛ دستورهای بعد از آن بلافاصله اجرا نمی‌شوند. در مثال حاضر، اجرای آن‌ها تنها با درخواست بعدی از طریق next، از جمله درخواست ضمنیِ for، از سر گرفته می‌شود. generatorها راه‌های دیگری مانند send نیز برای ازسرگیری دارند. برخلاف ادعای بالا، return در generator مجاز است، اما اجرای generator را پایان می‌دهد؛ return همراه مقدار، آن مقدار را در StopIteration.value قرار می‌دهد، نه اینکه مانند yield عضو بعدی را تولید کند. اگر تنها yield مثال را به return تبدیل کنید، آن function دیگر generator function نخواهد بود و در اولین دور مقدار start را برمی‌گرداند. این پیشنهاد منبع در این نوبت اجرا نشده است. منبع: [Yield expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions) و [دستور return](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement).

چیز دیگری هم داریم به نام generator expression. اول یک مثال ببینید:

```python
even = (e for e in range(10) if not e % 2)
# odd = (o for o in range(10) if o % 2)
print(even)
for e in even:
    print(e)
```

    <generator object <genexpr> at 0x107cc0048>
    0
    2
    4
    6
    8

در واقع، این نوع expression را پیش‌تر در List Comprehension دیده‌ایم؛ همان کار با generator expression انجام می‌شد.

**توجه**

به پرانتزهای بیرونیِ عبارت even = (e for e in range(10) if not e % 2) خوب نگاه کنید. با پرانتز، even یک Iterator است که با generator ساخته شده است؛ اگر به‌جای آن از براکت استفاده کنیم، یک List خواهیم داشت که با generator ساخته شده است. البته با آکولاد {} هم یک Set ساخته می‌شود…

> **یادداشت مترجم — توضیح تکمیلی:** منبع در دو بند بالا این مفهوم‌ها را بیش از حد یکی گرفته است. generator expression با پرانتز یک generator می‌سازد و مقدارها را هنگام درخواست تولید می‌کند؛ list comprehension با براکت، list را می‌سازد و عضوهایش را همان موقع محاسبه می‌کند؛ set comprehension با آکولاد، set می‌سازد. این‌ها syntaxهای شبیه به هم ولی متمایزند؛ list comprehension و set comprehension را نباید «ساخته‌شده با generator expression» دانست. همچنین set ترتیب پیمایش تضمین‌شده‌ای ندارد؛ ترتیب خروجی ثبت‌شدهٔ آن در مثال زیر قراردادی همگانی نیست. منبع: [مستندات رسمی comprehensionها](https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries) و [Generator expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions).

```python
# even = (e for e in range(10) if not e % 2)
odd = [o for o in range(10) if o % 2]
print(odd)
for o in odd:
    print(o)
```

    [1, 3, 5, 7, 9]
    1
    3
    5
    7
    9

```python
# even = (e for e in range(10) if not e % 2)
odd = {o for o in range(10) if o % 2}
print(odd)
for o in odd:
    print(o)
```

    {1, 3, 5, 7, 9}
    1
    3
    5
    7
    9

**generator expression باید داخل پرانتز به کار برود**؛ بنگرید به [HOWTO رسمی](https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions). پرانتزهای argumentهای یک function هم می‌توانند همین نقش را داشته باشند، مثلاً:

```python
sum_of_even = sum(e for e in range(10) if not e % 2)
print(sum_of_even)
```

    20

> **یادداشت مترجم — توضیح تکمیلی:** حذف پرانتزِ جداگانهٔ generator expression در فراخوانی function، مانند مثال بالا، زمانی مجاز است که generator expression تنها argument باشد؛ اگر argument دیگری هم وجود داشته باشد، باید پرانتزِ خودِ expression را نگه دارید. منبع: [Generator expressions در مرجع زبان](https://docs.python.org/3/reference/expressions.html#generator-expressions).

طبیعتاً داخل یک function می‌توان functionهای دیگری هم داشت. مثال زیر ساختار functionای را نشان می‌دهد که functionهای دیگری درونش تعریف شده‌اند:

```python
def a_func():
    def b_func():
        pass
    def c_func():
        pass
        def d_func():
            pass
        b_func()
    return True
```

حالا تصور کنید یک function، function دیگری را برگرداند. قدم‌به‌قدم پیش برویم:

```python
def a_func():
    def b_func():
        print("Hi, I'm b_func!")
    print("Hi, I'm a_func!")
a_func()
```

    Hi, I'm a_func!

```python
def a_func():
    def b_func():
        print("Hi, I'm b_func!")
    print("Hi, I'm a_func!")
    b_func()
a_func()
```

    Hi, I'm a_func!
    Hi, I'm b_func!

کد قبلی را می‌توانیم این‌طور بنویسیم: a_func نتیجهٔ فراخوانیِ b_func داخلی‌اش را به‌عنوان مقدار بازگشتی برگرداند:

```python
def a_func():
    def b_func():
       print("Hi, I'm b_func!")
    print("Hi, I'm a_func!")
    return b_func()
a_func()
```

    Hi, I'm a_func!
    Hi, I'm b_func!

اگر در دستور return فقط نام function را بنویسیم چه؟ به این شکل:

```python
def a_func():
    def b_func():
        print("Hi, I'm b_func!")
    print("Hi, I'm a_func!")
    return b_func
a_func()
```

    Hi, I'm a_func!
    <function __main__.a_func.<locals>.b_func()>

این بار چیزی که برمی‌گردد، نتیجهٔ اجرای فراخوانیِ b_func نیست؛ *خودِ function* به نام b_func برگردانده می‌شود.

## decorator

### function هم object است

نکتهٔ کلیدی همین است:

> خودِ function هم یک object است؛ یعنی instanceای از یکی از classهایی که Python تعریف کرده است.

بنابراین، خودِ function هم درست مثل داده‌هایی از نوع‌های دیگر، می‌تواند argument یا مقدار بازگشتیِ function دیگری باشد.

قدم‌به‌قدم پیش برویم. دقت کنید که در کد زیر، a_decorator نتیجهٔ فراخوانیِ wrapper را برمی‌گرداند، نه خودِ functionِ wrapper را:

```python
def a_decorator(func):
    def wrapper():
        print('We can do sth. before a func is called...')
        func()
        print('... and we can do sth. after it is called...')
    return wrapper()

def a_func():
    print("Hi, I'm a_func!")

a_func()
a_decorator(a_func)
```

    Hi, I'm a_func!
    We can do sth. before a func is called...
    Hi, I'm a_func!
    ... and we can do sth. after it is called...

اگر خودِ functionِ wrapper برگردانده شود، خروجی آن چیزی نیست که شاید انتظار داشته باشید:

```python
def a_decorator(func):
    def wrapper():
        print('We can do sth. before a func is called...')
        func()
        print('... and we can do sth. after it is called...')
    return wrapper  #

def a_func():
    print("Hi, I'm a_func!")

a_func()
a_decorator(a_func)
```

    Hi, I'm a_func!
    <function __main__.a_decorator.<locals>.wrapper()>

### operator مربوط به decorator

اما Python برای functionها operatorای به نام @ فراهم کرده است که کارش… توضیح یک‌بارهٔ آن آسان نیست؛ اول به کد زیر نگاه کنید:

```python
def a_decorator(func):
    def wrapper():
        print('We can do sth. before calling a_func...')
        func()
        print('... and we can do sth. after it was called...')
    return wrapper

@a_decorator
def a_func():
    print("Hi, I'm a_func!")

a_func()
```

    We can do sth. before calling a_func...
    Hi, I'm a_func!
    ... and we can do sth. after it was called...

دقت کنید: در کد بالا، a_decorator(func) خودِ functionِ wrapper را برمی‌گرداند.

هنگام تعریف a_func، پیش از آن یک خط @a_decorator اضافه کرده‌ایم. نتیجهٔ این کار چنین است:

> هر بار که a_func فراخوانی می‌شود، چون پیش از آن @a_decorator آمده است، ابتدا به‌عنوان argument به a_decorator(func) داده می‌شود… سپس اجرای واقعی درون a_decorator انجام می‌شود.

— functionای که با @ فراخوانی می‌شود، decorator نام دارد؛ مثل a_decorator(func) در مثال بالا.

> **یادداشت مترجم — توضیح تکمیلی:** نقل‌قول بالا زمان اعمال decorator را نادرست بیان می‌کند. decorator هنگام اجرای تعریف function اعمال می‌شود، نه در هر فراخوانیِ بعدی. در این مثال، همان موقع function اصلی به a_decorator داده می‌شود و نام a_func به wrapper بازگشتی اشاره می‌کند. در فراخوانی‌های بعدی، wrapper اجرا می‌شود؛ a_decorator دوباره اجرا نمی‌شود. @ در این جایگاه syntaxِ decorator است؛ نباید آن را با کاربرد @ به‌عنوان operator ضرب ماتریسی یکی دانست. دو قطعهٔ بعدیِ خودِ منبع نیز معادل‌بودن این فرایند را نشان می‌دهند. منبع: [Function definitions در مرجع رسمی](https://docs.python.org/3/reference/compound_stmts.html#function-definitions).

حالا می‌توان نقش decorator را خیلی ساده و مستقیم توضیح داد:

```python
@a_decorator
def a_func():
    ...
```

معادل است با:

```python
def a_func():
    ...
a_func = a_decorator(a_func)
```

یعنی function اصلی را با نتیجهٔ فراخوانیِ a_decorator جایگزین می‌کنیم. مقدار بازگشتیِ a_decorator هرچه باشد، فراخوانی‌های بعدیِ a_func در واقع همان مقدار بازگشتی را فراخوانی می‌کنند؛ خودِ a_decorator تا آن زمان اجرای خود را تمام کرده است.

### کاربرد decorator

رایج‌ترین کاربرد Decorator چیست؟ رایج‌ترین کاربردش تغییر رفتار functionهای دیگر است.

```python
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'
print(an_output())
```

    The quick brown fox jumps over the lazy dog.

```python
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_restult = original_result.upper()
        return modified_restult
    return wrapper

@uppercase
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'
print(an_output())
```

    THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.

می‌توانید بیش از یک decorator هم به یک function اضافه کنید:

```python
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_restult = original_result.upper()
        return modified_restult
    return wrapper
def strong(func):
    def wrapper():
        original_result = func()
        modified_restult = '<strong>'+original_result+'</strong>'
        return modified_restult
    return wrapper

@strong
@uppercase
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'
print(an_output())
```

    <strong>THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.</strong>

جای دو decorator را عوض کنید و به شکل زیر بنویسید و امتحان کنید:

```python
@uppercase
@strong
def an_output():
...
```
ترتیب اجرای decoratorها «از پایین به بالا» است؛ البته «از درون به بیرون» توصیف دقیق‌تری است. کمی روی آن تأمل کنید.

> **یادداشت مترجم — توضیح تکمیلی:** قطعهٔ بالا فقط طرحی ناقص برای جابه‌جایی decoratorهاست؛ خط ... در منبع داخل بدنهٔ function تورفتگی ندارد، بنابراین این قطعه به همین صورت کد اجراییِ معتبر نیست و IndentationError می‌دهد. منظور نویسنده این است که بدنهٔ مثال قبلی را نگه دارید و فقط ترتیب دو decorator را عوض کنید. در زمان تعریف، decorator نزدیک‌تر به def زودتر اعمال می‌شود؛ در ترتیب اصلی، حاصل strong(uppercase(an_output)) است. هنگام فراخوانی، ابتدا wrapper بیرونی وارد می‌شود و سپس wrapper داخلی را فرا می‌خواند؛ پس «پایین به بالا» را نباید ترتیب عمومیِ ورود به wrapperها هنگام فراخوانی دانست. در ترتیب جابه‌جاشده، uppercase نتیجهٔ strong را می‌گیرد و در نتیجه نام tagهای HTML را هم به حروف بزرگ تبدیل می‌کند. این جابه‌جایی در این نوبت آزمایش نشده است.

### اعمال decorator به functionهای دارای parameter

تا اینجا functionهایی که برایشان decorator به کار برده‌ایم، parameter نداشته‌اند: an_output و پیش از آن a_func.

اگر function دارای parameter باشد چه؟ داخل خودِ decorator باید چه بنویسیم؟

اینجاست که قدرت `*args` و `**kwargs` در Python آشکار می‌شود. کسانی که قبلاً از ترس زحمت، با خواندن دقیق و چندباره بر این مبحثِ «یک ستاره، دو ستاره، و دیگر سرگیجه!» مسلط نشده‌اند، حالا احتمالاً به مشکل می‌خورند…

خودِ decorator function را این‌طور می‌نویسیم:

```python
def a_decorator(func):
    def wrapper(*args, **kwargs):
        return original_result
    # ...
    return wrapper
```

در اینجا (`*args`, `**kwargs`) بسیار قدرتمند است و می‌تواند تمام argumentهایی را که به function داده می‌شوند بپذیرد. دقیق‌تر بگوییم، `*args` همهٔ positional argumentهای ورودی و `**kwargs` همهٔ keyword argumentهای ورودی را دریافت و مدیریت می‌کند.

> **یادداشت مترجم — توضیح تکمیلی:** در تعریف wrapper، args یک tuple از positional argumentها و kwargs یک dict از keyword argumentها می‌گیرد. برای رساندنشان به function اصلی باید هنگام فراخوانی، آن‌ها را مانند func(`*args`, `**kwargs`) باز کنید؛ این کار در مثال trace پایین‌تر آمده است. قطعهٔ بالا فقط اسکلتِ ناقص است: original_result در آن تعریف نشده و func هم فراخوانی نمی‌شود. در محیطی که این نام در scope قابل دسترس تعریف نشده باشد، فراخوانی wrapper به NameError می‌رسد. پس آن را یک decorator کامل و آمادهٔ استفاده ندانید. منبع: [تعریف function و parameterها](https://docs.python.org/3/reference/compound_stmts.html#function-definitions).

فرض کنید چنین functionای داریم:

```python
def say_hi(greeting, name=None):
    return greeting + '! ' + name + '.'

print(say_hi('Hello', 'Jack'))
```

    Hello! Jack.

> **یادداشت مترجم — توضیح تکمیلی:** مقدار پیش‌فرضِ name در این کد None است، اما بدنه فرض می‌کند name یک string است. اگر name را ندهید یا صریحاً None بدهید، ترکیب string و None با + به TypeError می‌رسد؛ decoratorِ trace در مثال بعد هم این مشکل را برطرف نمی‌کند. فراخوانی‌های ثبت‌شدهٔ منبع، stringِ 'Jack' را می‌دهند و با این مشکل روبه‌رو نیستند. منبع: [عملیات نوع‌های sequence](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations).

اگر بخواهیم در decorator با نام function و argumentهای آن هم کاری انجام دهیم چه؟ مثلاً @trace بنویسیم تا به کاربر بگوید هنگام فراخوانی یک function چه اتفاق‌هایی افتاده است…

```python
def trace(func):
    def wrapper(*args, **kwargs):
        print(f"Trace: You've called a function: {func.__name__}(),",
              f"with args: {args}; kwargs: {kwargs}")

        original_result = func(*args, **kwargs)
        print(f"Trace: {func.__name__}{args} returned: {original_result}")
        return original_result
    return wrapper

@trace
def say_hi(greeting, name=None):
    return greeting + '! ' + name + '.'

print(say_hi('Hello', name = 'Jack'))
```

    Trace: You've called a function: say_hi(), with args: ('Hello',); kwargs: {'name': 'Jack'}
    Trace: say_hi('Hello',) returned: Hello! Jack.
    Hello! Jack.

> **یادداشت مترجم — توضیح تکمیلی:** wrapperهای این فصل metadataی function اصلی، مانند `__name__` و `__doc__`، را حفظ نمی‌کنند؛ مثلاً نام بیرونیِ say_hi پس از اعمال trace به wrapper اشاره می‌کند. اینکه پیام trace هنوز نام say_hi را نشان می‌دهد، به این دلیل است که از `func.__name__` استفاده می‌کند و func به function اصلی اشاره دارد. برای حفظ metadata در کد کاربردی، معمولاً از functools.wraps روی wrapper استفاده می‌شود؛ کد منبع در اینجا تغییر نکرده است. منبع: [مستندات رسمی functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps).

با دانستن مبانی بالا، خواندن صفحهٔ Wiki با عنوان Python Decorator Library بسیار آسان‌تر می‌شود:

> https://wiki.python.org/moin/PythonDecoratorLibrary

### یادگرفتن decorator واقعاً چقدر مهم است؟

حتماً باید decorator را یاد بگیرید؛ چون خیلی‌ها بلدش نیستند.

در Oreilly.com مقاله‌ای هست با عنوان «5 reasons you need to learn to write Python decorators»؛ یعنی «۵ دلیل برای اینکه باید نوشتن decoratorهای Python را یاد بگیرید». جالب اینکه پنجمین دلیل آن این است: **پیشرفت در مسیر شغلی شما!**

> نوشتن decorator در ابتدا آسان نیست. کار خارق‌العاده و دور از دسترسی هم نیست، اما یادگرفتن آن و درک عمیق ریزه‌کاری‌هایش آن‌قدر تلاش می‌خواهد که بسیاری از توسعه‌دهندگان هرگز زحمت مسلط‌شدن بر آن را به خود نمی‌دهند. و این به نفع شماست. وقتی در تیم خود کسی شوید که نوشتن decorator را خوب یاد گرفته و decoratorهایی می‌نویسد که مسئله‌های واقعی را حل می‌کنند، توسعه‌دهندگان دیگر از آن‌ها استفاده خواهند کرد. چون وقتی کار دشوارِ نوشتنشان انجام شد، استفاده از decoratorها بسیار آسان است. این می‌تواند تأثیر مثبت کدی را که می‌نویسید، به‌شدت چند برابر کند؛ حتی شاید از شما یک قهرمان بسازد.
>
> در سفرهایی که به جاهای دور و نزدیک داشته‌ام و طی آن‌ها به صدها مهندس نرم‌افزارِ شاغل آموزش داده‌ام چطور مؤثرتر از Python استفاده کنند، تیم‌ها همواره گفته‌اند که نوشتن decorator یکی از ارزشمندترین و مهم‌ترین ابزارهایی بوده که در کارگاه‌های برنامه‌نویسی پیشرفتهٔ Python من آموخته‌اند.

> **یادداشت مترجم — توضیح تکمیلی:** دو بند بالا ترجمهٔ کامل نقل‌قول انگلیسیِ پایانیِ منبع‌اند و به مقالهٔ «5 reasons you need to learn to write Python decorators» در O’Reilly نسبت داده شده‌اند، نه به تجربهٔ شخصی مترجم. متن اصلیِ این فصل برای مقاله URL یا نام نویسندهٔ مقاله را ذکر نکرده است؛ انتساب و عنوان موجود حفظ شده‌اند و اطلاعات کتاب‌شناختیِ تأییدنشده‌ای به آن‌ها افزوده نشده است.

چرا این‌همه آدم نمی‌توانند آن را یاد بگیرند؟ فقط به این دلیل که پیش از رسیدن به اینجا، وقتی با `*args` و `**kwargs` روبه‌رو شدند، گفتند «یک ستاره، دو ستاره، و دیگر سرگیجه!»… و بعد هم کمی بیشتر برای فهمیدنش تلاش نکردند.


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: class — پیاده‌سازی در Python](Part.3.B.2.classes-2.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: Regular Expression](Part.3.B.4.regex.md)

</div>

<!-- reading-navigation:end -->
