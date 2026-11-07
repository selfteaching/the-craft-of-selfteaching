<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: درگاه ورود](Part.1.E.1.entrance.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: Control flow](Part.1.E.3.controlflow.md)

</div>

<!-- reading-navigation:end -->


# مقدارها و عملیات متناظر با آن‌ها

از نظر ساختاری، همهٔ برنامه‌های کامپیوتری از دو جزء بنیادی، و فقط همین دو جزء، ساخته شده‌اند:

> * **Evaluation**؛ محاسبه و به دست آوردن مقدار
> * **Control flow**؛ تعیین مسیر اجرای برنامه

دستگاهی که control flow ندارد صرفاً ماشین‌حساب است؛ دستگاهی با control flow است که programmable می‌شود.

به برنامهٔ تشخیص عدد اول که قبلاً دیده‌ایم نگاه کنید. در Notebook، با زدن `⎋`، یعنی `ESC`، مطمئن شوید در command mode هستید؛ سپس `⇧ L` نمایش شمارهٔ خط‌ها را روشن یا خاموش می‌کند.

```python
def is_prime(n):            # 定义 is_prime()，接收一个参数
    if n < 2:              # 开始使用接收到的那个参数（值）开始计算……
        return False       # 不再是返回给人，而是返回给调用它的代码……
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

for i in range(80, 110):
    if is_prime(i):          # 调用 is_prime() 函数，
        print(i)            # 如果返回值为 True，则向屏幕输出 i
```

    83
    89
    97
    101
    103
    107
    109

`if...` و `for...`، control flow را تعیین می‌کنند: در چه شرایطی چه محاسبه‌ای انجام شود و در چه شرایطی کدام محاسبه تکرار شود.

call کردن functionِ `is_prime()` در خط ۱۳ هم control flow را تغییر می‌دهد؛ برای همین می‌توانیم **function را یک subprogram در نظر بگیریم**.

به‌محض call شدن این function، اجرا به کد درون `is_prime()` می‌رود که در خط ۱ تعریف شده است. درون آن باز هم محاسبه و control flow داریم که یک return value از نوع Boolean تعیین می‌کنند. سپس اجرا به خط ۱۳ برمی‌گردد؛ مقدار برگشتی در اختیار `if` قرار می‌گیرد تا مشخص شود خط ۱۴ اجرا بشود یا نه…

کامپیوتر، به‌عنوان دستگاهی programmable، به این دلیل می‌تواند control flow داشته باشد که **Boolean operations** انجام می‌دهد؛ یعنی روی Boolean valueها کار می‌کند و سپس آن‌ها را به statementهای branch و loop می‌دهد تا control flow برنامه شکل بگیرد.

## مقدار

بیشتر statementهای برنامه، در اصل، شامل **evaluation** هستند؛ یعنی مقدار چیزی را به دست می‌آورند. در اینجا منظور از «ارزیابی»، قضاوت دربارهٔ خوب یا بد بودن کسی یا چیزی نیست؛ منظور این است که «حساب کنیم مقدار دقیقاً چیست». به همین دلیل، نویسنده در متن چینی، واژه‌ای به معنای «محاسبه» را برای ترجمهٔ evaluation دقیق‌تر می‌داند.

در برنامه، چیزهایی که روی آن‌ها محاسبه انجام می‌شود به **literal** و **variable** تقسیم می‌شوند.

```python
a = 1 + 2 * 3
a += 1
print(a)
```

در کد بالا:

`1`، `2` و `3` همگی **literal** هستند. معنای literal «لفظی» است؛ مقدار آن همان چیزی است که مستقیماً نوشته شده است. مقدار `1` همان `1` است.

`a` یک **variable** است؛ یعنی مقدارش می‌تواند تغییر کند. برای نمونه، در statement دوم، مقدار آن از `7` به `8` تغییر می‌کند.

در statement اول، `+` و `*`، **operator** هستند: روی مقدارهای دو طرفشان عملیات مشخصی انجام می‌دهند و مقدار تازه‌ای به دست می‌آورند. ابتدا `*` روی `2` و `3` کار می‌کند و `6` به دست می‌آید؛ سپس `+` روی `1` و `6` کار می‌کند و `7` به دست می‌آید. اینکه ضرب و تقسیم پیش از جمع و تفریق انجام می‌شوند، به **operator precedence**، یعنی تقدم operatorها، بستگی دارد.

`=` نماد assignment است؛ مقدار سمت راستش را در variable سمت چپ قرار می‌دهد.

*مقدارها* اجزای سازندهٔ برنامه‌اند؛ مثل آجرهای ساختمان. ساختمان هر شکلی داشته باشد، در نهایت عمدتاً از آجر ساخته شده است.

هر *literal* طبعاً مقداری دارد؛ همان مقداری که در نوشتارش بیان شده است.

به *variable* باید پیش از استفاده مقدار بدهید؛ یعنی ابتدا مقداری در آن قرار دهید تا بعد بتوان در محاسبه از آن استفاده کرد.

در Python، هر function یک *return value* دارد. حتی اگر هنگام تعریف function مقدار برگشتی تعیین نکنید، مقدار پیش‌فرض `None` برگردانده می‌شود… به بزرگی و کوچکی حروف `None` توجه کنید!

```python
def f():
    pass
print(f())        # 输出 f() 这个函数被调用后的返回值，None
print(print(f())) # 这一行最外围的 print() 调用了一次 print(f())，所以输出一个 None，
                  # 而后再输出这次调用的返回值，所以又输出一次 None
```

    None
    None
    None

وقتی functionای را call می‌کنیم، در اصل چنین کاری انجام می‌دهیم:

> مقداری را به function می‌دهیم تا با محاسبه‌ها و control flow داخلی‌اش روی آن کار کند و سپس مقدار دیگری برگرداند.

مثلاً `abs()` قدرمطلقِ مقدار ورودی را برمی‌گرداند؛ `int()` بخش اعشاریِ مقدار داده‌شده را حذف می‌کند؛ و `float()` وقتی یک integer بگیرد، شکل float آن را برمی‌گرداند:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

abs(-3.14159)
int(abs(-3.14159))
float(int(abs(-3.14159)))
```

    3.14159
    3
    3.0

## نوع مقدارها

زبان‌های برنامه‌نویسی همواره این سه نوع پایهٔ داده را دارند:

> * Boolean value
> * number: شامل integer یا `int`، عدد دارای بخش اعشاری یا `float`، و عدد مختلط یا `complex`
> * string: دنباله‌ای از نویسه‌ها

وقتی داده‌ها نوع‌های متفاوتی دارند، مقدارهایشان هم از نوع‌های متفاوت‌اند.

قاعدهٔ معمول در محاسبه این است که عموماً *مقدارهای هم‌نوع باید با هم وارد عملیات شوند*.

روشن است که محاسبه با دو عدد معنی دارد، اما نمی‌توانید از operatorِ `+` بخواهید یک string و یک عدد را با هم جمع کند:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

11 + 10 - 9 * 8 / 7 // 6 % 5
'3.14' + 3                  # 这一句会报错
```

    20.0
    
    ---------------------------------------------------------------------------
    
    TypeError                                 Traceback (most recent call last)
    
    <ipython-input-18-e922b7565e53> in <module>
          3
          4 11 + 10 - 9 * 8 / 7 // 6 % 5
    ----> 5 '3.14' + 3                  # 这一句会报错
    
    TypeError: can only concatenate str (not "int") to str

بنابراین، وقتی ناچاریم روی مقدارهای با نوع متفاوت عملیات انجام دهیم، ابتدا **type casting** انجام می‌دهیم؛ یعنی نوع مقدار را تبدیل می‌کنیم. برای نمونه:

> * برای تبدیل string به عدد از `int()` یا `float()` استفاده می‌کنیم.
> * برای تبدیل عدد به string از `str()` استفاده می‌کنیم.

حتی در محاسبهٔ عددی هم گاهی لازم است integer را به float تبدیل کنیم یا برعکس:

> * برای تبدیل integer به float از `float()` استفاده می‌کنیم.
> * برای تبدیل float به integer از `int()` استفاده می‌کنیم.

> **یادداشت مترجم — توضیح تکمیلی:** هم‌نوع بودن شرط مطلق همهٔ عملیات نیست؛ مثلاً Python محاسبهٔ ترکیبیِ `int` و `float` را پشتیبانی می‌کند. در تبدیل float با `int()`، بخش اعشاری به سمت صفر حذف می‌شود، نه با گرد کردن به نزدیک‌ترین عدد. [مستندات رسمی](https://docs.python.org/3/library/functions.html#int).

functionِ `type()` برای دیدن نوع یک مقدار به کار می‌رود:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

type(3)
type(3.0)
type('3.14')
type(True)
type(range(10))
type([1,2,3])
type((1,2,3))
type({1,2,3})
type({'a':1, 'b':2, 'c':3})
```

    int
    float
    str
    bool
    range
    list
    tuple
    set
    dict

## Operatorها

نوع‌های مختلف داده، **operator**های متناسب با خود را دارند.

### Numeric operators

operatorهای محاسبه با عددها، جمع، تفریق، ضرب، تقسیم، تقسیم با گرد کردن به پایین، باقی‌مانده و توان هستند: `+`، `-`، `*`، `/`، `//`، `%` و `**`.

از این میان، `+` و `-` می‌توانند روی یک مقدار هم کار کنند؛ مثل `-3`. بقیه برای انجام عملیات به دو مقدار نیاز دارند.

ترتیب تقدم این operatorها چنین است:

> * کمترین تقدم متعلق به `+` و `-` با دو operand است.
> * پس از آن‌ها `*`، `/`، `//` و `%` قرار می‌گیرند.
> * سپس `+` و `-` با یک operand قرار دارند.
> * بیشترین تقدم متعلق به `**` است.

فهرست کامل تقدم operatorها در مستندات رسمی آمده است:

> https://docs.python.org/3/reference/expressions.html#operator-precedence

> **یادداشت مترجم — توضیح تکمیلی:** رابطهٔ توان و علامت یک‌ورودی ظرافتی دارد: توان نسبت به علامت سمت چپ تقدم دارد، اما علامت سمت راست را می‌پذیرد؛ بنابراین `-2**2` برابر `-4` و `2**-2` برابر `0.25` است. [مرجع رسمی توان](https://docs.python.org/3/reference/expressions.html#the-power-operator).

### Boolean operators

برای Boolean valueها سه operator «و»، «یا» و «نقیض» را داریم: `and`، `or` و `not`.

کمترین تقدم متعلق به `or` است، سپس `and` قرار می‌گیرد و بیشترین تقدم متعلق به `not` است:

```python
True and False or not True
```

    False

ابتدا `not` اجرا می‌شود، چون بیشترین تقدم را دارد. پس عبارت بالا معادل `True and False or (not True)`، و در نتیجه معادل `True and False or False` است.

سپس نوبت `and` است؛ بنابراین `True and False or False` معادل `(True and False) or False`، یعنی `False or False` می‌شود.

در نتیجه مقدار نهایی `False` است.

### Logical operators

میان عددها می‌توان از logical operatorها هم استفاده کرد؛ مثلاً `1 > 2` مقدار Booleanِ `False` را برمی‌گرداند. این operatorها عبارت‌اند از: `<` برای کوچک‌تر بودن، `<=` برای کوچک‌تر یا مساوی بودن، `>` برای بزرگ‌تر بودن، `>=` برای بزرگ‌تر یا مساوی بودن، `!=` برای نابرابری و `==` برای برابری.

تقدم آن‌ها از Boolean operatorها بیشتر و از numeric operatorها کمتر است. یعنی ابتدا محاسبه‌های عددی، سپس مقایسه‌ها و در آخر Boolean operations انجام می‌شوند.

```python
n = -95
n < 0 and (n + 1) % 2 == 0
```

    True

### String operators

برای string سه دسته عملیات داریم:

> * اتصال: `+` و `' '`؛ منظور از مورد دوم، فاصله است.
> * تکرار: `*`
> * عملیات منطقی: `in` و `not in`؛ همچنین `<`، `<=`، `>`، `>=`، `!=` و `==`

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

'Awesome' + 'Python'
'Awesome' 'Python'
'Python, ' + 'Awesome! ' * 3
'o' in 'Awesome' and 'o' not in 'Python'
```

    'AwesomePython'
    'AwesomePython'
    'Python, Awesome! Awesome! Awesome! '
    False

> **یادداشت مترجم — توضیح تکمیلی:** فاصله خودش operator اتصال نیست؛ دو string literal مجاور، مانند خط دوم مثال، خودکار به هم متصل می‌شوند. این قاعده برای دو variable یا دو expression دلخواه برقرار نیست. [مرجع رسمی اتصال literalها](https://docs.python.org/3/reference/lexical_analysis.html#string-literal-concatenation).

نویسه‌ها و stringها را، علاوه بر `==` و `!=`، می‌توان با `<`، `<=`، `>` و `>=` هم مقایسه کرد:

```python
'a' < 'b'
```

    True

چون هر نویسه یک کد Unicode متناظر دارد و هنگام مقایسهٔ نویسه‌ها، در واقع این کدها مقایسه می‌شوند.

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

'A' > 'a'
ord('A')
ord('a')
```

    False
    65
    97

وقتی دو string مقایسه می‌شوند، مقایسه از نخستین نویسهٔ هر دو شروع می‌شود و به‌ترتیب پیش می‌رود؛ «به‌محض مشخص شدن نتیجه، متوقف می‌شود»:

```python
'PYTHON' > 'Python 3'
```

    False

### List operators

عددها و stringها، که دنباله‌ای از نویسه‌ها هستند، نوع‌های پایهٔ داده‌اند. اما اغلب می‌خواهیم تعداد زیادی عدد و string را یکجا پردازش کنیم و آن وقت به **array** نیاز پیدا می‌کنیم. Python مفهوم **container** را در اختیارمان می‌گذارد؛ چیزی که چندین داده را در خود نگه می‌دارد.

Python انواع مختلفی از container دارد. خود string هم نوعی container است که چندین نویسه را در خود جا می‌دهد.

فعلاً به‌شکلی مقدماتی با container دیگری آشنا می‌شویم: **list**.

list با براکت `[]` مشخص می‌شود. مثلاً `[1, 2, 3, 4, 5]`، `['ann', 'bob', 'cindy', 'dude', 'eric']` و حتی `['a', 2, 'b', 32, 22, 12]` همگی list هستند.

چون list هم مانند string یک *ordered container* است، یعنی ترتیب عناصرش اهمیت دارد ــ در مقابل containerهای بدون ترتیب ــ operatorهای قابل استفاده برایشان یکسان‌اند:

> * اتصال: `+` و `' '`؛ منظور از مورد دوم، فاصله است.
> * تکرار: `*`
> * عملیات منطقی: `in` و `not in`؛ همچنین `<`، `<=`، `>`، `>=`، `!=` و `==`

> **یادداشت مترجم — توضیح تکمیلی:** در این فهرستِ متن اصلی خطایی وجود دارد: فاصله، listها را به هم متصل نمی‌کند؛ برای اتصال دو list از `+` استفاده می‌شود. قاعدهٔ string literalهای مجاور به list تعمیم پیدا نمی‌کند. [عملیات مشترک sequenceها](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations).

هنگام مقایسهٔ دو list، با فرض یکسان بودن نوع عناصرشان، همان قاعدهٔ مقایسهٔ string برقرار است: «به‌محض مشخص شدن نتیجه، متوقف شو». البته چون list می‌تواند عناصر با نوع‌های مختلف داشته باشد، معمولاً نیاز عملی چندانی به مقایسهٔ «بزرگ‌تر و کوچک‌تر» میان آن‌ها نداریم. تفاوت نوع‌ها هنگام مقایسه ممکن است `TypeError` ایجاد کند…

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

a_list = [1, 2, 3, 4, 5]
b_list = [1, 2, 3, 5]
c_list = ['ann', 'bob', 'cindy', 'dude', 'eric']
a_list > b_list
10 not in a_list
'ann' in c_list
```

    False
    True
    True

## محاسبه‌های پیچیده‌تر

جمع، تفریق، ضرب، تقسیم، تقسیم با گرد کردن به پایین، باقی‌مانده و توان روی عددها؛ اتصال، تکرار و بررسی عضویت برای stringها؛ و «یا»، «و» و «نقیض» برای Boolean valueها، همگی عملیات نسبتاً ساده‌اند.

کارهای کمی پیچیده‌تر را با call کردن function انجام می‌دهیم؛ چون داخل function می‌توانیم برنامه‌ای پیچیده‌تر از «یک expression» بنویسیم که روی argument دریافتی کار کند. به بیان دیگر، functionها شبیه subprogramهای ازپیش‌نوشته‌شده‌اند: مقداری به آن‌ها می‌دهید، روی آن محاسبه می‌کنند و مقداری برمی‌گردانند؛ دست‌کم `None`.

جدول زیر همهٔ [built-in function](https://docs.python.org/3/library/functions.html)های Python را نشان می‌دهد:

| ( | Python | Built-in  |  Functions   |  )  |
| --- | --- | --- | --- | --- |
| [abs()](https://docs.python.org/3/library/functions.html#abs) | [delattr()](https://docs.python.org/3/library/functions.html#delattr) | [hash()](https://docs.python.org/3/library/functions.html#hash) | [memoryview()](https://docs.python.org/3/library/functions.html#func-memoryview) | [set()](https://docs.python.org/3/library/functions.html#func-set) |
| [all()](https://docs.python.org/3/library/functions.html#all) | [dict()](https://docs.python.org/3/library/functions.html#func-dict) | [help()](https://docs.python.org/3/library/functions.html#help) | [min()](https://docs.python.org/3/library/functions.html#min) | [setattr()](https://docs.python.org/3/library/functions.html#setattr) |
| [any()](https://docs.python.org/3/library/functions.html#any) | [dir()](https://docs.python.org/3/library/functions.html#dir) | [hex()](https://docs.python.org/3/library/functions.html#hex) | [next()](https://docs.python.org/3/library/functions.html#next) | [slice()](https://docs.python.org/3/library/functions.html#slice) |
| [ascii()](https://docs.python.org/3/library/functions.html#ascii) | [divmod()](https://docs.python.org/3/library/functions.html#divmod) | [id()](https://docs.python.org/3/library/functions.html#id) | [object()](https://docs.python.org/3/library/functions.html#object) | [sorted()](https://docs.python.org/3/library/functions.html#sorted) |
| [bin()](https://docs.python.org/3/library/functions.html#bin) | [enumerate()](https://docs.python.org/3/library/functions.html#enumerate) | [input()](https://docs.python.org/3/library/functions.html#input) | [oct()](https://docs.python.org/3/library/functions.html#oct) | [staticmethod()](https://docs.python.org/3/library/functions.html#staticmethod) |
| [bool()](https://docs.python.org/3/library/functions.html#bool) | [eval()](https://docs.python.org/3/library/functions.html#eval) | [int()](https://docs.python.org/3/library/functions.html#int) | [open()](https://docs.python.org/3/library/functions.html#open) | [str()](https://docs.python.org/3/library/functions.html#func-str) |
| [breakpoint()](https://docs.python.org/3/library/functions.html#breakpoint) | [exec()](https://docs.python.org/3/library/functions.html#exec) | [isinstance()](https://docs.python.org/3/library/functions.html#isinstance) | [ord()](https://docs.python.org/3/library/functions.html#ord) | [sum()](https://docs.python.org/3/library/functions.html#sum) |
| [bytearray()](https://docs.python.org/3/library/functions.html#func-bytearray) | [filter()](https://docs.python.org/3/library/functions.html#filter) | [issubclass()](https://docs.python.org/3/library/functions.html#issubclass) | [pow()](https://docs.python.org/3/library/functions.html#pow) | [super()](https://docs.python.org/3/library/functions.html#super) |
| [bytes()](https://docs.python.org/3/library/functions.html#func-bytes) | [float()](https://docs.python.org/3/library/functions.html#float) | [iter()](https://docs.python.org/3/library/functions.html#iter) | [print()](https://docs.python.org/3/library/functions.html#print) | [tuple()](https://docs.python.org/3/library/functions.html#func-tuple) |
| [callable()](https://docs.python.org/3/library/functions.html#callable) | [format()](https://docs.python.org/3/library/functions.html#format) | [len()](https://docs.python.org/3/library/functions.html#len) | [property()](https://docs.python.org/3/library/functions.html#property) | [type()](https://docs.python.org/3/library/functions.html#type) |
| [chr()](https://docs.python.org/3/library/functions.html#chr) | [frozenset()](https://docs.python.org/3/library/functions.html#func-frozenset) | [list()](https://docs.python.org/3/library/functions.html#func-list) | [range()](https://docs.python.org/3/library/functions.html#func-range) | [vars()](https://docs.python.org/3/library/functions.html#vars) |
| [classmethod()](https://docs.python.org/3/library/functions.html#classmethod) | [getattr()](https://docs.python.org/3/library/functions.html#getattr) | [locals()](https://docs.python.org/3/library/functions.html#locals) | [repr()](https://docs.python.org/3/library/functions.html#repr) | [zip()](https://docs.python.org/3/library/functions.html#zip) |
| [compile()](https://docs.python.org/3/library/functions.html#compile) | [globals()](https://docs.python.org/3/library/functions.html#globals) | [map()](https://docs.python.org/3/library/functions.html#map) | [reversed()](https://docs.python.org/3/library/functions.html#reversed) | [__import__()](https://docs.python.org/3/library/functions.html#__import__) |
| [complex()](https://docs.python.org/3/library/functions.html#complex) | [hasattr()](https://docs.python.org/3/library/functions.html#hasattr) | [max()](https://docs.python.org/3/library/functions.html#max) | [round()](https://docs.python.org/3/library/functions.html#round) | |

> **یادداشت مترجم — توضیح تکمیلی:** این جدول مربوط به زمان نگارش کتاب است؛ فهرست نسخهٔ فعلی Python را در همان پیوند مستندات رسمی ببینید.

لازم نیست همین حالا عجله کنید و همه را یکجا بشناسید؛ بالاخره به‌مرور یادشان می‌گیرید.

از میان آن‌ها، برای عددها، `abs()` قدرمطلق را حساب می‌کند و `divmod()` خارج‌قسمت و باقی‌مانده را به دست می‌آورد؛ و موارد دیگر.

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

abs(-3.1415926)
divmod(11, 3)
```

    3.1415926
    (3, 2)

این built-in functionها هم فقط «عملیات پایه» را انجام می‌دهند. مثلاً اگر بخواهیم برای عددها محاسبه‌های مثلثاتی انجام دهیم، کافی نیستند؛ پس باید moduleِ `math` را از **standard library** به کار بگیریم:

```python
import math
math.sin(5)
```

    -0.9589242746631385

در کد `math.sin(5)`، می‌توان `.` را هم نوعی «operator» در نظر گرفت که کارش این است:

> call کردن function از moduleهای دیگر.

کار `math.sin(5)` چنین است:

> مقدار `5` را به functionِ `sin()` در moduleِ `math` بده؛ بگذار `sin()` طبق کد داخلی‌اش روی آن محاسبه کند و یک مقدار، یعنی نتیجهٔ محاسبه، برگرداند.

functionهای تعریف‌شده در **class** را هم می‌توان به این شکل call کرد. شاید هنوز ندانید class دقیقاً چیست، اما از نظر ساختاری درک این توضیح آسان است: آن هم قطعه‌کدی است که در فایل دیگری نگهداری می‌شود و functionهای تعریف‌شده درونش را می‌توان به همین صورت call کرد.

مثلاً عددها هم به یک class تعلق دارند؛ بنابراین می‌توان function تعریف‌شده در آن class را call کرد. نمونه‌اش `float.as_integer_ratio()` است که دو مقدار برمی‌گرداند؛ تقسیم مقدار اول بر دوم دقیقاً برابر با float ورودی است:

```python
3.1415926.as_integer_ratio()
```

    (3537118815677477, 1125899906842624)

> **یادداشت مترجم — توضیح تکمیلی:** module واحدی برای سازمان‌دهی کد است. class نوعی الگو برای ساخت objectهاست و الزامی ندارد در فایل جداگانه تعریف شود. نقطه در مثال‌ها برای دسترسی به attribute به کار می‌رود؛ attribute می‌تواند function یا method باشد. `as_integer_ratio()` در این مثال methodِ خود مقدار float است. [مرجع رسمی attribute reference](https://docs.python.org/3/reference/expressions.html#attribute-references) و [این method](https://docs.python.org/3/library/stdtypes.html#float.as_integer_ratio).

## نکته‌ای تکمیلی دربارهٔ Boolean value

شاید وقتی عبارت زیر و نتیجه‌اش را ببینید کمی گیج شوید:

```python
True or 'Python'
```

    True

دلیلش این است که Python درست بودن را چنین تعریف می‌کند:

> به‌طور پیش‌فرض، یک object درست در نظر گرفته می‌شود، مگر اینکه class آن methodِ `__bool__()`ای تعریف کرده باشد که برای آن object مقدار `False` برگرداند، یا methodِ `__len__()`ای داشته باشد که صفر برگرداند.
>
> https://docs.python.org/3/library/stdtypes.html#truth-value-testing

فهم این عبارت برای تازه‌کار آسان نیست، اما بند بعدی روشن‌تر است:

> بیشتر objectهای built-in که نادرست در نظر گرفته می‌شوند عبارت‌اند از:
>
> > * مقدارهای ثابتی که نادرست تعریف شده‌اند: `None` و `False`.
> > * صفر از هر نوع عددی: `0`، `0.0`، `0j`، `Decimal(0)` و `Fraction(0, 1)`.
> > * sequenceها و collectionهای خالی: `''`، `()`، `[]`، `{}`، `set()` و `range(0)`.

پس `'Python'` یک string غیرخالی است؛ در دستهٔ sequenceهای خالی قرار نمی‌گیرد و نادرست محسوب نمی‌شود؛ در نتیجه Boolean value متناظر با آن `True` است.

حالا می‌توانیم موضوع را ساده‌تر این‌طور بفهمیم:

> هر variable یا literal، علاوه بر مقدار خودش، گویی یک Boolean value متناظر هم دارد.

> **یادداشت مترجم — توضیح تکمیلی:** نتیجهٔ مثال آغاز این بخش، دقیق‌تر، از short-circuit evaluation می‌آید: `or` اگر operand اول درست محسوب شود، همان operand را برمی‌گرداند و دومی را ارزیابی نمی‌کند. پس در این مثال حتی نیازی به بررسی `'Python'` نیست. `and` و `or` الزاماً مقدار `bool` برنمی‌گردانند؛ یکی از operandها را برمی‌گردانند. [مرجع رسمی Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not).

## نکته‌ای تکمیلی دربارهٔ نوع مقدارها

علاوه بر number، Boolean value، string و list که پیش‌تر معرفی شد، نوع‌های دیگری هم داریم؛ مثل `range()` برای دنبالهٔ حسابی، `tuple`، `set` و `dictionary`؛ و نیز نوع‌هایی برای تاریخ، که در متن اصلی Date Type نامیده شده‌اند.

این‌ها ترکیب‌های گوناگونی از نوع‌های پایه‌اند. در زندگی واقعی، اغلب به داده‌ای نیاز داریم که از ترکیب نوع‌های پایه ساخته شده باشد. مثلاً دفترچهٔ تماس، مجموعه‌ای از stringهاست که هر کدام به چند string و عدد مربوط می‌شوند.

``` python
entry[3662] = {
    'first_name': 'Michael',
    'last_name': 'Willington',
    'birth_day': '12/07/1992',
    'mobile': {
        '+714612234',
        '+716253923'
    }
    'id': 3662,
    ...
}
```

> **یادداشت مترجم — توضیح تکمیلی:** بلوک بالا طرحی از ساختار داده است، نه برنامه‌ای آمادهٔ اجرا: `entry` در اینجا تعریف نشده، پس از مجموعهٔ `mobile` یک ویرگول کم است و `...` نیز جای بخش‌های حذف‌شده را نشان می‌دهد. برای حفظ مثال اصلی، کد تغییر نکرده است.

هر نوع، operatorهای متناسب با خودش را دارد که می‌توانند روی مقدارهای آن کار کنند.

گاهی لازم است میان این نوع‌ها هم عملیات انجام دهیم. آن وقت، پیش از عملیات، باز به type casting نیاز داریم؛ مثلاً تبدیل list به set یا برعکس:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

a = [1, 2, 3, 4, 5, 6, 7]
b = set(a)
c = list(b)
a
b
c
```

    [1, 2, 3, 4, 5, 6, 7]
    {1, 2, 3, 4, 5, 6, 7}
    [1, 2, 3, 4, 5, 6, 7]

> **یادداشت مترجم — توضیح تکمیلی:** set ترتیب عناصر را تضمین نمی‌کند؛ بنابراین هنگام بازگشت به list نباید به ترتیب نشان‌داده‌شده در این خروجی تکیه کرد. set همچنین عناصر تکراری را حذف می‌کند. [مرجع رسمی set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).

## جمع‌بندی

به نقطهٔ شروع برگردیم: از نظر ساختاری، همهٔ برنامه‌های کامپیوتری از دو جزء بنیادی، و فقط همین دو جزء، ساخته شده‌اند:

> * **Evaluation**
> * **Control flow**

این فصل بیشتر جزئیات عملیات روی نوع‌های پایهٔ داده را معرفی کرد. علاوه بر آن‌ها، به نوع‌های پیچیده‌تری هم نیاز داریم که از ترکیبشان ساخته شوند. اما نوع داده هرچه باشد، چیزی که operator روی آن کار می‌کند همیشه **مقدار** آن داده است. بنابراین، هرچند بیشتر کتاب‌های برنامه‌نویسی طبق معمول از «نوع داده» صحبت می‌کنند، ما برای رسیدن به اصل موضوع روی «نوع مقدار» تمرکز کرده‌ایم. این جابه‌جاییِ تمرکز کوچک است، اما تجربه نشان داده همین تفاوت کوچک به تازه‌کارها کمک بزرگی می‌کند تا مفهوم‌ها را روشن‌تر بفهمند.

برای هر نوع *مقدار*، ساده یا پیچیده، روش‌هایی برای کار کردن با آن داریم:

> * **Operator**
>   * عملیات روی مقدارها
>   * عملیات منطقی
> * **Function**
>   * built-in functionها
>   * functionهای moduleهای دیگر
>   * functionهای تعریف‌شده در class خود آن مقدار

بنابراین، آنچه باید از اینجا به بعد یاد بگیرید چیزی جز آشنایی با انواع *داده* و عملیات متناظرشان نیست؛ از جمله operatorها و functionهایی که روی *مقدارهای* آن‌ها کار می‌کنند. چه operator و چه function، در نهایت یک **مقدار** با *Boolean value* متناظرش به دست می‌دهند. از این زاویه، ساختار دانش برنامه‌نویسی چندان پیچیده نیست. به بیان دیگر:

> از اینجا به بعد، چیزی که یاد می‌گیرید صرفاً *عملیات* روی *انواع داده* است.

هنوز فرصت نشده function را عمیق توضیح دهیم، اما در نهایت می‌بینید که درست مثل operator، در همه‌جای برنامه حضور دارد.

## یادداشت‌ها

این چند پیوند را هم اینجا می‌گذارم؛ در آینده بارها و بارها برای مراجعه به آن‌ها برمی‌گردید:

> * دربارهٔ expressionها: https://docs.python.org/3/reference/expressions.html
> * دربارهٔ تقدم همهٔ عملیات: https://docs.python.org/3/reference/expressions.html#operator-precedence
> * برای فهم پیوند قبلی، باید BNF را بشناسید: https://en.wikipedia.org/wiki/Backus-Naur_form
> * built-in functionهای Python: https://docs.python.org/3/library/functions.html
> * نوع‌های استاندارد داده در Python: https://docs.python.org/3/library/stdtypes.html

راستی، درون Python، همهٔ operatorها هم در واقع با call کردن function انجام می‌شوند…

> https://docs.python.org/3.7/library/operator.html



<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: درگاه ورود](Part.1.E.1.entrance.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: Control flow](Part.1.E.3.controlflow.md)

</div>

<!-- reading-navigation:end -->
