<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: ذخیره کردن functionها در فایل](Part.2.D.6-modules.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: فایل‌های اجرایی Python](Part.2.D.8-main.md)

</div>

<!-- reading-navigation:end -->


# توسعه با روش Test Driven Development

نوشتن یک function یا برنامه، به بیان دیگر، همان «پیاده‌سازی یک الگوریتم» است. تعریفی که Wikipedia از «الگوریتم» ارائه می‌کند، چنین است:

> در ریاضیات و علوم رایانه، **الگوریتم** شرحی بی‌ابهام از روش حل یک دسته از مسئله‌هاست. الگوریتم‌ها می‌توانند *محاسبه*، _پردازش داده_ و *کارهای استدلال خودکار* را انجام دهند.

«الگوریتم» در واقع چیز مرموزی نیست؛ فقط «مراحل حل یک مسئله» است.

در [فصل اول بخش دوم](Part.2.A.clumsy-and-patience.md)، functionی برای تشخیص سال کبیسه دیدیم:

> بیایید functionی به نام is_leap() برای تشخیص سال کبیسه بنویسیم. این function یک سال را به‌عنوان parameter می‌گیرد؛ اگر سال کبیسه باشد True برمی‌گرداند و در غیر این صورت False.
>
> بر اساس تعریف سال کبیسه:
>
> > * سال باید مضرب 4 باشد؛
> > * سالی که بر 100 بخش‌پذیر باشد، اما بر 400 بخش‌پذیر نباشد، کبیسه نیست.
> > * پس کافی است از میان سال‌های بخش‌پذیر بر 4، سال‌هایی را کنار بگذاریم که بر 100 بخش‌پذیرند اما بر 400 بخش‌پذیر نیستند.

به عقب برنگردید! همین حالا خودتان نوشتن این function را امتحان کنید. خواهید دید که چندان هم آسان نیست…

```python
def is_leap(year):
    pass
```

گام اول برخلاف تصور خیلی‌ها این نیست که بلافاصله شروع به نوشتن کنیم…

گام اول این است که فرض کنیم function را نوشته‌ایم و حالا باید درستی نتیجه‌ای را که برمی‌گرداند بررسی کنیم…

این روش توسعه، یعنی «اول پیدا کردن راهی برای بررسی نتیجه و سپس حرکت از نتیجه به‌سوی پیاده‌سازی»، روشی بسیار مؤثر است که **Test Driven Development** نام دارد؛ یعنی توسعه‌ای که testها مسیر آن را هدایت می‌کنند.

اگر `is_leap(year)` را درست نوشته باشم، آن وقت:

> * مقدار بازگشتی `is_leap(4)` باید `True` باشد.
> * مقدار بازگشتی `is_leap(200)` باید `False` باشد.
> * مقدار بازگشتی `is_leap(220)` باید `True` باشد.
> * مقدار بازگشتی `is_leap(400)` باید `True` باشد.

توانایی فهرست کردن این چهار حالت، فقط نتیجهٔ «در نظر گرفتن همهٔ جوانب» بر اساس الگوریتم است. اما خودتان امتحان کنید تا ببینید حتی در کارهای ساده هم ظاهراً در نظر گرفتن همهٔ جوانب چندان آسان نیست…

پس پیش از نوشتن بدنهٔ `def is_leap(year)`، فقط با `pass` جای آن را نگه می‌دارم و بعد چهار دستور برای آزمایش نتیجه اضافه می‌کنم. فعلاً مقدار همهٔ این بررسی‌ها طبیعتاً `False` است… وقتی function را کامل و درست بنویسم، مقدار همهٔ آن‌ها باید `True` شود.

> **یادداشت مترجم — توضیح تکمیلی:** pass هیچ کاری انجام نمی‌دهد؛ functionی که فقط همین دستور را دارد، به‌طور ضمنی None برمی‌گرداند. بنابراین هر چهار بررسی هویت با True یا False در این مرحله نادرست‌اند. چهار مورد بالا حالت‌های متفاوتی را پوشش می‌دهند، اما اثبات درستی برای تمام ورودی‌ها نیستند. قواعد سال کبیسهٔ این مثال مربوط به تقویم Gregorian است، نه تقویم هجری خورشیدی. منابع: [تعریف function و مقدار بازگشتی ضمنی](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) و [تقویم Gregorian در moduleِ calendar](https://docs.python.org/3/library/calendar.html).

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    pass

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True
```

    False
    
    False
    
    False
    
    False

از آنجا که بیشتر سال‌ها کبیسه نیستند، ترتیب کنار گذاشتن حالت‌ها را تقریباً چنین در نظر می‌گیریم:
> * ابتدا فرض کنیم هیچ سالی کبیسه نیست؛
> * سپس بررسی کنیم آیا سال بر `4` بخش‌پذیر است؛
> * بعد سال‌هایی را کنار بگذاریم که بر `100` بخش‌پذیرند اما بر `400` بخش‌پذیر نیستند…

پس ابتدا جملهٔ اول را پیاده‌سازی می‌کنیم: «فرض کنیم هیچ سالی کبیسه نیست»:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    r = False
    return r

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True
```

    False
    True
    False
    False

سپس این بخش را پیاده‌سازی می‌کنیم: «سال باید مضرب 4 باشد»:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
    return r

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True
```

    True
    False
    True
    True

اکنون فقط قاعدهٔ آخر باقی مانده است: «سال‌هایی را کنار بگذاریم که بر `100` بخش‌پذیرند، اما بر `400` بخش‌پذیر نیستند». برای نمونه، مقدار `200` را برای parameter در نظر بگیرید:

> * چون بر `4` بخش‌پذیر است، `r = True` می‌شود؛
> * سپس بررسی می‌کنیم آیا بر `100` بخش‌پذیر است. بله؛ پس حالا بررسی می‌کنیم آیا بر `400` هم بخش‌پذیر است؛
>   * اگر نباشد، `r = False` می‌کنیم؛
>   * اگر باشد، مقدار `r` را نگه می‌داریم…
> به این ترتیب، برای `200` قطعاً `r = False` خواهد شد.

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
        if year % 100 == 0:
            if year % 400 !=0:
                r = False
    return r

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True
```

    True
    True
    True
    True

هرچند خواندن این روند کاملاً روشن و سرراست به نظر می‌رسد، وقتی خودتان آن را از ابتدا تا انتها انجام دهید، ممکن است در هر مرحله اشتباه کنید. اگر باور ندارید، امتحان کنید: پایین همین صفحه یک cell اضافه کنید و خودتان همه‌چیز را از ابتدا بنویسید…

البته کدی که پیش‌تر در moduleِ `datetime.py` از کتابخانهٔ همراه Python دیدیم، کوتاه‌تر است:

```python
# cpython/Lib/datetime.py
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
_is_leap(300)
```

    False

خودتان امتحان کنید: از نوشتن test شروع کنید و قدم‌به‌قدم این پیاده‌سازی را بسازید. البته copy و paste مجاز نیست، خنده‌دار است اما جدی می‌گویم!

در Python نوعی کنترل جریان مخصوص «آزمودن و برخورد با خطا» وجود دارد. امروزه بیشتر زبان‌های برنامه‌نویسی چنین دستورهایی دارند.

هنگام شروع اجرای برنامه، دو نوع خطا ممکن است باعث شکست آن شوند:

> * Syntax Errors، یعنی خطاهای مربوط به syntax؛
> * Exceptions، یعنی وضعیت‌های استثنایی.

برای مثال، اگر در Python 3 به‌جای `print(i)` بنویسید `print i`، یک Syntax Error مرتکب شده‌اید. parser مستقیماً به شما می‌گوید در کدام خط چه خطایی در syntax رخ داده است. با وجود چنین خطایی، اجرای برنامه شروع نمی‌شود.

اما گاهی syntax کاملاً درست است و بااین‌حال یک **exception** رخ می‌دهد. این خطاها پس از شروع اجرای برنامه پیش می‌آیند و Runtime Error نامیده می‌شوند؛ چون نبودِ خطای syntax اجازه می‌دهد اجرای برنامه آغاز شود. برای مثال، فرض کنید بنویسید `print(11/0)`:

```python
print(11/0)
```

    ---------------------------------------------------------------------------
    
    ZeroDivisionError                         Traceback (most recent call last)
    
    <ipython-input-2-5544d98276be> in <module>
    ----> 1 print(11/0)
    
    ZeroDivisionError: division by zero

هرچند خودِ این دستور خطای syntax ندارد، این expression قابل محاسبه نیست. بنابراین `ZeroDivisionError` ایجاد می‌کند و این exception اجازه نمی‌دهد اجرای برنامه ادامه پیدا کند.

> **یادداشت مترجم — توضیح تکمیلی:** در این مثال، علت خطا تقسیم بر صفر است. اگر exception به‌طور مناسب مدیریت شود، برنامه می‌تواند ادامه پیدا کند؛ در غیر این صورت اجرای عادی متوقف می‌شود. در Notebook معمولاً اجرای همان cell متوقف می‌شود، نه لزوماً کل محیط. همچنین SyntaxError خود یکی از نوع‌های exception است؛ تقسیم‌بندی بالا تفاوت آموزشیِ خطای syntax با خطاهای هنگام اجرا را بیان می‌کند. منبع: [آموزش رسمی Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html).

در Python تعداد زیادی exception رایج تعریف شده‌اند که به‌صورت سلسله‌مراتبی دسته‌بندی شده‌اند:

> پس از خواندن بخش سوم، می‌توانید برگردید و مستندات رسمی زیر را دوباره بررسی کنید:<br />
> https://docs.python.org/3/library/exceptions.html

> **یادداشت مترجم — توضیح تکمیلی:** درخت زیر وضعیت زمان نگارش منبع را نشان می‌دهد و برای نسخه‌های جدید Python کامل نیست؛ برای نمونه، نوع‌های مربوط به ExceptionGroup بعداً افزوده شده‌اند. همچنین برچسب bash صرفاً قالب بلوک منبع است؛ این درخت دستور قابل اجرا در shell نیست. منبعِ فهرست به‌روز: [سلسله‌مراتب exceptionها](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).

``` bash
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

برای مثال `FileNotFoundError` را در نظر بگیرید. پیش از باز کردن یک فایل، باید راهی برای بررسی وجود آن داشته باشیم. اگر فایل وجود نداشته باشد، یک exception رخ می‌دهد.

> **یادداشت مترجم — توضیح تکمیلی:** بررسی وجود فایل پیش از باز کردن آن، موفقیت را تضمین نمی‌کند؛ ممکن است فایل بین بررسی و باز کردن حذف شود. روش try و except که در ادامه می‌آید، خطای خودِ عملیات باز کردن را مدیریت می‌کند. منبع: [توضیح رسمی دربارهٔ بررسی پیشاپیش دسترسی به فایل](https://docs.python.org/3/library/os.html#os.access).

```python
f = open('test_file.txt', 'r')
```

    ---------------------------------------------------------------------------
    
    FileNotFoundError                         Traceback (most recent call last)
    
    <ipython-input-3-5fac19176fe6> in <module>
    ----> 1 f = open('test_file.txt', 'r')
    
    FileNotFoundError: [Errno 2] No such file or directory: 'test_file.txt'

در Python می‌توانیم دستورهایی را که ممکن است exception ایجاد کنند، در بلوک `try` اجرا کنیم. `try` می‌تواند همراه `except`، `else` و `finally` به کار برود. از زاویه‌ای دیگر، بلوک `try` نوع خاصی از کنترل جریان است که به این پرسش می‌پردازد: «وقتی exception رخ داد، چه کنیم؟»

```python
try:
    f = open('test_file.txt', 'r')
except FileNotFoundError as fnf_error:
    print(fnf_error)
```

    [Errno 2] No such file or directory: 'test_file.txt'

نتیجه چنین است:

> وقتی دستور `f = open('test_file.txt', 'r')` به دلیل نبودن فایل `test_file.txt` یک exception ایجاد کند، بلوک `except` کنترل جریان را به دست می‌گیرد. چون در این بلوک نوع `FileNotFoundError` را مشخص کرده‌ایم، اگر واقعاً همین خطا رخ داده باشد، کد داخل آن، یعنی `print(fnf_error)`، اجرا می‌شود…

شکل‌های دیگری از این جریانِ مدیریت خطا هم وجود دارد:

```python
try:
    do_something()
except built_in_error as name_of_error:
    do_something()
else:
    do_something()
```

یا:

```python
try:
    do_something()
except built_in_error as name_of_error:
    do_something()
else:
    do_something()
finally:
    do_something()
```

حتی می‌توان آن‌ها را به‌صورت تودرتو نوشت:

```python
try:
    do_something()
except built_in_error as name_of_error:
    do_something()
else:
    try:
        do_something()
    except built_in_error as name_of_error:
        do_something()
...
```

> **یادداشت مترجم — توضیح تکمیلی:** در الگوهای بالا، نام‌هایی مانند do_something و built_in_error جای‌نگهدارند و پیش از اجرای واقعی باید با کد و نوع exception مناسب جایگزین شوند. else وقتی اجرا می‌شود که بلوک try بدون exception تمام شود؛ finally برای کارهای پایانی، مانند آزاد کردن منابع، است و در مسیرهای معمول خروج از این ساختار، چه خطایی رخ داده باشد چه نه، اجرا می‌شود. منبع: [جزئیات دستور try](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement).

برای یادگیری بیشتر دربارهٔ مدیریت خطا، پس از خواندن مطالب مربوط به class در بخش سوم، مستندات رسمی زیر را با دقت بخوانید:

> * [Errors and Exceptions — خطاها و exceptionها](https://docs.python.org/3/tutorial/errors.html)
> * [Built-in Exceptions — exceptionهای built-in](https://docs.python.org/3/library/exceptions.html)
> * [Handling Exceptions — مدیریت exceptionها](https://wiki.python.org/moin/HandlingExceptions)

در واقع، شاید نباید عنوان بزرگی مانند «Test Driven Development» بر این فصل می‌گذاشتیم؛ چون در توسعهٔ واقعی، آنچه Test Driven Development نامیده می‌شود از moduleها، frameworkها و ابزارهای قوی‌تر و پیچیده‌تری استفاده می‌کند؛ برای مثال، دست‌کم از moduleِ [unittest](https://docs.python.org/3/library/unittest.html) در standard libraryِ Python.

> **یادداشت مترجم — توضیح تکمیلی:** داشتن framework خاص، شرط تعریف TDD نیست؛ نکتهٔ محوری، نوشتن test پیش از پیاده‌سازی و پیش بردن کد با بازخورد testهاست. unittest امکاناتی برای سازمان‌دهی و اجرای خودکار testها فراهم می‌کند. مدیریت exception نیز با نوشتن test یکی نیست: اولی رفتار برنامه در برابر وضعیت‌های استثنایی را تعیین می‌کند و دومی رفتار مورد انتظار را بررسی می‌کند. منبع برای نقش unittest: [معرفی رسمی unittest](https://docs.python.org/3/library/unittest.html).

هنگام نوشتن برنامه، برای دیگران و خودِ آینده‌مان comment و Docstring بنویسیم؛ برای اطمینان از درستی نتیجه در حالت‌های مختلف test بنویسیم؛ یا از همان ابتدا exceptionهای گوناگون را در نظر بگیریم و از بلوک‌های مدیریت خطا استفاده کنیم. این‌ها کارهایی کاملاً بدیهی‌اند، اما بیشتر مردم انجامشان نمی‌دهند… چون کمی دردسر به نظر می‌رسند.

اینجاست که بهترین نمونه‌های «گرفتار شدن به‌خاطر زرنگیِ خود» به‌مرور روی هم انباشته می‌شوند. خیلی‌ها واقعاً چون باهوش‌اند، فکر می‌کنند «لازم نیست این‌قدر خودم را به زحمت بیندازم». درست مثل سقراط (Socrates) که بنا بر روایت نویسنده، به حافظهٔ بسیار قوی خود تکیه می‌کرد، تا جایی که هرچه را یک بار می‌دید به خاطر می‌سپرد، و کسانی را که یادداشت برمی‌داشتند، تحقیر می‌کرد.

اما با گذشت زمان و بزرگ‌تر شدن حجم پروژه، سرانجام همان «آدم‌های باهوش» در دام خودشان می‌افتند. هوش به‌تنهایی از پس یک پروژه برنمی‌آید؛ آنچه پروژه را پیش می‌برد، خرد است. سقراط خودش پروژه‌ای به انجام نرساند؛ شاگردش افلاطون (Plato) بود که با وجود تمسخر او، همه‌چیز را با قلم و کاغذ ثبت کرد. سپس شاگرد افلاطون، ارسطو (Aristotle)، فرصت یافت از سقراط الهام بگیرد، کتاب «تحلیلات پیشین» (Prior Analytics) را بنویسد و «قیاس سه‌بخشی» یا syllogism را مطرح کند؛ چیزی که تا امروز بر بشر اثر گذاشته است…

> **یادداشت مترجم — نیازمند بررسی:** جزئیات این روایت تاریخی، از جمله حافظهٔ سقراط، تمسخر یادداشت‌برداری، ثبت «همه‌چیز» با قلم و کاغذ و این زنجیرهٔ علت‌ومعلولی، در متن منبع سندی ندارند و در این ترجمه تأیید نشده‌اند. استدلال آموزشیِ نویسنده دربارهٔ اهمیت ثبت و بررسی کار را باید از صحت این روایت جدا دانست.

مبادا سادگی مثال‌های بخش دوم شما را گمراه کند. این مثال‌ها عمداً ساده انتخاب شده‌اند تا خواننده آسان‌تر بر جنبه‌های گوناگونِ نوشتن function به دست خودش تمرکز کند. اما وقتی در آینده واقعاً خودتان کاری انجام دهید، یا حتی کد یک پروژهٔ واقعی را بخوانید، می‌بینید که همچنان دشواری زیادی دارد. دست‌کم گرفتنِ امروز، می‌تواند به شکست فردا منجر شود.

هنوز وقتش نیست؛ پس از تمام کردن کل کتاب، به خاطر داشته باشید که برگردید و لینک‌های زیر را ببینید:

> * [doctest — آزمایش مثال‌های تعاملی Python](https://docs.python.org/3/library/doctest.html)
> * [unittest — frameworkِ unit testing](https://docs.python.org/3/library/unittest.html)


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: ذخیره کردن functionها در فایل](Part.2.D.6-modules.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: فایل‌های اجرایی Python](Part.2.D.8-main.md)

</div>

<!-- reading-navigation:end -->
