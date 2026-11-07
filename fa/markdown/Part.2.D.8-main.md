<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: توسعه با روش Test Driven Development](Part.2.D.7-tdd.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: فکر کردن هدفمند](Part.2.E.deliberate-thinking.md)

</div>

<!-- reading-navigation:end -->


# فایل‌های اجرایی Python

از نظر نظری، در نهایت می‌توانید هر برنامه‌ای را، چه کوچک و چه بزرگ، در یک function جا بدهید یا اجرای آن را زیر پوشش یک function قرار دهید. طبق convention، نام این function را `main()` می‌گذارند:

```python
def routine_1():
    print('Routine 1 done.')

def routine_2():
    sub_routine_1()
    sub_routine_2()
    print('Routine 2 done.')

def sub_routine_1():
    print('Sub-routine 1 done.')

def sub_routine_2():
    print('Sub-routine 2 done.')

def main():
    routine_1()
    routine_2()
    print('This is the end of the program.')

if __name__ == '__main__':
    main()
```

    Routine 1 done.
    Sub-routine 1 done.
    Sub-routine 2 done.
    Routine 2 done.
    This is the end of the program.

وقتی یک module، یعنی در مثال اینجا یک فایل `.py` حاوی کد Python مانند `mycode.py`، با دستور `import` وارد می‌شود، مقدار `__name__` آن همان نام module است؛ برای مثال `'mycode'`.

اما وقتی module از خط فرمان اجرا شود، interpreterِ Python مقدار `__name__` آن را برابر `'__main__'` قرار می‌دهد.

کل برنامه را در `main()` قرار می‌دهیم و سپس این بخش را به کد module اضافه می‌کنیم:

```python
if __name__ == '__main__':
    main()
```

نتیجهٔ این کار چنین است:

> 1. وقتی فایل Python با دستور `import` به‌عنوان module وارد شود، شرط `if` برقرار نیست و functionِ `main()` اجرا نمی‌شود؛
> 2. وقتی فایل Python با `python -m` اجرا شود، شرط `if` برقرار است و functionِ `main()` اجرا می‌شود.

> **یادداشت مترجم — توضیح تکمیلی:** main نامی قراردادی است، نه نامی که Python خودکار فراخوانی کند؛ این شرط است که فراخوانی آن را کنترل می‌کند. رفتار دوم هم برای اجرای مستقیم فایل و هم برای اجرای module با گزینهٔ -m برقرار است. کدهای سطح module بیرون از این شرط، هنگام import همچنان اجرا می‌شوند. برای moduleهای درون package نیز __name__ معمولاً نام کاملِ شامل مسیر package است. منبع: [مستندات رسمی __main__](https://docs.python.org/3/library/__main__.html).

Easter eggِ Python را به خاطر دارید؟ کد `this.py` چنین است:

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

بنابراین با `import this`، کد داخل `this.py` اجرا می‌شود:

> **یادداشت مترجم — توضیح تکمیلی:** مانند فصل قبل، منظور اولین import عادی در همان فرایند است؛ import مجدد معمولاً از moduleِ cacheشده استفاده می‌کند و متن را دوباره چاپ نمی‌کند. منبع: [cache مربوط به moduleها](https://docs.python.org/3/reference/import.html#the-module-cache).

```python
import this
```

در پوشهٔ فعلی فایلی به نام `that.py` ذخیره کرده‌ام که محتوایش در ادامه آمده است. در واقع، فقط کد `this.py` را درون functionِ `main()` قرار داده‌ام:

```python
# %load that.py
def main():

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

if __name__ == '__main__':
    main()
```

حالا وقتی در جای دیگری آن را با `import that` وارد کنید، محتوای functionِ `main()` اجرا نمی‌شود:

```python
import that
```

اما اگر در خط فرمان با `python that.py` یا `python -m that` فایل `that.py` را به‌عنوان module اجرایی اجرا کنید، `main()` اجرا خواهد شد. دقت کنید اشتباه ننویسید: `python -m that.py` خطا می‌دهد. وقتی argumentِ `-m` را به کار می‌برید، پسوند `.py` را ننویسید:

> **یادداشت مترجم — توضیح تکمیلی:** برای آزمایش این بخش، ابتدا فایل that.py را با محتوای مثال بسازید. خط %%bash در دو بلوک زیر، cell magic مربوط به IPython/Jupyter است، نه دستور معمول Terminal؛ در Terminal فقط خطِ بعد از آن را وارد کنید. اجرای همین cellها با %%bash به در دسترس بودن Bash وابسته است و در Windows الزاماً آماده نیست. منابع: [مستندات %%bash](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-bash) و [گزینهٔ -m در Python](https://docs.python.org/3/using/cmdline.html#cmdoption-m).

```bash
%%bash
python that.py
```

```bash
%%bash
python -m that
```

پس از آنکه مانند `that.py` کل برنامه را در functionِ `main()` قرار دادید، `import that` دیگر کد داخل این function را خودکار اجرا نمی‌کند. اما همچنان می‌توانید `that.main()` را فراخوانی کنید:

```python
import that
that.main()
```

البته در `that.py` هیچ Docstringی وجود ندارد؛ بنابراین نتیجهٔ `help(that)` را می‌توانید به این شکل ببینید:

```python
import that
help(that)
```

> **یادداشت مترجم — توضیح تکمیلی:** متن اصلی پس از این مثال خروجی‌ای ثبت نکرده است. حتی بدون Docstring هم help می‌تواند اطلاعات ساختاری، مانند نام module و functionهایش، را نمایش دهد؛ نبودن Docstring به معنای خالی بودن تمام خروجی نیست. منبع: [مستندات help](https://docs.python.org/3/library/functions.html#help).

پس برنامهٔ قبلی هم که از میان بیش از ۳۷۰ هزار واژه، بیش از ۳۷۰۰ واژه با مجموع ارزش حروف برابر با 100 انتخاب می‌کرد، می‌تواند به شکل زیر نوشته شود:

```python
#!/usr/bin/env python

def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum
def main(wordlist, result):
    with open(result, 'w') as result:
        with open(wordlist, 'r') as file:
            for word in file.readlines():
                if sum_of_word(word.strip()) == 100:
                    result.write(word)

if __name__ == '__main__':
    main('words_alpha.txt', 'results.txt')
```

دربارهٔ خط اول کد بالا، یعنی `#!/usr/bin/env python`، پیشنهاد می‌کنم خودتان موضوع را پیگیری کنید. در Google جست‌وجو کنید:

> [`python3 script executable`](https://www.google.com/search?q=python3+script+executable)

خیلی زود متوجه خواهید شد…

همچنین این عبارت را جست‌وجو کنید:

> [`python3 script executable parameters retrieving`](https://www.google.com/search?q=python3+script+executable+parameters+retrieving)

بعد می‌توانید برنامهٔ بالا را به فایل اجرایی Python تبدیل کنید که در خط فرمان argumentهای مشخصی دریافت می‌کند…

> **یادداشت مترجم — توضیح تکمیلی:** خط آغازشده با #! را shebang می‌نامند؛ نقش آن در اجرای مستقیم فایل به سیستم‌عامل و روش اجرا وابسته است و نباید انتظار رفتار کاملاً یکسان در Windows و Unix داشت. نام python در این خط نیز الزاماً در همهٔ محیط‌ها همان نسخهٔ موردنظر شما نیست. برای دریافت argumentهای خط فرمان، sys.argv و moduleِ argparse منابع رسمی مناسبی‌اند. این مثال همچنین به فایل ورودی words_alpha.txt نیاز دارد؛ وجود آن را در پوشهٔ اجرا بررسی کنید. منابع: [scriptهای اجرایی Python در Unix](https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts)، [shebang در راهنمای Windows](https://docs.python.org/3/using/windows.html#shebang-lines)، [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv) و [argparse](https://docs.python.org/3/library/argparse.html).

راستی، با Easter eggِ `import this` می‌شود بازی جالب‌تری هم کرد:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import this
love = this
this is love                            # True
love is True                            # False
love is False                           # False
love is not True or False               # True
love is not True or False; love is love # True True
```

    True
    False
    False
    True
    True
    True

در Terminal دستور `python` را وارد کنید و Enter بزنید؛ سپس دستورها را در Interactive Shell یکی‌یکی امتحان کنید. هر عبارت پس از `love = this` یک عملیات Boolean است. فکر کنید چرا چنین نتیجه‌ای می‌دهد؟

> **یادداشت مترجم — توضیح تکمیلی:** commentهای چینیِ کد بعدی توضیح می‌دهند که this و love پس از assignment به همان object اشاره می‌کنند، اما هیچ‌کدام همان objectِ True یا False نیستند. همچنین is not از or اولویت بالاتری دارد؛ پس عبارت مربوطه مانند (love is not True) or False ارزیابی می‌شود و True می‌دهد. علامت ; دو دستور را در یک خط جدا می‌کند و love is love نیز True است. کد و commentهای اصلی بدون تغییر حفظ شده‌اند. منبع: [مقایسهٔ هویت و اولویت operatorها](https://docs.python.org/3/reference/expressions.html#is-not).

```python
import this
love = this

this is love
# True, 试试看，id(this) 和 id(love) 是同一个值
# 即，它们的内存地址相同

love is True
# False, id(love) 和 id(True) 不是同一个值
love is False
# 同上

love is not True or False
# is not 的优先级比 or 高；所以相当于是：
# (love is not True) or False，于是返回 True

love is not True or False; love is love
# 重复一次上一句 —— `;` 是语句分隔符
# 而后 love is love 当然是 True
```

در کد زیر، به خروجی functionِ `id()` توجه کنید:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import this
love = this
this is love
love is True
love is False
love is not True or False
love is not True or False; love is love
id(love)
id(this)
id(True)
id(False)
love is not True
```

    True
    False
    False
    True
    True
    True
    4345330968
    4345330968
    4308348176
    4308349120
    True

> **یادداشت مترجم — توضیح تکمیلی:** عددهای id در خروجی ثبت‌شده مربوط به همان اجرا هستند و در اجرای شما ممکن است متفاوت باشند. نکته این است که this و love به یک object اشاره می‌کنند و در طول عمر آن، id یکسان دارند. تفسیر id به‌عنوان نشانی حافظه، ویژگی پیاده‌سازی CPython است، نه تضمین عمومی زبان Python. منبع: [مستندات رسمی id](https://docs.python.org/3/library/functions.html#id).

جدول کامل اولویت operatorهای Python اینجاست:

> [Operator precedence — اولویت operatorها](https://docs.python.org/3/reference/expressions.html#operator-precedence)

Easter eggهای بیشترِ Python:

> [Python Easter Eggs](https://github.com/OrkoHunter/python-easter-eggs)


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: توسعه با روش Test Driven Development](Part.2.D.7-tdd.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: فکر کردن هدفمند](Part.2.E.deliberate-thinking.md)

</div>

<!-- reading-navigation:end -->
