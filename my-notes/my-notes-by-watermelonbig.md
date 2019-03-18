> 利用周末时间通读了一遍，学到了很多，在此对作者表示感谢。上传一篇读书笔记，表明我来过，认真读过。

每个人基础不同，关注点自然不同。下面只是一份我的阅读笔记，记录的是我自认为有缺陷或存在生板的一些知识或智慧吧，以及一些可以继续深究的新知识，好便于日后自己缺哪补哪、有的放矢、反复练习。

关于迭代器，生成器和yield的定义与使用技巧方面，本书中描述较简单，如果也有像我没完全整明白的读者，建议也可以参考下面这篇文章：[Python yield 使用浅析](https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)

## 鸡汤摘录
自学是门手艺，编程很大程度上也是一门手艺，掌握它在绝大多数情况下与天分智商全无关系 —— 很多人是在十来岁的时候学会编程的基本技能的。所有的手艺，最基本特征就是：

> **主要靠时间**

这就跟你看人们的车技一样，二十年安全驾龄和刚上路的肯定不一样，但，这事儿跟天分、智商真的没什么关系……

把一切都当作手艺看的好处之一就是心态平和，因为你知道那不靠天分和智商，它靠的就一件事儿，不混时间，刻意思考、刻意练习 —— 其实吧，老祖宗早就有总结：
  >天下无难事，只怕有心人……

有个现象，不自学的人不知道。真正开始自学且不断自学之后，刚开始总是觉得时间不够用 —— 因为当时的自己和其他人没什么太大区别。

随着时间的推移，不仅差异会出现，自我认知差异也开始越来越明显：
  >别人的时间都白过了，自己的时间都有产出……

到了下一个阶段，在其他人不断焦虑的情况下，自己却开始越来越淡定：
>因为早已习惯了投入大量时间换取新技能……

等后来真的开始用这些技能做事，不断地做其他人因为时间白过了或者因为投入的“预算”不够而学不会做不到的事情 —— 并且还能充分明白，这并不是自己聪明、有天分的结果；只不过是做了该做的事情，投入了该投入的“成本”和“预算”而已……

于是，就真的能够理解下面这句话背后的深意：
>人生很长，何必惊慌。

反正，这事儿跟天分与智商几乎没有任何关系。

**刻意思考**

**找活干**，是应用所学的最有效方式，有活干，所以就有问题需要解决，所以就有机会反复攻关，在这个过程中，以用带练……

所以，很多人在很多事儿上都想反了。人们常常取笑那些呼哧呼哧干活的人，笑着说，“能者多劳”，觉得他们有点傻。
这话真的没错。

但，这么说更准：**劳者多能** —— 你看，都想反了吧？

到最后，一切自学能力差的人，外部的表现都差不多，都起码包括这么一条：眼里没活。他们也不喜欢干活，甚至也没想过，玩乐也是干活（每次逢年过节玩得累死那种） —— 从消耗或者成本的角度来看根本没啥区别 —— 只不过那些通常都是没有产出的活而已。

把自学当作一门手艺，把所有的技能也都当作一门手艺，那就相对容易理解了：
- **全面，是掌握一门手艺的基本。**

为了全面，当然要靠时间。所以，关于“混与不混”，我们有了更深刻却又更朴素的认识：
- **所谓的不混时间，无非就是刻意练习、追求全面。**

也正是这个原因，几乎所有自学高手都懂这个道理：
- **绝对不能只靠一本书**

总有一天你会明白的，一切的“学会”和“学好”之间的差异，无非是全面程度的差异。
于是，翻译过来，“学好”竟然如此简单：
- **多读几本书。狠一点，就是多读很多本书。**

提高对所学知识技能的“全面程度”，有个最狠的方法 —— 再次说出来不惊人，但实际效果惊到爆：
- **教是最好的学习方法。**

搞来搞去，计算机行业里有个著名的词汇诞生：全栈工程师。
其实，所有精湛的手艺人，都是**全栈**，不信你就仔细观察一下。
于是，所有在入门、进阶之后走得更远的手艺人，都明白且认同这个道理：
- **学无止境**

于是，最后一个重要技巧，不仅仅是“不断磨练当前的手艺”，还有就是不断向所有的手艺人学习。
再进一步，技巧没用了……

想再进一步，靠的是另外一个层次的东西 —— 那就是**尊重与热爱**。

关于**学——练——用——造**大法
- 你一定要想办法启动自学，否则你没有未来；
- 你把自学当作一门手艺，长期反复磨练它；
- 你懂得学、练、用、造各个阶段之间的不同，以及针对每个阶段的对应策略；
- 面对“过早引用”过多的世界，你有你的应对方式；
- 你会“囫囵吞枣”，你会“重复重复再重复”，你深刻理解“读书百遍其义自见”；
- 以后你最擅长的技能之一就是拆解拆解再拆解；
- 你用你的拆解手艺把所有遇到的难点都拆解成能搞定的小任务；
- 自学任何一门手艺之前你都不会去问“有什么用”，而是清楚地知道，无论是什么只要学会了就只能也必然天天去用；
- 你没有刚需幻觉，你也没有时间幻觉，你更没有困难幻觉，反正你就是相对更清醒；
- 不管你新学什么手艺，你都知道只要假以时日你就肯定能做好，因为所有的手艺精湛，靠的只不过是充足的预算；
- 你知道如何不浪费生命，因为只要不是在刻意练习、不是在刻意思考，那就是在“混时间”；
- 你总是在琢磨你能做个什么新作品；
- 你刻意地使用你的作品作为有效社交工具，也用作品去过滤无效社交；
- 你乐于分享，乐于阅读也更乐于写作 —— 因为这世界怎么帮助你的，你就想着要怎样回报；
- 你把全面和完整当作最高衡量标准，也用这个标准去克制、应对自己的注意力漂移；
- 你会不断自学新的手艺，因为你越来越理解单一技能的脆弱，越来越理解多项技能的综合威力；
- 你越来越依赖互联网，它是你最喜欢的“书”，而Google 是你最好的朋友 —— 他总是能帮你找到更好的老师；
- 偶尔，你会学会没人教、没人带、甚至没书可参考的手艺，别人都说你“悟性”高，可你自己清楚地知道那其实是怎么回事儿；
- 你越来越明白，其实没什么“秘密”，越简单、越朴素的道理越值得重视；
- 你发现你用来思考的时间越来越多 —— 准确地讲，是“琢磨”…… 只不过是因为你真会琢磨了 —— 你很清楚你应该花时间琢磨的是什么。


## 使用jupyter lab
启动方法
```bash
cd ~
jupyter lab
```
- 写文档和调试代码两不误！！！

jupyter lab的两个插件：
- @jupyterlab/toc    为正文内容生成一个导航栏
- ryantam626/jupyterlab_sublime  设置键盘映射

在jupyter prompt中安装插件：
```bash
jupyter labextension install @jupyterlab/toc
jupyter labextension install @ryantam626/jupyterlab_sublime
jupyter lab build
```

## 关于浏览器支持的CSS样式定制插件
建议Stylus 这类终端 CSS 定制插件

谷歌浏览器无法访问到国外的插件更新服务，在这里不妨改为使用Firefox吧。
以下为作者共享的一个Stylus下的CSS样式配置示例：
```CSS
a {color: #2456A4 !important;}strong {color:#6392BF;}em {color: #A9312A; font-style: normal !important;}table {font-size: 90% !important;}

#jp-main-dock-panel {background-color: #f9f9f9;}
.jp-RenderedHTMLCommon {font-family: "Yuanti SC"; font-size: 100%;}
.jp-Notebook {background-color: #fbfafa;}
.CodeMirror,
.jp-RenderedHTMLCommon pre {font-size: 90%;}
.jp-RenderedHTMLCommon pre {
padding: 10px 25px;
background-color: #fafafa;
border-left: 4px solid #dadada;
border-radius: 10px;}

.jp-RenderedHTMLCommon pre code {
background-color: #fafafa;}

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
border-radius: 4px;}
```

## 使用conda管理环境
创建环境名称为py3，并安装最新版本的Python3在终端中输入：
```bash
conda create -n py3 python=3
```
或也可以这样创建环境名称为py2，并安装最新版本的Python2：
```bash
conda create -n py2 python=2
```
在 Windows 上，你可以使用 activate my_env进入。在 OSX/Linux 上使用 source activate my_env 进入环境。

**共享环境：**

conda的方法
```bash
conda env export > environment.yaml 将你当前的环境保存到文件中包保存为YAML文件（包括Pyhton版本和所有包的名称）。
```
传统方法
```bash
pip freeze > environment.txt 使用pip将一个 txt文件导出并包括在其中。
```

## 需要掌握的git使用技巧
- 执行命令 git remote -v 查看你的远程仓库的路径
- 指定一个上级仓库 git remote add upstream https://github.com/selfteaching/the-craft-of-selfteaching.git
- 执行命令 git status 检查本地是否有未提交的修改

以下为merge上级仓库更新的方法
- 执行命令 git fetch upstream 抓取 xiaolai 原仓库的更新
- 执行命令 git checkout master 切换到 master 分支
- 执行命令 git merge upstream/master 合并远程的master分支
- 执行命令 git push 把本地仓库向github仓库（你fork到自己名下的仓库）推送修改

以上，现在你已经解决了fork的仓库和原仓库版本不一致的问题。可以放心向 xiaolai 发起 pull request 了。
如果有无法解决的一致性冲突，建议删除了fork出来的仓库，重新开始。

## Python关键字参数
在 Python 中，函数的参数，有两种：
- **位置参数**（Positional Arguments，在官方文档里常被缩写为 arg）
- **关键字参数**（Keyward Arguments，在官方文档里常被缩写为 karg）

在函数定义中，带有 = 的，即，已为其设定了默认值的参数，叫做 Keyword Arguments，其它的是 Positional Arguments。

在调用有 Keyword Arguments 的函数之时，如若不提供这些参数，那么参数在执行时，启用的是它在定义的时候为那些 Keyword Arguments 所设定的默认值；如若提供了这些参数的值，那么参数在执行的时候，启用的是接收到的相应值。

## 为了学会使用 Python，你以后最常访问的页面
对初学者最重要的两个链接是：
- Tutorial: https://docs.python.org/3/tutorial/index.html
- Library Reference: https://docs.python.org/3/library/index.html

或者下载已经转换好的版本
```bash
cd ~/Downloads
git clone https://github.com/xiaolai/the-python-tutorial-in-other-formats.git
```
html格式便于浏览，ipynb格式便于边浏览边调试实验用的代码。

反复阅读查询的页面肯定是其中的这两个：
- https://docs.python.org/3/library/functions.html
- https://docs.python.org/3/library/stdtypes.html

## 字符串格式化更好的方法
使用str.format()
```python
name = 'John'
age = 25'
{} is {} years old.'.format(name, age)
```
使用使用 f-string
```python
name = 'John'
age = 25
f'{name} is {age} years old.'
f'{name} is a grown up? {age >= 18}'
```

## Python的源码以及优秀的示例程序
Python 的代码是开源的，它的代码仓库在 Github 上：
https://github.com/python/

在这个代码仓库中，有一个目录下，保存着若干 Python Demo 程序：https://github.com/python/cpython/tree/master/Tools/demo

以下几个程序建议都精读一下，看看自己的理解能力：
- [beer.py](https://github.com/python/cpython/blob/master/Tools/demo/beer.py) Well-known programming example: Bottles of beer.
- [eiffel.py](https://github.com/python/cpython/blob/master/Tools/demo/eiffel.py) Python advanced magic: A metaclass for Eiffel post/preconditions.
- [hanoi.py](https://github.com/python/cpython/blob/master/Tools/demo/hanoi.py) Well-known programming example: Towers of Hanoi.
- [life.py](https://github.com/python/cpython/blob/master/Tools/demo/hanoi.py) Curses programming: Simple game-of-life.
- [markov.py](https://github.com/python/cpython/blob/master/Tools/demo/markov.py) Algorithms: Markov chain simulation.
- [queens.py](https://github.com/python/cpython/blob/master/Tools/demo/queens.py) Well-known programming example: N-Queens problem.

## 关于为函数、变量取名所需要的注意事项
- [PEP 8 -- Style Guide for Python Code: Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)
- [PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)

## 关于函数的参数
如果你在定义参数的时候，在一个位置参数（Positional Arguments）前面标注了星号，*，那么，这个位置参数可以接收一系列值，在函数内部可以对这一系列值用 for ... in ... 循环进行逐一的处理。

带一个星号的参数，英文名称是“Arbitrary Positional Arguments”，姑且翻译为“随意的位置参数”。还有带两个星号的参数，英文名称是“Arbitrary Keyword Arguments”，姑且翻译为“随意的关键字参数”。

在调用函数的时候，我们是可以将一个容器传递给函数的 Arbitrary Positional Arugments 的 —— 做法是，在调用函数的时候，在参数前面加上星号 *：

```python
def say_hi(*names):
for name in names:
print(f'Hi, {name}!')```
names = ('mike', 'john', 'zeo')say_hi(*names)

- 注意：一个函数中，可以接收一系列值的位置参数只能有一个；并且若是还有其它位置参数存在，那就必须把这个可以接收一系列值的位置参数排在所有其它位置参数之后。

设定一个可以接收很多值的关键字参数（Arbitrary Keyword Argument）:
```python
def say_hi(**names_greetings):
for name, greeting in names_greetings.items():
print(f'{greeting}, {name}!')
say_hi(mike='Hello', ann='Oh, my darling', john='Hi')

def say_hi(**names_greetings):
for name, greeting in names_greetings.items():
print(f'{greeting}, {name}!')
a_dictionary = {'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'}
say_hi(**a_dictionary)

say_hi(**{'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'})
```

面对许多参数，Python 需要按照既定的规则（即，顺序）判定每个参数究竟是哪一类型的参数：
Order of Arguments：
1. Positional
2. Arbitrary Positional
3. Keyword
4. Arbitrary Keyword

## Docstring-函数的文档
在函数定义内部，我们可以加上 Docstring；将来函数的“用户”就可以通过 help() 这个内建函数，或者 .__doc__ 这个 Method 去查看这个 Docstring，即，该函数的“产品说明书”。

Docstring 如若存在，必须在函数定义的内部语句块的开头，也必须与其它语句一样保持相应的缩进（Indention）。

简要总结一下 PEP 257 中必须掌握的关于函数文档的规范：
1. 无论是单行还是多行的 Docstring，一概使用三个双引号扩起；
2. 在 Docstring 内部，文字开始之前，以及文字结束之后，都不要有空行；
3. 多行 Docstring，第一行是概要，随后空一行，再写其它部分；
4. 完善的 Docstring，应该概括清楚以下内容：参数、返回值、可能触发的错误类型、可能的副作用，以及函数的使用限制等等；
5. 每个参数的说明都使用单独的一行……

**Sphinx 版本的 Docstring 规范**

Sphinx 可以从 .py 文件里提取所有 Docstring，而后生成完整的 Documentation。适合在大型项目中使用。
Sphinx 使用自己的一种标记语言，reStructureText，文件尾缀使用 .rst 。

## 有关开发方法论
**MoSCoW**

在开发方法论中，有一个叫做 MoSCoW Method 的东西，1994 年由 Clegg Dai 在《 Case Method Fast-Track: A RAD Approach》一书中提出的 —— 两个 o 字母放在那里，是为了能够把这个缩写读出来，发音跟莫斯科一样。

简单说，就是，凡事儿都可以分为：
- Must have
- Should have
- Could have
- Won't have

于是，在开发的时候，把所谓的需求打上这 4 个标签中的某一个，以此分类，就很容易剔除掉那些实际上做了还不如不做的功能……

一个 Wikipedia 上的链接列表，在编程领域里，有无数可以借鉴到生活中的哲学、方法论：
- [If it ain't broke, don't fix it](https://en.wikipedia.org/wiki/Bert_Lance#If_it_ain't_broke,_don't_fix_it)
- [KISS principle](https://en.wikipedia.org/wiki/KISS_principle)
- [Don't repeat yourself](https://en.wikipedia.org/wiki/Don't_repeat_yourself)
- [Feature creep](https://en.wikipedia.org/wiki/Feature_creep)
- [List of software development philosophies](https://en.wikipedia.org/wiki/List_of_software_development_philosophies)
- [Minimum viable product](https://en.wikipedia.org/wiki/Minimum_viable_product)
- [MoSCoW method](https://en.wikipedia.org/wiki/MoSCoW_method)
- [Overengineering](https://en.wikipedia.org/wiki/Overengineering)
- [Worse is better](https://en.wikipedia.org/wiki/Worse_is_better)
- [S.O.L.I.D.](https://en.wikipedia.org/wiki/SOLID)
- [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)

## About Class
当我们作为用户想了解一个 Class 的 Interface，即，它的 Attributes 和 Methods 的时候，常用的有三种方式：
- help(object)
- dir(object)
- object.__dict__

三个 Python 的内建函数：
- hasattr(object, attr) 查询这个 object 中有没有 这个 attr，返回布尔值
- getattr(object, attr) 获取这个 object 中这个 attr 的值
- setattr(object, attr, value) 将这个 object 中的 attr 值设置为 value

Python 的定义，变量名前面加上下划线（Underscore）一个以上 _ 的话，那么该变量是**“私有变量”（Private Variables）**，不能被外部引用。而按照 Python 的惯例，我们会使用两个下划线起始，去命名私有变量，如： __life_span。

私有变量的使用与封装

如果，你希望外部能够像获得 Class 的属性那样，直接写 g.population，而不是必须加上一个括号 g.population() 传递参数（实际上传递了一个隐含的 self 参数），那么可以在 def population(self): 之前的一行加上一句 @property（原理上应该是为函数设置了一个装饰器，实现类似属性方式的访问）：
```python
class Golem:
__population = 0
...

@property
def population(self):
return Golem.__population
```
如此这般之后，你就可以用 g.population 了
```python
g = Golem('Clay')
g.population
```
此时再给g.population 赋值会报错。

如果你非得希望从外部可以设置这个值，那么，你就得再写个函数，并且在函数之前加上一句(另外一个装饰器？)：
```python
...

@property
def population(self):
return Golem.__population

@population.setter
def population(self, value):
Golem.__population = value
```
这样之后，.population 这个 Attribute 就可以从外部被设定其值了

## 写一个迭代器
**方法一：使用Class**

迭代器是个 Object，所以，写迭代器的时候写的是 Class，比如，我们写一个数数的迭代器，Counter：
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
    print(c, sep=', ')type(Counter)
```
- 这里的重点在于两个函数的存在，__iter__(self) 和 __next__(self)。

```python
def __iter__(self):
    return self
```
- 这两句是约定俗成的写法，写上它们，Counter 这个类就被会被识别为 Iterator 类型。而后再有 __next__(self) 的话，它就是个完整的迭代器了。

**方法二：使用生成器（Generator）**

```python
def counter(start, stop):
    while start <= stop:
        yield start
        start += 1
for i in counter(101, 105):
    print(i)
```
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator 。

一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。

> 迭代器，生成器和yield的定义与使用技巧可以参考下面这篇文章：
> Python yield 使用浅析 https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/

**了解下生成器表达式**
```python
even = (e for e in range(10) if not e % 2)
# odd = (o for o in range(10) if o % 2)
print(even)
for e in even:
    print(e)
```
输出：
```
<generator object <genexpr> at 0x107cc0048>
0
2
4
6
8
```

## 写一个装饰器
最常用的场景就是用来改变其它函数的行为。
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

## 正则表达式的使用
目前（2019）网上最方便的 Regex 测试器，是 [regex101.com](https://regex101.com/)

关于字符串前面的r字符的作用：

在 Python 代码中，写 Pattern 的时候，之所以要在字符串 '...' 之前加上 r，写成 r'...'，这代表使用raw string格式识别这个字符串。因为如果不用 raw string 的话，那么，每个转义符号都要写成 \\；如果用 raw string，转义符号就可以直接使用 \ 本身了。

re.findall(pttn, str) 的意思是说，把 str 中所有与 pttn 这个规则一致的字符串都找出来：
```python
import re
with open('regex-target-text-sample.txt', 'r') as f:
    str = f.read()
    pttn = r'beg[iau]ns?'
    re.findall(pttn, str)
```
Out[5]:
['begin', 'began', 'begun', 'begin']

以下字符在 Regex 中都有特殊含义：
```
\ + * . ? - ^ $ | ( ) [ ] { } < >
```
**操作符、操作元、原子**

**集合原子**

标示集合原子，使用方括号 []。[abc] 的意思是说，“a or b or c”，即，abc 中的任意一个字符。

在方括号中，我们可以使用两个操作符：-（区间）和 ^（非）。
- [a-z] 表示从小写字母 a 到小写字母 z 中的任意一个字符。
- [^abc] 表示 abc 以外的其它任意字符，即，非[abc] 。


注意，一个集合原子中，^ 符号只能用一次，只能紧跟在 [ 之后。否则不起作用。

**类别原子**

类别原子，是指那些能够代表“一类字符”的原子，它们都得使用转义符号再加上另外一个符号表达，包括：
- \d 任意数字；等价于 [0-9]
- \D 任意非数字；等价于 [^0-9]
- \w 任意本义字符；等价于 [a-zA-z0-9_]
- \W 任意非本义字符；等价于 [^a-zA-z0-9_]
- \s 任意空白；相当于 [ \f\n\r\t\v] （注意，方括号内第一个字符是空格符号）
- \S 任意非空白；相当于 [^ \f\n\r\t\v] （注意，紧随 ^ 之后的是一个空格符号）
- . 除 \r \n 之外的任意字符；相当于[^\r\n]

类别原子挺好记忆的，如果你知道各个字母是哪个词的首字母的话：
-  d 是 digits
-  w 是 word characters
-  s 是 spaces

另外，在空白的集合[ \f\n\r\t\v]中：
- f 是分页符；
- \n \r 是换行符；
- \t 是制表符；
- \v 是纵向制表符（很少用到）。

各种关于空白的转义符也同样挺好记忆的，如果你知道各个字母是那个词的首字母的话：
- f 是 flip
- n 是 new line
- r 是 return
- t 是 tab
- v 是 vertical tab

**边界原子**

我们可以用边界原子指定边界。也可以称作“定位操作符”。
- ^ 匹配被搜索字符串的开始位置；
- $ 匹配被搜索字符串的结束位置；
- \b 匹配单词的边界；er\b，能匹配 wonderer 中的 er，却不能匹配 error 中的 er；
- \B 匹配非单词边界；er\B，能匹配 error 中的 er，却不能匹配 wonderer 中的 er。

注意：^ 和 $ 在 Python 语言中被 \A 和 \Z 替代。

**组合原子**

我们可以用圆括号 () 将多个单字符原子组合成一个原子 —— 这么做的结果是，()内的字符串将被当作一整个原子，可以被随后我们要讲解的数量操作符操作。另外，() 这个操作符，有两个作用：组合（Grouping）；捕获（Capturing)。

注意区别， er、[er] 和 (er)) 各不相同。
-  er 是两个原子，'e' 和紧随其后的 'r'
-  [er] 是一个原子，或者 'e' 或者 'r'；
-  (er) 是一个原子，'er'

**数量操作符**

数量操作符有： + ? * {n, m}。

它们是用来限定位于它们之前的原子允许出现的个数；不加数量限定则代表出现一次且仅出现一次：
- \+ 代表前面的原子必须至少出现一次，即：出现次数 ≧ 1

> 例如，go+gle可以匹配google gooogle goooogle等;

- ? 代表前面的原子最多只可以出现一次，即：0 ≦ 出现次数 ≦ 1

> 例如，colou?red可以匹配colored或者coloured;

- \* 代表前面的原子可以不出现，也可以出现一次或者多次，即：出现次数 ≧ 0

> 例如，520*可以匹配520 52000 5200000 520000000000等。

- {n} 之前的原子出现确定的 n 次；
- {n,} 之前的原子出现至少 n 次；
- {n, m} 之前的原子出现至少 n 次，至多 m 次

数量操作符是对它之前的原子进行操作的，换言之，数量操作符的操作元是操作符之前的原子。

**或操作符 |**

或操作符 | 是所有操作符中优先级最低的，数量操作符的优先级比它高，所以，在 | 前后的原子被数量操作符（如果有的话）操作之后才交给 | 操作。

在集合原子中（即，[] 内的原子）各个原子之间的关系，只有“或” —— 相当于方括号中的每个原子之间都有一个被省略的 |。
- 注意：中括号的 | 不被当作特殊符号，而是被当作 | 这个符号本身。在中括号中的圆括号，也被当作圆括号 () 本身，而无分组含义。

**匹配并捕获**

捕获（Capture），使用的是圆括号()。使用圆括号得到的匹配的值被暂存成一个带有索引的列表，第一个是 $1，第二个是 $2…… 以此类推。随后，我们可以在替换的过程中使用 $1 $2 中所保存的值。
- 注意：在 Python 语言中调用 re 模块之后，在 re.sub() 中调用被匹配的值，用的索引方法是 \1、\2…… 以此类推。

**非捕获匹配**

有时，你并不想捕获圆括号中的内容，在那个地方你使用括号的目的只是分组，而非捕获，那么，你就在圆括号内最开头加上 ?: —— (?:...)：

非捕获匹配，还有若干个操作符：
- (?=pattern) 正向肯定预查
- (?!pattern) 正向否定预查（negative assert）
- (?<=pattern)  反向（look behind）肯定预查
- (?<!pattern) 反向否定预查


**几个最常用的 Regex**

以下是几个常用的 Regex，值得保存：
- matching username [/^[a-z0-9_-]{3,16}$/](https://regexper.com/#%2F%5E%5Ba-z0-9_-%5D%7B3%2C16%7D%24%2F)
- matching password[3] [/^[a-z0-9_-]{6,18}$/](https://regexper.com/#/^[a-z0-9_-]{6,18}$/)
- matching an IP address [/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/](https://regexper.com/#/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/)

https://regexper.com/ 这个网站可以提供正则表达式的图形化展示，对理解有帮助。

## BNF 以及 EBNF
比如，什么是符合语法的整数（Integer）呢？符合以下语法描述的是整数（使用 Python 的 EBNF）：
```
integer ::= [sign] [digit]*
sign ::= "+" | "-"
digit ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```
以上的描述中，基本符号没几个，它们各自的含义是：
- ::= 表示定义；
- < > 尖括号里的内容表示必选内容；
- `[ ]` 中是可选项；
- " " 双引号里的内容表示字符；
- | 竖线两边的是可选内容，相当于or；
- \+ 表示零个或者一个……
- \* 表示一个或者多个……

**glob**，是 Global 的缩写。

你可以把它理解为“超级简化版正则表达式” —— 它最初是 Unix/Posix 操作系统中用来匹配文件名的“通配符”。

glob 的主要符号只有这么几个：
- *
- ?
- [abc]
- [^abc]

## 这些符号都代表什么？
把下面的表格打印出来，整理一下，在表格里填写每个符号在 Python 中都是用来做什么的？

- Mac book使用这个文件：https://github.com/watermelonbig/the-craft-of-selfteaching/raw/master/symbols.numbers
- Windows下使用这个文件：

以后不管学什么语言，就拿这个表格过一遍，到时候只有一个感觉：越学越简单！

## 下一步干什么？
理论上，下一步你的选择很多。自学是门手艺，你可以用它去学任何你想要掌握的其它手艺。如果，你有意在编程这个领域继续深入，那么，以下就是一些不错的线索。

当然，最先应当做的是，去检查一下自己的“突击”的结果，去 [Pythonbasics.org](http://pythonbasics.org/) 做做练习：https://pythonbasics.org/Exercises/

除了我在这里介绍的之外，请移步 The Hitchhiker's Guide to Python，它更为全面：[https://docs.python-guide.org/](https://docs.python-guide.org/)


**Python 必读书籍**

无论学什么，一本书肯定不够，以下是学习 Python 的基本必读书籍：
- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
- [Think Python: How to think like a computer scientist](http://greenteapress.com/wp/think-python-2e/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com)
- [Effective Python](https://effectivepython.com)
- [Python Cookbook](https://www.amazon.com/Python-Cookbook-Recipes-Mastering-ebook/dp/B00DQV4GGY)
- [Fluent Python](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming-ebook/dp/B0131L3PW4)
- [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html)
- [Mastering Object-oriented Python - Transform Your Approach to Python Programming](https://www.amazon.com/dp/B00JVQ14UO/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)

更多 Python 书籍：https://pythonbooks.revolunet.com

千万别觉得多，只要真的全面掌握，后面再学别的，速度上都会因此快出很多很多……

**Python Cheatsheet**

你已经知道了，这种东西，肯定是自己整理的才对自己真的很有用…… 不过，你也可以把别人整理的东西当作“用来检查自己是否有所遗漏”的工具。
网上有无数 Python Cheatsheets，以下是 3 个我个人认为相当不错的：
- [Comprehensive Python Cheatsheet](https://gto76.github.io/python-cheatsheet/)
- [Python Crash Course - Cheat Sheets](https://github.com/ehmatthes/pcc/tree/master/cheat_sheets)
- [Pysheeet](https://www.pythonsheets.com)

**Awesome Python**

Github 上的“居民”现在已经养成了一个惯例，无论什么好东西，他们都会为其只做一个“Awesome ...”的页面，在里面齐心协力搜集相关资源。比如，你想学 Golang，那你去 Google 搜索 Awesome Go，一定会给你指向到一个 Github 上的 “Awesome Go”的页面……

以下是 Awesome Python 的链接：https://github.com/vinta/awesome-python

**全栈工程师路径图**

既然学了，就肯定不止 Python —— 在扎实的基础之上，学得越多学得越快。以下是一个“全栈工程师路径图”，作者是位迪拜的帅哥 Kamran Ahmed：
https://github.com/kamranahmedse/developer-roadmap
