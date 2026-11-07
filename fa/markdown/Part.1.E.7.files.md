<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: Containerهای داده](Part.1.E.6.containers.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: چطور با دانشی که پر از Forward Reference است، با آرامش روبه‌رو شویم؟](Part.1.F.deal-with-forward-references.md)

</div>

<!-- reading-navigation:end -->


# فایل‌ها

داده‌هایی که می‌خواهیم پردازش کنیم معمولاً آن‌قدر زیادند که به کمک کامپیوتر نیاز داریم. برای نگهداری، خواندن و نوشتن حجم زیادی از داده، به **file** نیاز است. در این فصل فقط ساده‌ترین نوع، یعنی فایل متنی، را معرفی می‌کنیم.

## ساخت فایل

ساده‌ترین راه ساخت فایل، استفاده از functionِ built-inِ `open()` در Python است.

[مستندات رسمی](https://docs.python.org/3/library/functions.html#open) functionِ `open()` طولانی است؛ شکل ساده‌شدهٔ آن چنین است:

> `open(file, mode='r')`

parameter دوم، `mode`، مقدار پیش‌فرض `'r'` دارد. حالت‌های قابل‌استفاده عبارت‌اند از:

| نشانهٔ حالت | معنی |
| -------- | ------------------------------- |
| `'r'` | فقط خواندن |
| `'w'` | نوشتن؛ ساخت مجدد فایل |
| `'x'` | ساخت انحصاری؛ اگر فایل وجود داشته باشد، باز کردن آن شکست می‌خورد |
| `'a'` | افزودن به انتهای فایل موجود |
| `'b'` | حالت فایل binary |
| `'t'` | حالت فایل متنی؛ پیش‌فرض |
| `'+'` | خواندن و نوشتن؛ به‌روزرسانی |

برای ساخت فایل تازه، همین یک statement کافی است:

> **یادداشت مترجم — توضیح تکمیلی:** **هشدار:** اگر فایل از قبل وجود داشته باشد، حالت `'w'` محتوای آن را پاک می‌کند. حالت `'a'` در صورت نبودن فایل، آن را می‌سازد. نشانه‌های `'b'`، `'t'` و `'+'` هم معمولاً با یک حالت پایه ترکیب می‌شوند؛ مثلاً `'rb'` یا `'r+'`. مسیر `/tmp/` در مثال‌های اصل به محیط Unix-like مربوط است و وجود آن در Windows تضمین‌شده نیست؛ مسیرهای کد عمداً تغییر نکرده‌اند. `open()` پوشهٔ والدِ ناموجود را ایجاد نمی‌کند. بنگرید به [open](https://docs.python.org/3/library/functions.html#open).

```python
open('/tmp/test-file.txt', 'w')
```

    <_io.TextIOWrapper name='/tmp/test-file.txt' mode='w' encoding='UTF-8'>

البته بیشتر وقت‌ها مقدار برگشتی این function، یعنی یک [file object](https://docs.python.org/3/glossary.html#term-file-object)، را در variable ذخیره می‌کنیم تا بعداً به قابلیت‌های آن دسترسی داشته باشیم؛ مثلاً نام فایل را با `file.name` بگیریم یا فایل را با `file.close()` ببندیم:

> **یادداشت مترجم — توضیح تکمیلی:** file object نمایندهٔ فایلِ بازشده در برنامه است. `name` یک attribute است، نه method؛ اما `close()` یک method است. encoding نشان‌داده‌شده در خروجی اول، ویژگی محیط اجرای نویسنده است و لزوماً در همهٔ محیط‌ها یکسان نیست.

```python
f = open('/tmp/test-file.txt', 'w')
print(f.name)
f.close()
```

    /tmp/test-file.txt

## حذف فایل

برای حذف فایل باید از moduleِ `os` استفاده کنیم. پیش از حذف، باید بررسی کنیم فایل وجود دارد یا نه؛ وگرنه دستور حذف شکست می‌خورد.

```python
import os

f = open('/tmp/test-file1.txt', 'w')
print(f.name)
f.close() #关闭文件，否则无法删除文件
if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted.')
else:
    print(f'{f.name} does not exist.')
```

    /tmp/test-file1.txt
    /tmp/test-file1.txt deleted.

## خواندن و نوشتن فایل

پس از ساخت فایل، با `f.write()` داده را در آن می‌نویسیم و با `f.read()` محتوایش را می‌خوانیم.

```python
f = open('/tmp/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('/tmp/test-file.txt', 'r')
s = f.read()
print(s)
f.close()
```

    first line
    second line
    third line

اگر فایل چند خط داشته باشد، می‌توان از `file.readline()` استفاده کرد. هر بار call کردن این method، خط بعدی فایل را برمی‌گرداند.

```python
f = open('/tmp/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('/tmp/test-file.txt', 'r')
s = f.readline()    # 返回的是 'first line\n'
print(s)
s = f.readline()    # 返回的是 'second line\n'
print(s)
f.close()
```

    first line
    second line

**توجه:** نتیجهٔ برگشتی شاید کمی با انتظارتان فرق داشته باشد. اینجاست که `str.strip()`، که قبلاً دیده‌ایم، به کار می‌آید:

> **یادداشت مترجم — توضیح تکمیلی:** خط خوانده‌شده معمولاً `\n` پایانی را هم دارد و `print()` نیز خودش newline اضافه می‌کند؛ در نتیجه هنگام اجرای واقعیِ مثال قبلی، میان خط‌ها یک خط خالی دیده می‌شود. خروجی ثبت‌شدهٔ اصل این فاصله‌ها را کامل منعکس نمی‌کند و عیناً حفظ شده است. `strip()` علاوه بر newline، whitespaceهای دو سر خط را هم حذف می‌کند؛ اگر فاصله‌های ابتدا یا انتهای داده مهم باشند، این تفاوت را در نظر بگیرید.

```python
f = open('/tmp/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('/tmp/test-file.txt', 'r')
s = f.readline().strip()    # 返回的是 'first line'，'\n' 被去掉了……
print(s)
s = f.readline().strip()    # 返回的是 'second line'，'\n' 被去掉了……
print(s)
f.close()
```

    first line
    second line

در مقابل، methodِ `file.readlines()` همهٔ خط‌های فایل را به‌صورت یک list برمی‌گرداند؛ هر عنصر این list متناظر با یک خط فایل است:

```python
f = open('/tmp/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('/tmp/test-file.txt', 'r')
s = f.readlines()    # 返回的是一个列表，注意，readlines，最后的 's'
print(s)
f.close()
```

    ['first line\n', 'second line\n', 'third line\n']

وقتی خروجی list باشد، می‌توان آن را iterate کرد و به خط‌ها یکی‌یکی دسترسی پیدا کرد:

```python
f = open('/tmp/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('/tmp/test-file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()
```

    first line
    second line
    third line

به همین ترتیب، با `file.writelines()` می‌توان یک list را در فایل نوشت: عنصرهای list به‌ترتیب index، از صفر به بعد، نوشته می‌شوند.

> **یادداشت مترجم — توضیح تکمیلی:** `writelines()` خودش newline اضافه نمی‌کند؛ جدا شدن خط‌های این مثال به‌خاطر وجود `\n` در انتهای stringهاست. خروجی ثبت‌شدهٔ loopهای `print(line)` در این بخش نیز مانند مثال پیشین، خط‌های خالی حاصل از اجرا را کامل نشان نمی‌دهد. بنگرید به [Methods of File Objects](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects).

```python
a_list = ['first line\n', 'second line\n', 'third line\n']
f = open('/tmp/test-file.txt', 'w')
f.writelines(a_list)
f.close()

f = open('/tmp/test-file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()
```

    first line
    second line
    third line

## Blockِ with

Python برای کار با فایل‌ها شکل دیگری از statement block دارد که خواندن آن راحت‌تر است:

```python
with open(...) as f:
    f.write(...)
    ...
```

به این ترتیب می‌توان همهٔ عملیات مربوط به فایلی را که با حالت مشخصی باز شده، در یک block قرار داد:

```python
import os

with open('/tmp/test-file.txt', 'w') as f:
    f.write('first line\nsecond line\nthird line\n')

with open('/tmp/test-file.txt', 'r') as f:
    for line in f.readlines():
        print(line)

if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted.')
else:
    print(f'{f.name} does not exist.')
```

    first line
    second line
    third line
    test-file.txt deleted.

مزیت دیگر blockِ `with` این است که دیگر لازم نیست `file.close()` بنویسید…

> **یادداشت مترجم — توضیح تکمیلی:** هنگام خروج از این block، فایل بسته می‌شود، حتی اگر حین کار exception رخ دهد. در خروجی ثبت‌شدهٔ مثال بالا، پیام حذف `test-file.txt deleted.` است، ولی کد با مسیر `/tmp/test-file.txt` باید همان مسیر کامل را در پیام نمایش دهد؛ این ناسازگاریِ اصل اصلاح نشده است. همچنین بررسی وجود فایل پیش از حذف، برای مثال ساده مفید است، اما تضمین نمی‌کند فایل در فاصلهٔ بررسی تا حذف از بین نرود. بنگرید به [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).

## یک برنامهٔ کامل دیگر

چند سال پیش، هنگام نوشتن کتابی، به مثالی نیاز داشتم که نشان بدهد: «**حتی اگر نتیجه درست باشد، استدلالِ آشفته و بی‌پایه پذیرفتنی نیست!**»

کار نویسنده همین است؛ یکی از وظیفه‌های اصلی‌اش پیدا کردن مثال و شاهد برای ادعاهاست. نویسندهٔ خوب کسی است که مثال‌ها و شاهدهایی پیدا کند که هم *مناسب* باشند و هم *جذاب*. همین «جذاب بودن» وقت و انرژی زیادی می‌گیرد، چون یعنی باید *مثال‌های زیادی* پیدا کنید و بعد *بهترینشان* را برگزینید! اصلاً آن‌طور که خیلی‌ها تصور می‌کنند نیست که مثال‌ها خودبه‌خود و بی‌زحمت به ذهن برسند.

مثال‌های زیادی پیدا کردم، اما هیچ‌کدام راضی‌ام نکرد… تا اینکه روزی به این گفته برخوردم:

> اگر حرف `a` را `1`، حرف `b` را `2`، حرف `c` را `3` و همین‌طور تا `z` را `26` حساب کنیم، آن وقت:
>
> - knowledge = 96
> - hardwork = 98
> - attitude = 100
>
> پس نتیجه این است:
>
> - دانش، *knowledge*، و سخت‌کوشی، *hardwork*، البته هر دو مهم‌اند؛
> - اما آنچه موفقیت و شکست را تعیین می‌کند، نگرش، **attitude**، است!

نتیجه شاید حرف معقولی باشد، اما این شیوهٔ استدلال دیگر واقعاً زیاده‌روی است…

خوشحال شدم؛ به نظرم این یک *مثال خوب* بود! با کمی کار می‌شد آن را برای خواننده جذاب‌تر هم کرد: اگر واژه‌هایی پیدا می‌کردم که با همین روش امتیازشان ۱۰۰ می‌شد، ولی از همان نگاه اول معلوم بود «مثال نقض» هستند…

شهودم می‌گفت در میان صدها هزار واژهٔ انگلیسی، باید واژه‌های بی‌شماری باشد که با این روش حاصل جمعشان ۱۰۰ شود. حتماً خیلی از واژه‌های دارای معنای منفی هم همین امتیاز را می‌گیرند، نه؟ اما در چنین موضوعی شهود کافی نیست و محاسبهٔ دستی هم آدم را از پا درمی‌آورد… پس در برابر چنین استدلال پوچی، ظاهراً «حرفی برای گفتن» نداریم.

خوشبختانه من برنامه‌نویسی بلد بودم. پس لازم نبود فقط حرص بخورم و کاری از دستم برنیاید؛ می‌توانستم کامپیوتر را به کار بگیرم تا این کار را برایم انجام دهد.

خیلی زود کار انجام شد. واژه‌های انگلیسی بسیار زیادی پیدا کردم که با این روش جمعشان ۱۰۰ می‌شد؛ از جمله:

> - connivance؛ چشم‌پوشیِ آگاهانه از کار نادرست و اجازه دادن به آن
> - coyness؛ کم‌رویی
> - flurry؛ سراسیمگی
> - impotence؛ ناتوانی جنسی
> - stress؛ فشار روانی
> - tuppence؛ چیزی کم‌ارزش
> - …

پس می‌شود گفت آنچه موفقیت و شکست را تعیین می‌کند «سراسیمگی»، flurry، یا حتی «ناتوانی جنسی»، impotence، است؟! این آشکارا حرف بی‌پایه‌ای نیست؟

و به این ترتیب، مثال جذابم آماده شد و آن را در کتاب گذاشتم.

حالا این کار دقیقاً چطور انجام شد؟

اول باید یک فهرست نسبتاً کامل از واژه‌های انگلیسی پیدا می‌کردم. برای این کار نیازی به برنامه‌نویسی نبود؛ یک جست‌وجوی Google کافی بود. عبارت جست‌وجویم [english word list](https://www.google.com/search?q=english+word+list) بود؛ روشن و مستقیم، نه؟ بعد این مخزن را پیدا کردم: [https://github.com/dwyl/english-words](https://github.com/dwyl/english-words). در آن فایلی به نام [words-alpha.txt](https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt) هست که نزدیک به ۳۷۰٬۱۰۱ واژه دارد؛ باید کافی باشد! کافی بود آن را دانلود کنم و با برنامه پردازشش کنم.

> **یادداشت مترجم — توضیح تکمیلی:** متن نمایشی پیوند در اصل `words-alpha.txt` است، ولی نام واقعی فایل در مقصد و کدها `words_alpha.txt` است. تعداد واژه‌ها و زمان اجرا در ادامه مربوط به داده‌ها و محیط زمان نگارش‌اند و برای نسخه‌های بعدی تضمین نمی‌شوند. کد فایل ورودی را نسبت به working directory می‌جوید، نه الزاماً کنار متن ترجمه.

چون در هر خط فایل یک واژه قرار دارد، کافی است برنامه فایل را باز کند، محتوایش را در یک list بخواند و بعد list را iterate کند. برای هر واژه، عدد متناظر هر حرف را حساب می‌کنیم و جمع می‌زنیم تا ببینیم ۱۰۰ می‌شود یا نه. اگر شد، آن واژه را روی صفحه نمایش می‌دهیم… ظاهراً چندان سخت نیست.

```python
with open('words_alpha.txt', 'r') as file:
    for word in file.readlines():
        pass # 先用 pass 占个位，一会儿再写计算过程
```

طبق آن گفته، دادن امتیاز `1` به `a` و ادامه دادن تا امتیاز `26` برای `z` سخت نیست، چون `ord()` را داریم. این function کد Unicode یک character را برمی‌گرداند: مقدار `ord('a')` برابر `97` است، پس با `ord('a') - 96` به `1` می‌رسیم؛ `ord('z') - 96` هم `26` می‌شود.

```python
ord('a')
```

    97

بنابراین کد محاسبه برای stringِ `'knowledge'` ساده است:

```python
word = 'knowledge'
sum = 0
for char in word:
    sum += ord(char) - 96
print(sum)
```

    96

واقعاً هم حاصل `96` شد؛ خوب است. آن را به یک function به نام `sum_of_word(word)` تبدیل کنیم:

```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

sum_of_word('attitude')
```

    100

حالا ظاهراً محاسبه برای چندصد هزار خط هم ساده است:

```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('words_alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word) == 100:
            print(word)
```

    abstrusenesses
    acupuncturist
    adenochondrosarcoma
    ...
    worshipability
    zeuctocoelomatic
    zygapophysis

عجب! چرا خروجی با انتظارمان فرق دارد؟ چرا واژه‌های پیدا‌شده این‌قدر نامأنوس‌اند؟ تازه، واژهٔ `attitude` هم در خروجی نیست.

یک statementِ توقف، یعنی `break`، اضافه کنیم و هر character از اولین واژهٔ پیدا‌شده را همراه مقدارش بررسی کنیم؟

```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('words_alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word) == 100:
            print(word)
            for c in word:        # 把字母和值都打出来，看看对不对？
                print(c, ord(c) - 96)
            break                 # 找到一个之后就停下来。
```

    abstrusenesses
    
    a 1
    b 2
    s 19
    t 20
    r 18
    u 21
    s 19
    e 5
    n 14
    e 5
    s 19
    s 19
    e 5
    s 19
    
     -86

این `-86` از کجا آمد؟! با دقت به خروجی نگاه کنید: میان خط‌ها یک خط خالی اضافه شده است. این یادآوری می‌کند که خط خوانده‌شده از فایل، characterِ newline، یعنی `\n`، را هم دارد… اگر این‌طور باشد، حاصل `ord('\n') -96` برابر `-86` است. پس بی‌دلیل نبود که واژه‌های خروجی آن‌قدر عجیب بودند…

```python
ord('\n') -96
```

    -86

بهترش کنیم؛ ساده است: پیش از محاسبه، whitespaceهای ابتدا و انتهای string خوانده‌شده را حذف می‌کنیم. `str.strip()` همین کار را انجام می‌دهد:

```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('words_alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word.strip()) == 100:
            print(word)
```

    abactinally
    abatements
    abbreviatable
    ...
    zithern
    zoogleas
    zorgite

اگر بخواهیم واژه‌های واجد شرط را در فایل `results.txt` ذخیره کنیم، می‌نویسیم:

```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('results.txt', 'w') as result:
    with open('words_alpha.txt', 'r') as file:
        for word in file.readlines():
            if sum_of_word(word.strip()) == 100:
                result.write(word)
```

یعنی به همین سادگی تمام شد؟!

این ده خط کد، در چند ثانیه از میان ۳۷۰٬۱۰۱ واژهٔ انگلیسی، ۳٬۷۷۱ واژه پیدا کرد که با این روش امتیازشان ۱۰۰ بود.

در حال نوشیدن قهوه، نگاهی به `results.txt` انداختم و خیلی زود واژه‌هایی پیدا کردم که برای مثال نقض کاملاً مناسب بودند.

واقعاً نمی‌توانم تصور کنم اگر آن موقع برنامه‌نویسی بلد نبودم، امروز چه وضعی داشتم…

> **یادداشت مترجم — توضیح تکمیلی:** در این مثال، variableِ `sum` نام functionِ built-inِ هم‌نام را می‌پوشاند؛ منطق مثال درست است، اما بهتر است در برنامه‌های خودتان به این تداخل نام توجه کنید. برای حفظ اصل، نام تغییر نکرده است. همچنین روش امتیازدهی این برنامه برای حرف‌های کوچک انگلیسیِ فهرست ورودی در نظر گرفته شده، نه هر string دلخواه.

## جمع‌بندی

در این فصل، عملیات پایهٔ فایل متنی را معرفی کردیم:

> * برای باز کردن فایل، مستقیماً از functionِ built-inِ `open()` استفاده می‌کنیم؛ حالت‌های پایهٔ مطرح‌شده `r` و `w` هستند.
> * برای حذف فایل، moduleِ `os` و `os.remove()` را به کار می‌بریم؛ بهتر است پیش از حذف، وجود فایل را بررسی کنیم…
> * برای خواندن و نوشتن، `file.read()`، `file.write()`، `file.readline()`، `file.readlines()` و `file.writelines()` را داریم.
> * با `with` می‌توان عملیات مرتبط را در یک block قرار داد…


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: Containerهای داده](Part.1.E.6.containers.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: چطور با دانشی که پر از Forward Reference است، با آرامش روبه‌رو شویم؟](Part.1.F.deal-with-forward-references.md)

</div>

<!-- reading-navigation:end -->
