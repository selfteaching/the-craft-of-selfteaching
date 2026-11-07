<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: functionهای دارای recursion](Part.2.D.4-recursion.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: ذخیره کردن functionها در فایل](Part.2.D.6-modules.md)

</div>

<!-- reading-navigation:end -->


# مستندات function

وقتی functionی را فراخوانی می‌کنید، مانند کاربرِ محصولی هستید که آن function است.

نوشتن یک function هم مانند ساختن یک محصول است؛ محصولی که شاید در آینده کاربران زیادی داشته باشد، از جمله خود شما.

هر محصول باید راهنمای استفاده داشته باشد. هم دیگران به آن نیاز دارند و هم خودتان؛ ممکن است پس از مدت زیادی، همهٔ جزئیات و دلیل تصمیم‌های اولیه را فراموش کرده باشید. آن وقت شما هم به راهنمای استفاده نیاز دارید، حتی اگر طراح آن محصول خودتان بوده باشید.

Python در این زمینه توجه زیادی به خرج داده و «راهنمای استفاده» از function را به یکی از امکانات خود زبان تبدیل کرده است. شاید این هم یکی از دلایلی باشد که Python ابزاری مانند [Sphinx](http://www.sphinx-doc.org) دارد، در حالی که بیشتر زبان‌های دیگر چنین ابزاری ندارند.

> **یادداشت مترجم — توضیح تکمیلی:** مقایسهٔ پایانی، برداشت نویسنده است و نباید آن را نبودِ ابزار مستندسازی در زبان‌های دیگر دانست. خود Sphinx هم به Python محدود نیست و از زبان‌ها و حوزه‌های دیگری پشتیبانی می‌کند. منبع: [حوزه‌های پشتیبانی‌شده در مستندات رسمی Sphinx](https://www.sphinx-doc.org/en/master/usage/domains/index.html).

## Docstring

درون تعریف function می‌توانیم یک **Docstring** قرار دهیم؛ متنی که نحوهٔ استفاده از function را توضیح می‌دهد. بعداً «کاربر» function می‌تواند با functionِ built-in به نام `help()` یا با `.__doc__`، که نویسنده آن را Method نامیده است، این Docstring، یعنی «راهنمای استفاده» از function، را ببیند.

> **یادداشت مترجم — توضیح تکمیلی:** برخلاف نام‌گذاری متن اصلی، __doc__ یک attribute است، نه method؛ مقدار آن متن مستندات است و اگر Docstring وجود نداشته باشد، معمولاً None است. در مثال‌ها help مستندات را نمایش می‌دهد و print متن خام آن را چاپ می‌کند. منبع: [مستندات رسمی functionهای تعریف‌شده توسط کاربر](https://docs.python.org/3/reference/datamodel.html#user-defined-functions).

ابتدا نمونه‌ای از Docstring و روش دیدن Docstring یک function را بررسی کنیم:

```python
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

help(is_prime)
print(is_prime.__doc__)
is_prime.__doc__
```

    Help on function is_prime in module __main__:

    is_prime(n)
        Return a boolean value based upon
        whether the argument n is a prime number.

        Return a boolean value based upon
        whether the argument n is a prime number.

    '\n    Return a boolean value based upon\n    whether the argument n is a prime number.\n    '

Docstring می‌تواند یک string چندخطی یا تک‌خطی باشد:

```python
def is_prime(n):
    """Return a boolean value based upon whether the argument n is a prime number."""

    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

help(is_prime)
print(is_prime.__doc__)
is_prime.__doc__
```

    Help on function is_prime in module __main__:

    is_prime(n)
        Return a boolean value based upon whether the argument n is a prime number.

    Return a boolean value based upon whether the argument n is a prime number.

    'Return a boolean value based upon whether the argument n is a prime number.'

اگر function دارای Docstring باشد، این متن باید در ابتدای بدنهٔ تعریف function قرار بگیرد و مانند دستورهای دیگر، indentation مناسب را داشته باشد. اگر آن را جای دیگری بگذارید، به‌عنوان Docstring عمل نمی‌کند:

```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True
    """
    Return a boolean value based upon
    whether the argument n is a prime number.
    """

help(is_prime)
print(is_prime.__doc__)
is_prime.__doc__
```

    Help on function is_prime in module __main__:

    is_prime(n)

    None

## قواعد نوشتن Docstring

قواعد چیزی است که بهتر است رعایت شود، اما در عمل خیلی‌ها آن را رعایت نمی‌کنند.

حالا که یاد می‌گیریم، باید **درست‌وحسابی** یاد بگیریم؛ این واقعاً مهم است. بنابراین لازم است [PEP 257](https://www.python.org/dev/peps/pep-0257/)، سند قواعد Docstring در Python، را با دقت بخوانید.

خلاصهٔ قواعدی از PEP 257 که باید بدانید:

> 1. چه Docstring تک‌خطی باشد و چه چندخطی، آن را میان سه double quote قرار دهید؛
> 2. درون Docstring، پیش از شروع متن و پس از پایان آن، خط خالی نگذارید؛
> 3. در Docstring چندخطی، خط اول خلاصه است؛ سپس یک خط خالی می‌آید و بعد بقیهٔ توضیحات؛
> 4. یک Docstring کامل باید parameterها، مقدار بازگشتی، نوع خطاهایی که ممکن است رخ دهند، side effectهای احتمالی، محدودیت‌های استفاده از function و موارد مشابه را روشن و خلاصه توضیح دهد؛
> 5. توضیح هر parameter را در خطی جداگانه بنویسید…

> **یادداشت مترجم — توضیح تکمیلی:** side effect یعنی اثری غیر از برگرداندن مقدار، مانند نوشتن در فایل یا تغییر یک object مشترک. بند دوم، خلاصه‌سازیِ دقیقِ تمام توصیه‌های PEP 257 نیست: این سند برای Docstring چندخطی توصیه می‌کند سه double quote پایانی در خطی جدا قرار بگیرد؛ همچنین دربارهٔ فاصله‌گذاری Docstring مربوط به class قواعد دیگری دارد. خود سند، مبنای جزئیات است: [Docstringهای چندخطی در PEP 257](https://peps.python.org/pep-0257/#multi-line-docstrings).

چون هنوز بررسی class را شروع نکرده‌ایم، فعلاً از قواعد Docstring مربوط به class می‌گذریم. بااین‌حال، لازم است بارها به این قواعد برگردید و آن‌ها را مرور کنید. دربارهٔ Docstring دو سند وجود دارد:

> * [PEP 257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
> * [PEP 258: Docutils Design Specification](https://www.python.org/dev/peps/pep-0258/)

> **یادداشت مترجم — توضیح تکمیلی:** PEP 258 یک طرح تاریخی برای Docutils است و وضعیت رسمی آن «Rejected» است؛ آن را هم‌ردیفِ یک قاعدهٔ پذیرفته‌شده و جاری در نظر نگیرید. منبع: [وضعیت رسمی PEP 258](https://peps.python.org/pep-0258/).

به این نکته **به‌ویژه توجه کنید**:

> Docstring **برای انسان نوشته می‌شود**. بنابراین در Docstring کد پیچیده، توضیح **چرا** بسیار مهم‌تر از توضیحِ _چه کاری_ است. فعلاً این نکته را به خاطر بسپارید؛ با گذشت زمان آن را عمیق‌تر درک خواهید کرد.

## قواعد Docstring به شیوهٔ Sphinx

Sphinx می‌تواند Docstringها را از فایل‌های `.py` استخراج کند و مستندات کامل بسازد. اگر در آینده پروژه‌ای بزرگ بنویسید و به مستندات جامع نیاز داشته باشید، خواهید دید که Sphinx واقعاً «نجات‌دهنده» است؛ در وقت و نیرو صرفه‌جویی می‌کند، خیال شما را راحت می‌کند و حتی جانتان را نجات می‌دهد…

اینجا نمی‌توان یک‌باره روش استفاده از Sphinx را به‌طور کامل توضیح داد؛ به‌ویژه اینکه از زبان نشانه‌گذاری خاصی به نام reStructureText، با پسوند فایل `.rst`، هم استفاده می‌کند…

> **یادداشت مترجم — توضیح تکمیلی:** املای درست نام این زبان reStructuredText است. این زبان مختص Sphinx نیست؛ Sphinx برای نوشتن مستندات از آن استفاده می‌کند. در مثال زیر، فیلدهایی مانند param و returns برای مستندسازی parameterها و مقدار بازگشتی‌اند. نام‌های amount و destinationReached در Docstring با parameterهای واقعیِ method، یعنی distance و destination، هماهنگ نیستند؛ Cars نیز در این قطعه تعریف نشده و بدنهٔ method فقط pass است. این ناسازگاری‌های مثال اصلی بدون تغییر حفظ شده‌اند. منبع: [توضیح فیلدهای اطلاعاتی Python در Sphinx](https://www.sphinx-doc.org/en/master/usage/domains/python.html#info-field-lists).

بااین‌حال، می‌توانیم یک مثال ببینیم:

```python
class Vehicle(object):
    '''
    The Vehicle object contains lots of vehicles
    :param arg: The arg is used for ...
    :type arg: str
    :param `*args`: The variable arguments are used for ...
    :param `**kwargs`: The keyword arguments are used for ...
    :ivar arg: This is where we store arg
    :vartype arg: str
    '''

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        '''We can't travel a certain distance in vehicles without fuels, so here's the fuels

        :param distance: The amount of distance traveled
        :type amount: int
        :param bool destinationReached: Should the fuels be refilled to cover required distance?
        :raises: :class:`RuntimeError`: Out of fuel

        :returns: A Car mileage
        :rtype: Cars
        '''
        pass

help(Vehicle)
```

    Help on class Vehicle in module __main__:

    class Vehicle(builtins.object)
     |  Vehicle(arg, *args, **kwargs)
     |
     |  The Vehicle object contains lots of vehicles
     |  :param arg: The arg is used for ...
     |  :type arg: str
     |  :param `*args`: The variable arguments are used for ...
     |  :param `**kwargs`: The keyword arguments are used for ...
     |  :ivar arg: This is where we store arg
     |  :vartype arg: str
     |
     |  Methods defined here:
     |
     |  __init__(self, arg, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  cars(self, distance, destination)
     |      We can't travel a certain distance in vehicles without fuels, so here's the fuels
     |
     |      :param distance: The amount of distance traveled
     |      :type amount: int
     |      :param bool destinationReached: Should the fuels be refilled to cover required distance?
     |      :raises: :class:`RuntimeError`: Out of fuel
     |
     |      :returns: A Car mileage
     |      :rtype: Cars
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

Sphinx با کمک extensionها از Docstring به سبک Google و NumPy هم پشتیبانی می‌کند.

دو لینک زیر را اینجا می‌گذارم تا در آینده برای مراجعه در دسترس شما باشند:

> * [sphinx.ext.napoleon — پشتیبانی از Docstring به سبک NumPy و Google](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
> * [sphinx.ext.autodoc — گنجاندن مستندات از Docstringها](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: functionهای دارای recursion](Part.2.D.4-recursion.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: ذخیره کردن functionها در فایل](Part.2.D.6-modules.md)

</div>

<!-- reading-navigation:end -->
