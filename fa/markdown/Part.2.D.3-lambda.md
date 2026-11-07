<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: دربارهٔ parameterها و argumentها (بخش دوم)](Part.2.D.2-aargs.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: functionهای دارای recursion](Part.2.D.4-recursion.md)

</div>

<!-- reading-navigation:end -->


# نام دیگر و function بی‌نام

## alias؛ نامی دیگر برای همان function

در Python می‌توان برای یک function یک **alias**، یعنی نامی دیگر، در نظر گرفت.

در کد زیر ابتدا functionی به نام `_is_leap` تعریف می‌کنیم و سپس نام دیگری برای آن می‌گذاریم:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year_leap_bool = _is_leap
year_leap_bool              #<function __main__._is_leap(year)>
year_leap_bool(800)         # _is_leap(800) -> True

id(year_leap_bool)          # id() 这个函数可以查询某对象的内存地址
id(_is_leap)                # year_leap_bool 和 _is_leap 其实保存在同一个地址中，也就是说，它们是同一个对象。

type(year_leap_bool)
type(_is_leap)              # 它们都是 function
```

    <function __main__._is_leap(year)>

    True

    4547071648

    4547071648

    function

    function

می‌بینیم که نشانی حافظهٔ نشان‌داده‌شده با `id(year_leap_bool)` و `id(_is_leap)` یکسان است: هر دو همان یک object هستند و هر دو function هستند. بنابراین وقتی می‌نویسید `year_leap_bool = _is_leap`، در واقع نام دیگری برای functionِ `_is_leap()` تعیین کرده‌اید.

> **یادداشت مترجم — توضیح تکمیلی:** object موجودیتی در برنامه است که هویت، نوع و مقدار دارد. id هویت object را به‌صورت یک عدد صحیح نشان می‌دهد؛ این عدد در طول عمر آن object ثابت و یکتا است. برابر بودن آن با نشانی حافظه، جزئیات پیاده‌سازی CPython است و تضمین عمومی همهٔ پیاده‌سازی‌های Python نیست. عددهای ثبت‌شدهٔ بالا هم ممکن است در اجرای شما متفاوت باشند. commentهای چینی مثال می‌گویند که دو نام به یک object اشاره دارند و نوع هر دو function است؛ تعبیر «نشانی حافظه» در آن‌ها با همین محدودیت باید خوانده شود. منابع: [مستندات رسمی id](https://docs.python.org/3/library/functions.html#id) و [مدل دادهٔ Python](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types).

در چه موقعیت‌هایی باید برای function یک alias بگذاریم؟

در هر پروژه، نام‌گذاری functionها و variableها کاری ساده است، اما آسان نیست! ممکن است نام‌ها تکراری شوند، هرچند تا حد امکان با جدا کردن scopeها از این مشکل جلوگیری کرده باشیم؛ یا نام مبهم باشد و کسی را که بعداً کد را می‌خواند گیج کند…

بنابراین، کوتاه‌تر کردن نام یک function صرفاً برای چند بار کمتر فشار دادن کلیدهای صفحه‌کلید، در واقع فکر خوبی نیست و عادت خوبی هم نیست. به‌ویژه حالا که ویرایشگرها از تکمیل خودکار و ویرایش با چند cursor پشتیبانی می‌کنند، طولانی بودن نام variable دیگر زحمتی ایجاد نمی‌کند.

در بیشتر موارد، هدف از انتخاب alias برای function باید افزایش خوانایی کد باشد؛ چیزی که هم برای خودتان مهم است و هم برای دیگران.

## lambda

برای نوشتن یک function بسیار کوتاه می‌توان از keywordِ `lambda` استفاده کرد.

نمونهٔ زیر functionی است که با keywordِ `def` نوشته شده است:

```python
def add(x, y):
    return x + y
add(3, 5)
```

    8

و این هم نوشتن function با keywordِ `lambda`:

```python
add = lambda x, y: x + y
add(3, 5)
```

    8

ساختار syntaxِ lambda چنین است:

> `lambda_expr ::= "lambda" [parameter_list] ":" expression`

در بالا از نمادگذاری BNF استفاده شده است. البته فعلاً با BNF آشنا نیستید؛ اگر ابهامی دارید، درگیر آن نشوید.

به‌هرحال، نمونه‌اش را دیده‌اید:

```python
lambda x, y: x + y
```

ابتدا keywordِ `lambda` را می‌نویسیم. پس از آن دو بخش داریم: پیش از `:`، parameterها می‌آیند و پس از آن یک expression. مقدار همین expression، مقدار بازگشتی function خواهد بود.

> **توجه:** در lambda، پس از `:` باید دقیقاً یک expression وجود داشته باشد؛ نه بیشتر.

این function نامی ندارد؛ به همین دلیل به آن «function بی‌نام» یا anonymous function می‌گویند.

`add = lambda x, y: x + y`

در واقع مانند این است که برای یک function بی‌نام، نامی بگذارید.

> **یادداشت مترجم — توضیح تکمیلی:** expression بخشی از کد است که ارزیابی می‌شود و یک مقدار می‌دهد؛ مثلاً جمع دو عدد. lambda خودش یک expression است که یک function می‌سازد؛ بدنهٔ آن هم فقط یک expression است، نه مجموعه‌ای از دستورها. هرچند نسبت دادن lambda به یک نام مانند مثال بالا مجاز است، PEP 8 برای این حالت معمولاً تعریف با def را توصیه می‌کند. منابع: [مرجع رسمی lambda](https://docs.python.org/3/reference/expressions.html#lambda) و [توصیهٔ PEP 8](https://peps.python.org/pep-0008/#programming-recommendations).

## کاربردهای lambda

این function بی‌نامِ lambda چه کاربردی دارد؟

### به‌عنوان مقدار بازگشتی یک function

نخستین کاربرد رایج این است که *مقدار بازگشتی یک function دیگر باشد*.

یکی از مثال‌های [The Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) را ببینیم:

```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)
```

    42

    43

این مثال در نگاه اول گیج‌کننده است. اول ببینیم پس از `f = make_incrementor(42)`، خودِ `f` دقیقاً چیست:

```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f

id(make_incrementor)
id(f)
```

    <function __main__.make_incrementor.<locals>.<lambda>(x)>

    4428443296

    4428726888

نخست دقت کنید که `f`، aliasِ functionِ `make_incrementor()` نیست. اگر می‌خواستیم برای این function یک alias بگذاریم، باید می‌نوشتیم:

```python
f = make_incrementor
```

پس `f` چیست؟ این است: `<function __main__.make_incrementor.<locals>.<lambda>(x)>`.

> * دستور `f = make_incrementor(42)` مقدار بازگشتیِ `make_incrementor(42)` را در variableِ `f` نگه می‌دارد.
> * functionِ `make_incrementor()` پس از دریافت argumentِ `42`، یک function برمی‌گرداند: `lambda x: x + 42`.
> * بنابراین functionی که در `f` نگه داشته شده، `lambda x: x + 42` است.
> * در نتیجه، `f(0)` مقدار `0` را به این function بی‌نام می‌دهد و آن هم `0 + 42` را برمی‌گرداند.

> **یادداشت مترجم — توضیح تکمیلی:** نوشتن عدد 42 در lambda در توضیح بالا برای نشان دادن رفتار آن است؛ کد واقعاً به این شکل بازنویسی نمی‌شود. functionِ ساخته‌شده دسترسی به n در محیطِ تعریف خود را حفظ می‌کند؛ به این سازوکار closure می‌گویند. برای این مثال کافی است بدانید functionِ برگردانده‌شده هنوز می‌تواند از مقدار 42 استفاده کند، حتی پس از پایان فراخوانی make_incrementor. منبع: [مثال lambda در آموزش رسمی](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions).

### به‌عنوان argument یک function

برای مثال می‌توان از بعضی built-in functionها استفاده کرد که یک function را به‌عنوان argument می‌پذیرند؛ مانند [`map()`](https://docs.python.org/3/library/functions.html#map).

> `map`(*function*, *iterable*, *...*)
>
> یک iterator برمی‌گرداند که function را روی هر عضو iterable اعمال می‌کند و نتیجه‌ها را یکی‌یکی ارائه می‌دهد. اگر argumentهای iterable بیشتری داده شود، function باید به همان تعداد argument بپذیرد و به‌طور هم‌زمان روی عضوهای متناظرِ همهٔ iterableها اعمال می‌شود. در صورت وجود چند iterable، iterator وقتی متوقف می‌شود که کوتاه‌ترین iterable تمام شود. اگر ورودی‌های function از قبل در tupleهای argumentها چیده شده‌اند، [`itertools.starmap()`](https://docs.python.org/3/library/itertools.html#itertools.starmap) را ببینید.

نخستین argumentِ `map()` برای دریافت یک function است. argumentهای بعدی `iterable` هستند؛ یعنی objectهایی که می‌توان آن‌ها را پیمایش کرد، مانند containerهای مختلف: list، tuple، dictionary و مانند آن‌ها.

> **یادداشت مترجم — توضیح تکمیلی:** iterator نتیجه‌ها را هنگام درخواست، یکی‌یکی در اختیار می‌گذارد؛ خودِ خروجی map یک list آماده نیست. در مثال‌های زیر، list نتیجه‌ها را دریافت می‌کند و در یک list جمع می‌کند. منبع: [مستندات رسمی map](https://docs.python.org/3/library/functions.html#map).

```python
def double_it(n):
    return n * 2

a_list = [1, 2, 3, 4, 5, 6]

b_list = list(map(double_it, a_list))
b_list

c_list = list(map(lambda x: x * 2, a_list))
c_list
```

    [2, 4, 6, 8, 10, 12]

    [2, 4, 6, 8, 10, 12]

پیداست که استفاده از `lambda` کوتاه‌تر است. همچنین functionهایی که مانند `double_it(n)` کار ساده‌ای انجام می‌دهند، اغلب فقط برای همان یک بار استفاده لازم‌اند.

```python
phonebook = [
    {
        'name': 'john',
        'phone': 9876
    },
    {
        'name': 'mike',
        'phone': 5603
    },
    {
        'name': 'stan',
        'phone': 6898
    },
    {
        'name': 'eric',
        'phone': 7898
    }
]

phonebook
list(map(lambda x: x['name'], phonebook))
list(map(lambda x: x['phone'], phonebook))
```

    [{'name': 'john', 'phone': 9876},
     {'name': 'mike', 'phone': 5603},
     {'name': 'stan', 'phone': 6898},
     {'name': 'eric', 'phone': 7898}]

    ['john', 'mike', 'stan', 'eric']

    [9876, 5603, 6898, 7898]

می‌توان چند iterable به map() داد:

```python
a_list = [1, 3, 5]
b_list = [2, 4, 6]

list(map(lambda x, y: x * y, a_list, b_list))
```

    [2, 12, 30]

وقتی همهٔ مثال‌های بالا را فهمیدید، با دیدن مثالِ [The Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) دیگر ابهامی نخواهید داشت:

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])
pairs
```

    [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

> **یادداشت مترجم — توضیح تکمیلی:** در مثال آخر، key یک function می‌گیرد که معیار مرتب‌سازی هر عضو را تولید می‌کند. lambda از هر tuple، عضو دوم، یعنی واژهٔ انگلیسی، را برمی‌گرداند؛ بنابراین مرتب‌سازی بر اساس آن واژه‌هاست، نه عددهای اول. منبع: [راهنمای رسمی مرتب‌سازی Python](https://docs.python.org/3/howto/sorting.html#key-functions).


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: دربارهٔ parameterها و argumentها (بخش دوم)](Part.2.D.2-aargs.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: functionهای دارای recursion](Part.2.D.4-recursion.md)

</div>

<!-- reading-navigation:end -->
