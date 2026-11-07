<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: مستندات function](Part.2.D.5-docstrings.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: توسعه با روش Test Driven Development](Part.2.D.7-tdd.md)

</div>

<!-- reading-navigation:end -->


# ذخیره کردن functionها در فایل

طبیعی است که بهتر است functionهایی را که نوشته‌ایم ذخیره کنیم تا در آینده هر وقت لازم شد آن‌ها را فراخوانی کنیم.

## module

می‌توانیم محتوای زیر را در فایلی به نام `mycode.py` ذخیره کنیم. چنین فایل `.py` که از بیرون قابل استفاده است، نام مشخصی دارد: **module**. بنابراین این فایل، و به همین ترتیب هر فایل `.py`، را می‌توان *module* نامید:

> **یادداشت مترجم — توضیح تکمیلی:** module روشی برای سازمان‌دهی کد و استفادهٔ دوباره از آن است. commentهای چینی ابتدای کد می‌گویند که کد این Code Cell در فایل mycode.py در پوشهٔ فعلی ذخیره شده و با دستور %load در Jupyter به cell آورده شده است. %load محتوای فایل را داخل cell می‌آورد؛ فایل را ایجاد یا ذخیره نمی‌کند. برای اجرای مثال بعدی، ابتدا فایل را با همین محتوا بسازید. منبع: [مستندات رسمی IPython دربارهٔ %load](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-load).

```python
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
    :param capitalized: Whether name should be converted to capitalized before print. False as default.
    :returns: None
    """
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')
```

سپس می‌توانیم در جای دیگری به شکل زیر از آن استفاده کنیم؛ فرض بر این است که کد بالا اکنون در فایل `mycode.py` در working directory فعلی ذخیره شده است:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import mycode

help(mycode.is_prime)
help(mycode.say_hi)

mycode.__name__
mycode.is_prime(3)
mycode.say_hi('mike', 'zoe')
```

    Help on function is_prime in module mycode:
    
    is_prime(n)
        Return a boolean value based upon
        whether the argument n is a prime number.
    
    Help on function say_hi in module mycode:
    
    say_hi(*names, greeting='Hello', capitalized=False)
        Print a string, with a greeting to everyone.
        :param *names: tuple of names to be greeted.
        :param greeting: 'Hello' as default.
        :param capitalized: Whether name should be converted to capitalzed before print. False as default.
        :returns: None
    
    'mycode'
    
    True
    
    Hello, mike!
    Hello, zoe!

نام **module** بالا، `mycode` است؛ برای توضیح بیشتر، [آموزش رسمی moduleها](https://docs.python.org/3/tutorial/modules.html) را ببینید.

> **یادداشت مترجم — توضیح تکمیلی:** در خروجی ثبت‌شده، واژهٔ capitalzed با Docstring کد بالا، که capitalized دارد، تفاوت دارد. این اختلافِ خودِ منبع حفظ شده است؛ مستندات زمان اجرا از نسخهٔ واقعاً بارگذاری‌شدهٔ module خوانده می‌شود.

## ترتیب جست‌وجوی پوشه‌ها برای یافتن module

وقتی به Python می‌گویید `import ...`، باید فایل مشخص‌شده را پیدا کند. در توضیح سادهٔ اینجا، نام فایل از نامِ پس از `import` به‌اضافهٔ `.py` ساخته می‌شود. Python به این ترتیب جست‌وجو می‌کند:

> * ابتدا بررسی می‌کند آیا نامی که مشخص کرده‌اید در میان moduleهای built-in وجود دارد؛
> * اگر نبود، پوشه‌های فهرست `sys.path` را به‌ترتیب جست‌وجو می‌کند.

> **یادداشت مترجم — توضیح تکمیلی:** این شرح ساده‌شده است. سازوکار import ابتدا cache موجود در sys.modules را بررسی می‌کند و می‌تواند علاوه بر فایل‌های Python، packageها و moduleهای extension را هم بارگذاری کند؛ پس هر import الزاماً به جست‌وجوی یک فایل با پسوند py منتهی نمی‌شود. منبع: [سازوکار رسمی import](https://docs.python.org/3/reference/import.html#the-module-cache).

برای دیدن `sys.path` روی رایانهٔ خود می‌توانید کد زیر را اجرا کنید:

```python
import sys
sys.path
```

در فهرست پوشه‌هایی که `sys.path` برمی‌گرداند، working directory فعلی شما در جایگاه اول است.

> **یادداشت مترجم — توضیح تکمیلی:** جملهٔ بالا به محیط اجرا وابسته است. هنگام اجرای یک script، معمولاً پوشهٔ همان script در ابتدای مسیر جست‌وجو قرار می‌گیرد؛ در حالت تعاملی یا اجرای module با گزینهٔ -m، معمولاً working directory فعلی مبناست. گزینه‌های اجرا و تنظیمات محیط هم می‌توانند این رفتار را تغییر دهند. منبع: [مقداردهی اولیهٔ sys.path](https://docs.python.org/3/library/sys_path_init.html).

گاهی می‌دانید فایل module موردنیاز کجاست و لازم است پوشهٔ جست‌وجو را مشخص کنید. در این حالت می‌توانید با `sys.path.append()` یک محل جست‌وجوی تازه اضافه کنید:

```python
import sys
sys.path.append("/My/Path/To/Module/Directory")
import my_module
```

## moduleهای built-in سیستم

با کد زیر می‌توانید فهرست moduleهای built-in سیستم را بگیرید:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import sys

sys.builtin_module_names
"_sre" in sys.builtin_module_names # True
"math" in sys.builtin_module_names # False （根据自己电脑库的安装情况，结果会有不同）
```

    ('_abc',
     '_ast',
     '_codecs',
     '_collections',
     '_functools',
     '_imp',
     '_io',
     '_locale',
     '_operator',
     '_signal',
     '_sre',
     '_stat',
     '_string',
     '_symtable',
     '_thread',
     '_tracemalloc',
     '_warnings',
     '_weakref',
     'atexit',
     'builtins',
     'errno',
     'faulthandler',
     'gc',
     'itertools',
     'marshal',
     'posix',
     'pwd',
     'sys',
     'time',
     'xxsubtype',
     'zipimport')
    True
    False

همان‌طور که نام variable و function نمی‌تواند با keywordها یکسان باشد، بهتر است نام module شما هم با نام moduleهای built-in سیستم یکی نباشد.

> **یادداشت مترجم — توضیح تکمیلی:** فهرست sys.builtin_module_names به نحوهٔ ساخت interpreter وابسته است، نه صرفاً کتابخانه‌هایی که نصب کرده‌اید؛ built-in module هم با تمام moduleهای standard library یکسان نیست. خروجی و comment مثال اصلی حفظ شده‌اند و ممکن است در محیط شما متفاوت باشند. بهتر است از هم‌نامی با moduleهای standard library و وابستگی‌های پروژه نیز پرهیز کنید تا آن‌ها را ناخواسته پنهان نکنید. منبع: [مستندات sys.builtin_module_names](https://docs.python.org/3/library/sys.html#sys.builtin_module_names).

## import کردن functionهای مشخص از یک module

وقتی از `import mycode` استفاده می‌کنید، به بیان نویسنده، همهٔ functionهای تعریف‌شده در فایل `mycode` را وارد محیط فعلی می‌کنید؛ او آن را معادل شکل زیر معرفی می‌کند:

```python
from mycode import *
```

> **یادداشت مترجم — توضیح تکمیلی:** این دو دستور معادل نیستند. import mycode نامِ خودِ module را به محیط فعلی اضافه می‌کند و برای دسترسی به function از mycode.is_prime استفاده می‌کنید. شکل دارای ستاره، نام‌های عمومی module یا نام‌های تعیین‌شده در __all__ را مستقیماً وارد محیط فعلی می‌کند و ممکن است نام‌های موجود را بپوشاند. منبع: [آموزش رسمی moduleها](https://docs.python.org/3/tutorial/modules.html#more-on-modules).

در واقع می‌توانید فقط functionی را که فعلاً لازم دارید import کنید؛ برای مثال فقط `is_prime()`:

```python
from mycode import is_prime
```

در این حالت دیگر لازم نیست `mycode.is_prime()` بنویسید؛ درست مانند زمانی که function را در محیط فعلی تعریف کرده‌اید، مستقیماً `is_prime()` می‌نویسید:

```python
from mycode import is_prime
is_prime(3)
```

    True

توجه کنید: طبق توضیح متن اصلی، اگر فایل `mycode.py` در پوشهٔ فعلی نباشد، Python نام `mycode` را به‌عنوان نام پوشه هم امتحان می‌کند. اگر در پوشهٔ فعلی پوشه‌ای به نام `mycode` وجود داشته باشد و درون آن فایل [`__init__.py`](https://docs.python.org/3/reference/import.html#regular-packages) هم باشد، این پوشه یک **package**، یعنی [مجموعه‌ای از moduleها](https://docs.python.org/3/reference/import.html#regular-packages)، را تشکیل می‌دهد. این فایل معمولاً خالی است و برای مشخص کردن package به کار می‌رود؛ moduleهای آن هم در یک **namespace** مستقل قرار دارند؛ [لینک namespace در متن اصلی](https://docs.python.org/3/glossary.html#term-namespace-package). نویسنده در ادامه می‌گوید که در این حالت، `from mycode import *` همهٔ فایل‌های `.py` درون پوشهٔ `mycode` را import می‌کند…

> **یادداشت مترجم — توضیح تکمیلی:** بخش پایانیِ توضیح بالا درست نیست: import با ستاره، خودکار همهٔ فایل‌های داخل package را پیدا و import نمی‌کند. محتوای __init__.py و در صورت وجود، فهرست __all__ تعیین می‌کنند چه نام‌هایی وارد شوند. همچنین regular package دارای __init__.py است، اما namespace package می‌تواند بدون آن وجود داشته باشد؛ لینک namespace متن اصلی به همین نوع ویژهٔ package اشاره می‌کند، نه تعریف عمومی namespace. namespace در معنای عمومی، نگاشتی از نام‌ها به objectهاست. منابع: [import با ستاره از package](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package)، [namespace package](https://docs.python.org/3/reference/import.html#namespace-packages) و [تعریف namespace](https://docs.python.org/3/glossary.html#term-namespace).

اگر بخواهیم module موجود در فایل `bar.py` را از پوشهٔ `foo` import کنیم، می‌توانیم چنین بنویسیم:

```python
import foo.bar
```
یا:
```python
from foo import bar
```

## import کردن و استفاده از alias

گاهی برای جلوگیری از سردرگمی یا برای اینکه مجبور نباشیم نویسه‌های زیادی تایپ کنیم، می‌توانیم برای functionی که import می‌کنیم یک **alias**، یعنی نام جایگزین، تعیین کنیم و سپس با همان نام آن را فراخوانی کنیم. برای مثال:

```python
from mycode import is_prime as isp
isp(3)
```

    True

حتی می‌توانیم برای کل module یک alias بگذاریم:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import mycode as m

m.is_prime(3)
m.say_hi('mike', 'zoe')
```

    True
    Hello, mike!
    Hello, zoe!

## module لزوماً فقط شامل function نیست

فایل module لزوماً فقط function ندارد؛ می‌تواند بیرون از functionها هم کد اجرایی داشته باشد. هنگام اجرای دستور `import`، این کد اجراییِ خارج از functionها فقط یک بار اجرا می‌شود.

> **یادداشت مترجم — توضیح تکمیلی:** منظور، import عادیِ یک module در همان فرایند اجراست: پس از بارگذاری اولیه، معمولاً از نسخهٔ cacheشده استفاده می‌شود. بارگذاری مجددِ صریح یا شروع فرایندی تازه می‌تواند کد را دوباره اجرا کند. خودِ تعریف function هم هنگام بارگذاری اجرا می‌شود، اما بدنهٔ function تا زمان فراخوانی آن اجرا نمی‌شود. منبع: [جزئیات moduleها در آموزش رسمی](https://docs.python.org/3/tutorial/modules.html#more-on-modules).

یکی از Easter eggهای Python درست بهترین مثال برای اینجاست: moduleِ `this` که فایل آن [`this.py`](https://github.com/python/cpython/blob/master/Lib/this.py) نام دارد:

```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

کد درون moduleِ `this` چنین است:

```python
s = """Gur Mra bs Clguba, ol Gvz Crgref
Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
```

در فایل `this.py` هم functionی تعریف نشده است، اما پس از `import this` می‌توانیم به variableهایی که در آن تعریف شده‌اند دسترسی داشته باشیم:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import this
this.d
this.s
```

    {'A': 'N',
     'B': 'O',
     'C': 'P',
     'D': 'Q',
     'E': 'R',
     'F': 'S',
     'G': 'T',
     'H': 'U',
     'I': 'V',
     'J': 'W',
     'K': 'X',
     'L': 'Y',
     'M': 'Z',
     'N': 'A',
     'O': 'B',
     'P': 'C',
     'Q': 'D',
     'R': 'E',
     'S': 'F',
     'T': 'G',
     'U': 'H',
     'V': 'I',
     'W': 'J',
     'X': 'K',
     'Y': 'L',
     'Z': 'M',
     'a': 'n',
     'b': 'o',
     'c': 'p',
     'd': 'q',
     'e': 'r',
     'f': 's',
     'g': 't',
     'h': 'u',
     'i': 'v',
     'j': 'w',
     'k': 'x',
     'l': 'y',
     'm': 'z',
     'n': 'a',
     'o': 'b',
     'p': 'c',
     'q': 'd',
     'r': 'e',
     's': 'f',
     't': 'g',
     'u': 'h',
     'v': 'i',
     'w': 'j',
     'x': 'k',
     'y': 'l',
     'z': 'm'}
    
    "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf orggre guna htyl.\nRkcyvpvg vf orggre guna vzcyvpvg.\nFvzcyr vf orggre guna pbzcyrk.\nPbzcyrk vf orggre guna pbzcyvpngrq.\nSyng vf orggre guna arfgrq.\nFcnefr vf orggre guna qrafr.\nErnqnovyvgl pbhagf.\nFcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.\nNygubhtu cenpgvpnyvgl orngf chevgl.\nReebef fubhyq arire cnff fvyragyl.\nHayrff rkcyvpvgyl fvyraprq.\nVa gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.\nGurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.\nNygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.\nAbj vf orggre guna arire.\nNygubhtu arire vf bsgra orggre guna *evtug* abj.\nVs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.\nVs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"

امتحان کنید و ببینید آیا می‌توانید کد این فایل را خودتان، بدون کمک، بخوانید و بفهمید. برای تازه‌کارها تمرین ذهنی خوبی است!

این کد ابتدا بر اساس یک قاعده، جدول رمز می‌سازد و آن را در dictionary به نام `d` ذخیره می‌کند؛ سپس «متن رمزشده» در variableِ `s` را به متن انگلیسی تبدیل می‌کند…

شاید بتوانید امتحان کنید و functionی بنویسید که یک متن انگلیسی بگیرد و آن را به «متن رمزشده‌ای» مانند همین نمونه تبدیل کند؟

## functionِ dir()

وقتی function خود را در یک module ذخیره کردید، کاربران آن، از جمله خودتان، می‌توانند با functionِ `dir()` نام variableها و functionهای قابل دسترسی در module را ببینند:

```python
import mycode
dir(mycode)
```

    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'is_prime',
     'say_hi']



<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: مستندات function](Part.2.D.5-docstrings.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: توسعه با روش Test Driven Development](Part.2.D.7-tdd.md)

</div>

<!-- reading-navigation:end -->
