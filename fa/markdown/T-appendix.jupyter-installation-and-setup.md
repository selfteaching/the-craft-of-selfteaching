<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: آشنایی با Git](T-appendix.git-introduction.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: این نشانه‌ها چه معنایی دارند؟](T-appendix.symbols.md)

</div>

<!-- reading-navigation:end -->


# نصب و پیکربندی JupyterLab

## دانلود و نصب Anaconda

[Anaconda](https://www.anaconda.com) در حال حاضر راحت‌ترین توزیع Python است و بسیاری از بسته‌هایی را همراه دارد که بالاخره به آن‌ها نیاز پیدا خواهیم کرد. علاوه بر Python، [زبان R](https://www.r-project.org/)، [Pandoc](https://pandoc.org/)، [NumPy](http://www.numpy.org/)، [SciPy](https://www.scipy.org/)، [Matplotlib](https://matplotlib.org/) و بسیاری ابزارهای دیگر هم در آن گنجانده شده‌اند.

چه از رابط گرافیکی برای نصب استفاده کنید و چه از خط فرمان، پیشنهاد می‌کنم Anaconda را در پوشهٔ شخصی کاربر، یعنی `~/`، نصب کنید. نسخهٔ Python 3.x را دانلود و نصب کنید.

راهنمای رسمی نصب از طریق رابط گرافیکی مفصل است و دستورالعمل سیستم‌عامل‌های مختلف را پوشش می‌دهد:

> https://docs.anaconda.com/anaconda/install/

در خط فرمان Terminal در macOS، می‌توانید مستقیماً آن را دانلود و نصب کنید:

```bash
cd ~/Downloads/
wget https://repo.anaconda.com/archive/Anaconda3-2018.12-MacOSX-x86_64.sh
chmod +x Anaconda3-2018.12-MacOSX-x86_64.sh
./Anaconda3-2018.12-MacOSX-x86_64.sh
```

در آخرین مرحلهٔ نصب از شما پرسیده می‌شود که آیا می‌خواهید [Visual Studio Code](https://code.visualstudio.com)، محصول Microsoft، را نصب کنید یا نه. `yes` را انتخاب کنید؛ به‌هرحال در آینده بیش از یک ویرایشگر متن روی رایانه‌تان خواهید داشت… از ویرایشگرهای دیگری که ممکن است بعدها نصب کنید، [SublimeText](https://www.sublimetext.com) و [Atom](https://atom.io) هستند.

> **یادداشت مترجم — توضیح تکمیلی:** توزیع Python بسته‌ای است که Python و مجموعه‌ای از ابزارها و کتابخانه‌ها را یک‌جا ارائه می‌کند. عبارت «در حال حاضر»، فهرست بسته‌ها و پیشنهاد نصب ویرایشگرها در این بخش به زمان نگارش اشاره دارند. فایل نصب بالا مربوط به دسامبر ۲۰۱۸ و Macهای Intel است؛ آن را دستور نصب پیشنهادی امروز، به‌ویژه برای Apple silicon، ندانید. وجود `wget` و پیشنهاد نصب VS Code در همهٔ محیط‌ها و نسخه‌های نصب‌کننده تضمین‌شده نیست. برای انتخاب نصب‌کنندهٔ سازگار با سیستم خود، [راهنمای رسمی نصب Anaconda](https://docs.anaconda.com/anaconda/install/) را بررسی کنید. دستورها در این ترجمه بدون تغییر حفظ شده‌اند و اجرا نشده‌اند.

پس از پایان نصب، Terminal را باز کنید؛ در Windows باید Anaconda Prompt را که پیش‌تر نصب شده است باز کنید و دستورها را در آن وارد کنید. سپس چند جزء دیگر را نصب کنید:

```bash
conda update conda
conda update anaconda
conda install -c conda-forge nodejs
conda install -c conda-forge jupyterlab # 这是用来升级 jupyter lab 到最新版的方法
```

> **یادداشت مترجم — توضیح تکمیلی:** comment چینیِ آخرین دستور می‌گوید این روش برای ارتقای JupyterLab به تازه‌ترین نسخه است. دستورهای `update` می‌توانند بسته‌های محیط را تغییر دهند؛ نتیجه به نسخه‌ها و کانال‌های مورد استفاده بستگی دارد. نیاز به Node.js در روش‌های قدیمی ساخت extensionها را نباید پیش‌نیاز همیشگی استفاده از JupyterLab امروزی دانست. [راهنمای رسمی نصب JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) را مبنا قرار دهید.

پس از نصب می‌توانید ببینید دستورهای اجرایی موردنیازتان در کجا قرار دارند. برای این کار از `which` استفاده کنید؛ در Windows از `where` استفاده می‌شود:

```bash
which python
python --version
which node
node -v
which jupyter
jupyter lab --version
jupyter notebook --version
which pip
pip --version
```

## نخستین اجرای JupyterLab

Terminal را باز کنید و با `cd` به پوشه‌ای بروید که می‌خواهید JupyterLab در آن باز شود؛ یعنی جایی که فایل‌های `ipynb` را نگه می‌دارید تا بتوانید آن‌ها را در JupyterLab باز کنید، بخوانید و ویرایش کنید. در اینجا پوشهٔ شخصی کاربر، یعنی `~/`، را مثال می‌زنیم:

```bash
cd ~
jupyter lab
```

حالا نباید پنجرهٔ Terminal را ببندید؛ وگرنه JupyterLab هم متوقف می‌شود. بگذارید همان‌جا باز بماند.

سپس مرورگری باز می‌شود و به نشانی [http://localhost:8888/lab?](http://localhost:8888/lab?) می‌رود؛ اکنون رابط کاربری JupyterLab را می‌بینید.

در حال حاضر JupyterLab و Jupyter Notebook در کنار هم وجود دارند، هرچند اولی گام بعدی برای جایگزینی دومی است. اگر هنوز به Jupyter Notebook عادت دارید، مرورگر را به نشانی [http://localhost:8888/tree?](http://localhost:8888/tree?) ببرید تا Jupyter Notebook را ببینید.

> **یادداشت مترجم — توضیح تکمیلی:** Notebook سندی با بخش‌های جداگانهٔ کد و متن است و پسوند فایل آن معمولاً `.ipynb` است. `localhost` به همین رایانه اشاره دارد. نشانی، پورت و token لازم برای ورود را از خروجی Terminal بگیرید؛ ممکن است دقیقاً مانند نمونه نباشند. توصیف رابطهٔ دو رابط و دسترسی از مسیر `/tree` مربوط به محیط نویسنده است و به بسته‌ها و نسخه‌های نصب‌شده بستگی دارد. [راهنمای اجرای JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html) را ببینید.

## پیکربندی JupyterLab

Terminal را باز کنید و دستور زیر را وارد کنید:

```bash
jupyter lab --generate-config
```

این دستور در پوشهٔ `~/.jupyter/` فایلی به نام `jupyter_notebook_config.py` می‌سازد.

```bash
cd ~/.jupyter
code jupyter_notebook_config.py
```

برای استفاده از دستور `code` در بالا، باید Visual Studio Code را نصب کرده و گزینهٔ `Install 'code' command in PATH` را در آن فعال کرده باشید. پیوست [نصب و پیکربندی Visual Studio Code](T-appendix.editor.vscode.md) را ببینید.

البته می‌توانید فایل `~/.jupyter/jupyter_notebook_config.py` را با هر ویرایشگری که دوست دارید باز کنید.

محتوای فایل طولانی است؛ هر وقت فرصت داشتید آن را با دقت بخوانید. می‌توانید محتوای زیر را مستقیماً در انتهای فایل کپی کنید و بر اساس نیازتان تغییر دهید:

```json
#c.NotebookApp.token = ''
#c.NotebookApp.open_browser = False
#c.NotebookApp.notebook_dir = '~/'
#c.NotebookApp.default_url = '/tree'
```

> **یادداشت مترجم — توضیح تکمیلی:** نام فایل و گزینه‌های بالا متعلق به پیکربندی نسخه‌های قدیمی‌اند. در نسخه‌های جدید ممکن است فایل پیکربندی JupyterLab یا Jupyter Server و نام گزینه‌ها متفاوت باشد؛ خروجی دستور تولید پیکربندی و [راهنمای انتقال پیکربندی به Jupyter Server](https://jupyter-server.readthedocs.io/en/latest/operators/migrate-from-nbserver.html) را بررسی کنید. بلوک بالا با برچسب `json` عیناً از اصل حفظ شده، اما محتوایش تنظیمات Python است، نه JSON؛ وجود `#` در آغاز خط نیز یعنی آن تنظیم فعلاً comment و غیرفعال است.

هر مورد را جداگانه توضیح می‌دهیم:

> `c.NotebookApp.token = ''`

هر بار که Jupyter را باز می‌کنید، یک token تازه برایتان تولید می‌کند؛ این بخشی از سازوکار امنیتی است. اما اگر فقط روی رایانهٔ خودتان از آن استفاده می‌کنید، این موضوع دردسر ایجاد می‌کند: برای باز کردن هم‌زمان آن در مرورگری دیگر باید token را از Terminal کپی کنید. بنابراین می‌توانید در فایل پیکربندی، مقدار آن را مستقیماً خالی بگذارید.

> **یادداشت مترجم — توضیح تکمیلی:** token یک کلید ورود است که دسترسی به محیط اجرای کد را محدود می‌کند. خالی کردن آن می‌تواند حفاظت ورود را از بین ببرد؛ حتی روی رایانهٔ شخصی هم این کار را توصیه نمی‌کنیم. توصیهٔ تاریخی نویسنده حفظ شده است، نه اینکه ایمن بودن آن تأیید شود. به‌جای حذف احراز هویت، از نشانی ورود تولیدشده یا روش‌های امن مستندشده استفاده کنید و سرویس را بدون حفاظت در دسترس شبکه نگذارید. منبع: [امنیت Jupyter Server](https://jupyter-server.readthedocs.io/en/latest/operators/security.html).

> `c.NotebookApp.open_browser = False`

هر بار که دستور `jupyter lab` یا `jupyter notebook` را اجرا می‌کنید، مرورگر پیش‌فرض سیستم به کار می‌رود.

عادت‌های افراد متفاوت است. مثلاً من ترجیح می‌دهم مرورگری را که معمولاً کمتر استفاده می‌کنم، فقط به Jupyter اختصاص بدهم؛ این‌طوری موقع بستن صفحه‌های دیگر، ناخواسته Jupyter را نمی‌بندم… برای همین این گزینه را روی `False` می‌گذارم.

> `c.NotebookApp.notebook_dir = '~/'`

وقتی دستور `jupyter` را در Terminal اجرا می‌کنید، Jupyter به‌طور پیش‌فرض در پوشهٔ کاری فعلی شما باز می‌شود؛ این هم ملاحظه‌ای امنیتی است. اما اگر فقط روی رایانهٔ خودتان کار می‌کنید و تنها کاربر آن هستید، شاید راحت‌تر باشد آن را مستقیماً روی `~/`، یعنی پوشهٔ شخصی خودتان، تنظیم کنید تا دسترسی به فایل‌های جاهای مختلف آسان‌تر باشد…

> **یادداشت مترجم — توضیح تکمیلی:** با انتخاب پوشهٔ شخصی به‌عنوان ریشهٔ دسترسی، فایل‌های بیشتری از طریق سرویس در دسترس قرار می‌گیرند. برای تمرین، انتخاب پوشهٔ مشخص پروژه دامنهٔ دسترسی را محدودتر می‌کند؛ شخصی بودن رایانه به‌تنهایی جایگزین ملاحظات امنیتی نیست.

> `c.NotebookApp.default_url = '/tree'`

این گزینه برای کسانی است که هنوز به Jupyter Notebook عادت دارند. با این تنظیم، حتی اگر دستور `jupyter lab` را وارد کنید، Jupyter Notebook باز می‌شود.

دستورهای مربوط به Jupyter که در Terminal زیاد به کار می‌آیند عبارت‌اند از:

```bash
jupyter lab
jupyter lab --version
conda install -c conda-forge jupyterlab # 这是用来升级 jupyter lab 到最新版的方法
jupyter notebook list                   # 查看正在运行的 jupyter lab/notebook
jupyter notebook stop                   # 停止 jupyter lab/notebook 服务
```

> **یادداشت مترجم — توضیح تکمیلی:** commentهای سه خط آخر، به‌ترتیب، «روش ارتقای JupyterLab به تازه‌ترین نسخه»، «دیدن JupyterLab/Notebookهای در حال اجرا» و «متوقف کردن سرویس JupyterLab/Notebook» هستند. در نسخه‌های جدید، دستورهای مدیریت سرویس را مطابق مستندات همان نسخه بررسی کنید.

## پیکربندی JupyterLab به‌عنوان سرویس سیستم

اگر از اینکه هر بار برای اجرای JupyterLab به Terminal بروید خسته شده‌اید، می‌توانید آن را به‌عنوان سرویس سیستم تنظیم کنید تا هر بار با روشن شدن رایانه خودکار اجرا شود. آن‌وقت کافی است در مرورگر به [http://localhost:8888/](http://localhost:8888/) بروید.

```bash
code ~/Library/LaunchAgents/com.jupyter.lab.plist
```

این دستور باعث می‌شود Visual Studio Code فایل `~/Library/LaunchAgents/com.jupyter.lab.plist` را بسازد و باز کند.

محتوای زیر را در آن کپی کنید. دقت کنید که باید `your_username` را با نام کاربری خودتان جایگزین کنید:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>local.job</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Users/your_username/anaconda3/bin/jupyter</string>
		<string>lab</string>
		<string>--no-browser</string>
		<string>--notebook-dir=/Users/your_username/</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
	<key>StandardErrorPath</key>
	<string>/tmp/local.job.err</string>
	<key>StandardOutPath</key>
	<string>/tmp/local.job.out</string>
</dict>
</plist>
```

اگر قبلاً در فایل `jupyter_notebook_config.py` این تنظیمات را انجام داده‌اید:

```json
c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '~/'
```

دیگر نیازی به این دو خط نیست:

```xml
		<string>--no-browser</string>
		<string>--notebook-dir=/Users/your_username/</string>
```

سپس در Terminal اجرا کنید:

```bash
launchctl load ~/Library/LaunchAgents/com.jupyter.lab.plist
```

اگر بخواهید این سرویس را دوباره راه‌اندازی کنید، اجرا کنید:

```bash
launchctl unload ~/Library/LaunchAgents/com.jupyter.lab.plist
launchctl load ~/Library/LaunchAgents/com.jupyter.lab.plist
```

> **یادداشت مترجم — توضیح تکمیلی:** این روش مخصوص macOS و سازوکار `launchd` است، نه Windows یا Linux. فایل در پوشهٔ LaunchAgents کاربر قرار می‌گیرد؛ اجرای آن به نشست کاربر مربوط است و عبارت «با روشن شدن رایانه» را نباید تضمین اجرا پیش از ورود کاربر دانست. مسیر نصب Anaconda را نیز باید مطابق نصب خودتان بررسی کنید و فایل را در ویرایشگر ذخیره کنید. گزینه‌ها و روش مدیریت سرویس ممکن است در نسخهٔ فعلی macOS متفاوت باشند؛ [راهنمای رسمی Apple دربارهٔ agentها و daemonها](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html) را ببینید. نمونهٔ سرویس در این ترجمه اجرا یا نصب نشده است؛ آن را با احراز هویت غیرفعال راه‌اندازی نکنید.

## دربارهٔ themeهای JupyterLab

برای کاربران چینی‌زبان، اندازهٔ پیش‌فرض نوشته‌ها در Jupyter کمی کوچک است و خواندن آن چندان راحت نیست. اما بهترین راه‌حل، جست‌وجوی theme مناسب نیست؛ بهتر است از مرورگری استفاده کنید که extensionهایی مانند [Stylus](https://github.com/openstyles/stylus) را برای سفارشی‌سازی CSS در سمت کاربر پشتیبانی می‌کند. Chrome، Firefox و Opera از Stylus پشتیبانی می‌کنند.

CSS سفارشی من در Stylus به این شکل است:

```css
a {color: #2456A4 !important;}
strong {color:#6392BF;}
em {color: #A9312A; font-style: normal !important;}
table {font-size: 90% !important;}

#jp-main-dock-panel {background-color: #f9f9f9;}
.jp-RenderedHTMLCommon {font-family: "Yuanti SC"; font-size: 100%;}
.jp-Notebook {background-color: #fbfafa;}
.CodeMirror, .jp-RenderedHTMLCommon pre {font-size: 90%;}
.jp-RenderedHTMLCommon pre {
    padding: 10px 25px;
    background-color: #fafafa;
    border-left: 4px solid #dadada;
    border-radius: 10px;
}

.jp-RenderedHTMLCommon pre code {
    background-color: #fafafa;
}

.jp-RenderedHTMLCommon h1 code,
.jp-RenderedHTMLCommon h2 code,
.jp-RenderedHTMLCommon h3 code,
.jp-RenderedHTMLCommon h4 code,
.jp-RenderedHTMLCommon p code,
.jp-RenderedHTMLCommon li code,
.jp-RenderedHTMLCommon blockquote p code,
.jp-RenderedHTMLCommon blockquote li code,
.jp-RenderedHTMLCommon td code {
    background-color: #f6f6f6;
    font-size: 90%;
    color:#2e2e2e;
    padding: 4px 4px;
    margin: 0 8px;
    box-shadow: 0px 1px 2px 0px rgba(0,0,0,0.2);
    border-radius: 4px;
}
```

به این ترتیب، در واقع theme با نام JupyterLab Light را کمی دست‌کاری کرده‌ام.

همچنین برای برجسته کردن نکته‌های مهم در نوشته‌هایم، نمایش دو عنصر `strong` و `em` را طوری تنظیم کرده‌ام که رنگ‌های متفاوتی داشته باشند. از آنجا که نمایش کج برای متن چینی مناسب نیست، مقدار `font-style` مربوط به `em` را هم روی `normal` گذاشته‌ام…

> **یادداشت مترجم — توضیح تکمیلی:** CSS قواعد نمایش ظاهری صفحه را مشخص می‌کند و theme مجموعه‌ای از تنظیمات ظاهر است. این نمونه، سلیقه و محیط نویسنده را نشان می‌دهد؛ فونت `Yuanti SC` برای متن چینی انتخاب شده و لزوماً روی سیستم شما موجود یا برای فارسی مناسب نیست. selectorهای نمونه نیز ممکن است با رابط نسخهٔ فعلی JupyterLab منطبق نباشند. کد اصلی بدون تغییر حفظ شده و نمایش آن در مرورگر آزمایش نشده است.

## نصب extensionها

Jupyter Notebook در طول سال‌ها توسعه، extensionهای زیادی پیدا کرده است، اما بعضی از آن‌ها با تازه‌ترین JupyterLab سازگار نیستند. با این حال، برای شروع به extensionهای زیادی احتیاج ندارید؛ همین دو مورد کافی‌اند:

> * [@jupyterlab/toc](https://github.com/jupyterlab/jupyterlab-toc)
> * [ryantam626/jupyterlab_sublime](https://github.com/ryantam626/jupyterlab_sublime)

ابتدا با میان‌بر `⌘ ,` بخش Advanced Settings در JupyterLab را باز کنید و در Extension Manager این User Overrides را اضافه کنید:

```json
{
    "enabled": true
}
```

> **نکته:** در JupyterLab 3.x / 4.x می‌توانید Extension Manager را مستقیماً در رابط Settings با علامت زدن گزینهٔ مربوط فعال کنید و دیگر لازم نیست تنظیم JSON بالا را دستی اضافه کنید.

سپس برای نصب extensionها دستورهای زیر را در Terminal اجرا کنید:

```bash
jupyter labextension install @jupyterlab/toc
jupyter labextension install @ryantam626/jupyterlab_sublime
jupyter lab build
```

extension مربوط به toc، عنوان‌های فایل `ipynb` را خودکار به فهرست مطالب تبدیل می‌کند.

![](https://github.com/jupyterlab/jupyterlab-toc/raw/master/toc.gif)

با jupyterlab_sublime می‌توانید در cellهای JupyterLab از میان‌برهایی مانند SublimeText استفاده کنید. مثلاً `⌘ D` نمونه‌های دیگرِ همان متن انتخاب‌شده را هم انتخاب می‌کند؛ یا با `⌘` و کلیک ماوس می‌توانید چند نقطهٔ قابل‌ویرایش ایجاد کنید…

![](http://blog.rtwilson.com/wp-content/uploads/2016/03/IPyNbSublime.gif)

> **یادداشت مترجم — توضیح تکمیلی:** extension قابلیت اضافه‌ای است که به برنامه افزوده می‌شود. پویانمایی اول، ساخت فهرست از عنوان‌ها و رفتن به بخش مربوط را نشان می‌دهد؛ دومی انتخاب و ویرایش هم‌زمان در چند نقطه را نمایش می‌دهد. دستورهای نصب بالا مربوط به روش قدیمی extensionهای نیازمند ساخت‌اند. فهرست مطالب در JupyterLabهای جدید قابلیت داخلی است؛ برای نمونه [راهنمای فهرست مطالب](https://jupyterlab.readthedocs.io/en/stable/user/toc.html) را ببینید. پیش از نصب jupyterlab_sublime سازگاری آن را با نسخهٔ خود بررسی کنید و [راهنمای رسمی extensionها](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html) را بخوانید. «نکته» دربارهٔ نسخه‌های 3.x / 4.x در متن اصلی هم وجود دارد و یادداشت افزودهٔ مترجم نیست.

## میان‌برهای پرکاربرد

در ادامه پرکاربردترین میان‌برهای JupyterLab در macOS آمده‌اند. میان‌برها در دو حالت اجرا می‌شوند: برای ورود به edit mode از `⏎` و برای بازگشت به command mode از `⎋` یا ESC استفاده کنید.

همچنین برای استفاده از قابلیت «ویرایش هم‌زمان چند خط» هنگام ویرایش کد، باید extension مربوط به JupyterLab، یعنی [@ryantam626/jupyterlab_sublime](https://github.com/ryantam626/jupyterlab_sublime)، را نصب کنید.

| میان‌بر | توضیح | حالت |
| ------- | ----- | ---- |
| `ESC` | بازگشت از edit mode به command mode | command |
| `A` | درج یک cell پیش از cell فعلی | |
| `B` | درج یک cell پس از cell فعلی | |
| `D`, `D` | با دو بار زدن پیاپی کلید `d`، cell فعلی را حذف کنید | |
| `Y` | تبدیل cell فعلی به Code Cell | |
| `M` | تبدیل cell فعلی به Markdown Cell | |
| `^ ⇧ - ` | تقسیم cell فعلی به دو cell | edit |
| `⇧ M` | ادغام cellهای انتخاب‌شده | |
| `⇧ J` or `⇧ ↓` | گسترش انتخاب cellها به سمت پایین | |
| `⇧ K` or `⇧ ↑` | گسترش انتخاب cellها به سمت بالا | |
| `⇧ ⏎` or `^ ⏎` | اجرای کد cell فعلی | |
| `⇧ L` | نمایش یا پنهان کردن شمارهٔ خط‌های کد | |
| `⏎` | ورود cell فعلی به edit mode | edit |
| `⇥` | تکمیل خودکار کد | |
| `⇧ ⇥` | نمایش docstring مورد زیر مکان‌نما | |
| `⌘ D` | Sublime Keymap: انتخاب نمونهٔ بعدی همان string | |
| `⇧ ⌘ L` | Sublime Keymap: فعال کردن ویرایش هم‌زمان چند خط در خط‌های انتخاب‌شده | |
| `⌘ + Mouse Click` | ایجاد نقطهٔ بعدی برای مکان‌نمای قابل‌ویرایش هم‌زمان | |

> **یادداشت مترجم — توضیح تکمیلی:** cell هر بخش مستقل متن یا کد در Notebook است. در command mode فرمان روی cellها اعمال می‌شود؛ در edit mode محتوای داخل cell را ویرایش می‌کنید. `⌘` یعنی Command، `⇧` یعنی Shift، `^` یعنی Control و `⇥` یعنی Tab. docstring متن توضیحی همراه یک جزء کد است. جای برچسب حالت‌ها و خانه‌های خالی جدول مطابق اصل حفظ شده‌اند؛ این چینش به معنی یکسان بودن حالت اجرای همهٔ سطرهای پس از آن نیست. میان‌برهای واقعی را در تنظیمات نسخهٔ خود بررسی کنید؛ مثلاً ادغام cellهای انتخاب‌شده به command mode مربوط است. شرح نیاز به extension نیز وضعیت محیط نویسنده را بیان می‌کند، نه همهٔ ویرایشگرهای امروزی.

## افزودن چند میان‌بر ضروری

در Settings > Keyboard Shortcuts می‌توانید چند میان‌بر پرکاربرد را که سیستم به‌صورت پیش‌فرض فراهم نکرده است تعریف کنید:

```json
{
	"notebook:move-cells-down-down": {
		"command": "notebook:move-cell-down",
		"keys": [
		"Alt J"
		],
		"selector": ".jp-Notebook:focus",
		"title": "Move Cells Down",
		"category": "Notebook Cell Operations"
	},
	"notebook:move-cells-down-up": {
		"command": "notebook:move-cell-up",
		"keys": [
		"Alt K"
		],
		"selector": ".jp-Notebook:focus",
		"title": "Move Cells Down",
		"category": "Notebook Cell Operations"
	},
	"notebook:enable-output-scrolling": {
		"command": "notebook:enable-output-scrolling",
		"keys": [
		"S"
		],
		"selector": ".jp-Notebook:focus",
		"title": "Enable output scrolling",
		"category": "Notebook Cell Operations"
	},
	"notebook:disable-output-scrolling": {
		"command": "notebook:disable-output-scrolling",
		"keys": [
		"Alt S"
		],
		"selector": ".jp-Notebook:focus",
		"title": "Enable output scrolling",
		"category": "Notebook Cell Operations"
	}
}
```

به این ترتیب چهار میان‌بر اضافه می‌شود:
> * `⌥ J`: جابه‌جایی cellهای انتخاب‌شده به پایین
> * `⌥ K`: جابه‌جایی cellهای انتخاب‌شده به بالا
> * `S`: فعال کردن پیمایش خروجی
> * `⌥ S`: غیرفعال کردن پیمایش خروجی

مثلاً جابه‌جایی cellهای انتخاب‌شده به بالا:

![](https://user-images.githubusercontent.com/86304/37438938-b5bc4994-27b2-11e8-8f58-184a58b33ba4.gif)

> **یادداشت مترجم — توضیح تکمیلی:** `⌥` کلید Option در macOS است. پویانمایی، بالا بردن cell انتخاب‌شده را بدون کپی کردن محتوای آن نشان می‌دهد. قالب تنظیمات و شناسهٔ فرمان‌های بالا قدیمی است؛ آن‌ها را بدون بررسی در تنظیمات نسخهٔ جدید کپی نکنید. در نمونهٔ اصلی، بعضی عنوان‌های `title` با عملکرد `command` هم‌خوان نیستند؛ این متن‌ها بدون اصلاح پنهانی حفظ شده‌اند. برای تعریف میان‌بر در نسخهٔ خود، [راهنمای تنظیمات JupyterLab](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#settings) را ببینید.

## نمایش محتوای همهٔ variableها

به‌صورت پیش‌فرض، Code Cell فقط آخرین مقداری را نمایش می‌دهد که ارزیابی می‌شود. `_` نمایندهٔ مقداری است که درست پیش از آن ارزیابی شده است.

```python
[1, 2, 3]
```

    [1, 2, 3]

```python
_ # 执行完上面的 Cell，试试这个 Cell; 而后执行完下面的 Cell 之后再重新执行一次当前这个 Cell
```

    [1, 2, 3]

```python
(1, 2, 3)
{1, 2, 3}
```

    {1, 2, 3}

بنابراین برای نمایش چند مقداری که به‌تازگی ارزیابی شده‌اند، مدام ناچار می‌شویم از `print()` استفاده کنیم…

اگر این کار را خسته‌کننده می‌دانید، می‌توانید در ابتدای cell بنویسید:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

اگر می‌خواهید کار باز هم راحت‌تر شود، این تنظیم را در فایل پیکربندی بنویسید:

```python
c.InteractiveShell.ast_node_interactivity = "all"
```

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

(1, 2, 3)
{1, 2, 3}
```

    (1, 2, 3)
    
    {1, 2, 3}

> **یادداشت مترجم — توضیح تکمیلی:** variable نامی است که به یک مقدار اشاره می‌کند؛ عنوان این بخش در اصل هم «همهٔ variableها» است، اما تنظیم بالا نتیجهٔ عبارت‌های قابل‌نمایش را نشان می‌دهد، نه فهرست خودکار همهٔ variableهای موجود. `_` در محیط تعاملی IPython به آخرین نتیجهٔ نمایش‌داده‌شده اشاره می‌کند. comment چینیِ مثال می‌گوید: پس از اجرای cell بالایی این cell را امتحان کنید؛ سپس cell پایینی را اجرا کنید و دوباره به همین cell برگردید. تنظیم دائمی `InteractiveShell` به پیکربندی IPython مربوط است و نباید آن را با پیکربندی سرویس Jupyter یکی دانست؛ [مستندات رسمی پیکربندی IPython](https://ipython.readthedocs.io/en/stable/config/intro.html) را ببینید. کد و خروجی‌های ثبت‌شده عیناً حفظ شده‌اند و در جریان ترجمه اجرا نشده‌اند.

## Magic Functions

در Code Cell می‌توانید بعضی «Magic Functions» را اجرا کنید؛ این قابلیت از IPython به ارث رسیده است. بیشتر Magic Functionهایی که در IPython قابل استفاده‌اند، مستقیماً در JupyterLab هم کار می‌کنند. برای فهرست کامل آن‌ها به این نشانی مراجعه کنید:

> https://ipython.readthedocs.io/en/stable/interactive/magics.html

Magic Functionهای پرکاربردتر در JupyterLab در جدول زیر آمده‌اند:

| Magic Function | توضیح |
| -------------- | ----- |
| `%lsmagic` | فهرست همهٔ Magic Functionهای قابل استفاده در JupyterLab |
| `%run` | اجرای فایل `.py` در cell: `%run file_name` |
| `%who` | فهرست همهٔ variableهای Global Scope فعلی؛ نمونه‌های مرتبط: `%who df` و `%whos` |
| `%env` | نمایش فهرست environment variableهای فعلی |
| `%load` | وارد کردن محتوای فایل دیگر به cell با `%load source`؛ `source` می‌تواند نام فایل یا URL باشد. |
| `%time` | نمایش زمان اجرای کد داخل cell؛ `%timeit` هم مرتبط است. |
| `%writefile` | نوشتن محتوای cell در فایل، `%write file_name`؛ %write -a file_name، و `-a` برای افزودن به انتهای فایل است. |
| `%matplotlib inline` | نمایش نتیجهٔ matplotlib در همان Notebook |
| `%%bash` | اجرای دستورهای shell پس از آن، مثلاً %%bash ls؛ موارد مشابه شامل `%%HTML`، `%%python2`، `%%python3`، `%%ruby` و `%%perl` هستند… |

> **یادداشت مترجم — توضیح تکمیلی:** Magic Function فرمان ویژهٔ محیط IPython است، نه syntax عمومی Python؛ در Notebook نیز در دسترس بودن آن به kernel، یعنی محیط اجرای کد، بستگی دارد. Global Scope به نام‌های سطح اصلی محیط اجرا اشاره دارد و environment variableها تنظیمات محیط فرایند هستند. در ردیف `%writefile`، متن اصلی مثال‌های `%write` را نوشته است؛ صورت مستند برای نوشتن یک cell در فایل، `%%writefile file_name` و برای افزودن به انتها، `%%writefile -a file_name` است. همچنین `%%bash` یک cell magic است: معمولاً در خط اول cell می‌آید و دستورهایی مانند `ls` در خط‌های بعد قرار می‌گیرند، نه به صورت `%%bash ls` برای اجرای `ls`. این ناسازگاری‌های اصل بی‌صدا اصلاح نشده‌اند. پشتیبانی Bash و kernelهای نام‌برده به محیط شما بستگی دارد؛ مرجع رسمی همان [مستندات Magicهای IPython](https://ipython.readthedocs.io/en/stable/interactive/magics.html) است.

## برنامه‌های دسکتاپ Jupyter

### Nteract

از سیستم‌عامل‌های مختلف پشتیبانی می‌کند و هم زیباست و هم خوش‌دست. یک ایراد کوچک دارد: فراخوانی function به نام `input()` را پشتیبانی نمی‌کند.

> https://nteract.io/desktop

![نمایی از برنامهٔ Nteract](https://cloud.githubusercontent.com/assets/836375/18421299/d95ad398-783b-11e6-8b23-d54cf7caad1e.png)

### Pineapple

فقط از macOS پشتیبانی می‌کند و استفاده از آن هم راحت است؛ عیبش این است که ظاهر خیلی بدی دارد…

> https://nwhitehead.github.io/pineapple/

![نمایی از برنامهٔ Pineapple](https://nwhitehead.github.io/pineapple/images/sshots.png?raw=true)

> **یادداشت مترجم — توضیح تکمیلی:** دو تصویر، نمونه‌ای از رابط دسکتاپ برای باز کردن Notebook و کار با cellها را نشان می‌دهند؛ نکتهٔ آموزشی این است که مرورگر تنها شکل رابط کاربری ممکن نیست. توصیف ظاهر، پشتیبانی سیستم‌عامل و محدودیت `input()` گزارش نویسنده از نسخه‌های زمان نگارش است. وضعیت کنونی نگهداری، دریافت و سازگاری این برنامه‌ها در این بازبینی تأیید نشده است؛ پیش از نصب، منابع معرفی‌شده را بررسی کنید.


<!-- reading-navigation:start -->

<div dir="rtl" lang="fa">

[بخش قبلی: آشنایی با Git](T-appendix.git-introduction.md) · [فهرست مطالب](TOC.md) · [بخش بعدی: این نشانه‌ها چه معنایی دارند؟](T-appendix.symbols.md)

</div>

<!-- reading-navigation:end -->
