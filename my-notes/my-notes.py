# Part.1.E.1.entrance note-chaxiaoli
1 逻辑操作符（Logical Operators）
	比较操作符:== != > >= < <= in
	运算对象（Operands）:数字值和字符串值
	返回值：布尔值		

2 布尔运算操作符:
	与and 或or 非not
	布尔值：True False
	
3 流程控制（Control Flow）:
	分支：if/else 语句
	for循环（loop）
	r=2 #将整数常量（Literal）2赋值（Assignment）给变量（Variable）r

4 函数（Functions）
	函数名（Function Name）、参数（Parameters）、返回值（Return Value）、调用（Call）
	程序：核心构成部分就是输入、处理、输出。
	子程序（Sub-Program）：主程序执行到函数调用时，就开始执行实现函数的那些代码，而后再返回主程序
	
5 其他：
	语句：
		一个完整的程序，由1个或多个语句（statements）构成
	语句块：
		行首空白（Leading whitespace）：由空格 `' '` 或者 Tab `⇥` 构成
		Python将认为这一行与其他邻近有着相同行首空白的语句同属于一个**语句块**;
		而一个语句块必然由一个行末带有冒号 `:` 的语句起始;同属于一个语句块中的语句，行首空白数量应该相等
	注释：
		#
	操作符：
		加+、减-、乘*、除/、商//、余%、幂**
		x = x + 1可以写为X += 1
		被除数÷除数=商··· ···余数

# Part.1.E.2.values-and-their-operators note-chaxiaoli
1 计算机程序，都由且只由两个最基本的成分构成：
	运算（Evaluation）
	流程控制（Control Flow）
	
2 值：
	运算（Evaluation）：算出某个值究竟是什么，如a = 1 + 2 * 3
	常量（Literals）：如1,2,3
	变量（Variables）：必须先赋值才能使用，如a
	操作符（Operators）：对其左右的值进行相应的运算而后得到一个值，如+，*
	赋值（Assignment）：将它右边的值保存到左边的变量中，如=
	python中，每个函数都有返回值，即便你在定义一个函数的时候没有设定返回值，它会加上默认的返回值 None
	调用（Call）：我们把一个值交给某个函数，请函数根据它内部的运算和流程控制对其进行操作而后返回另外一个值。
	
3 值的类型：
	最基本的三种数据类型：
		布尔值（Boolean Value)
		数字（Numbers）：整数（Int）、浮点数（Float）、复数（Complex Numbers）
		字符串（Strings）
		# range,list,tuple,set,dict
	运算的默认法则：通常情况下应该是相同类型的值才能相互运算
	Type Casting（类型转换）：
		将字符串转换为数字用 int()、float()；
		将数字转换成字符串用 str()；
	数字间转换：
		将整数转换成浮点数字用 float()
		将浮点数字转换成整数用 int()
	查看数据类型：
		type()

4 操作符：
	针对不同类型的数据，有各自专用的操作符：
		如对于数字进行加、减、乘、除、商、余、幂的操作，对于字符串进行拼接、拷贝、属于的操作，对布尔值进行或、与、非的操作。
	数值操作符：数字
		加减乘除商余幂：+、-、*、/、//、%、**（+，-可以对单个值进行操作）
		优先级：+、- （两个值）小于 *、/、//、% 小于+、- （单个值）小于 **
	布尔值操作符：布尔值
		优先级：最低的是或 or，然后是与 and, 最高的是非 not
	逻辑操作符：数值比较，返回布尔值
		<（小于）、<=（小于等于）、>（大于）、>=（大于等于）、!=（不等于）、==（等于）
	优先级：数值计算的操作符最高>逻辑操作符>布尔值的操作符
	
	字符串操作符：
		拼接：+ 和 ' '（后者是空格）
		拷贝：*
		逻辑运算：in、not in；以及逻辑操作符，<、<=、>、>=、!=、==
			字符对应着 Unicode 码，字符在被比较的时候，被比较的是对应的 Unicode 码
			当字符串被比较的时候，将从两个字符串各自的第一个字符开始逐个比较，“一旦决出胜负马上停止”

	列表的操作符：
		容器（Container）：用来容纳批量的数据
		字符串：也是容器的一种，它的里面容纳着批量的字符，有序容器
		列表（List）：[]，有序容器
		列表的操作符：
			拼接：+ 和 ' '（后者是空格）
			拷贝：*
			逻辑运算：in、not in；以及，<、<=、>、>=、!=、==
			两个列表在比较时（前提是两个列表中的数据元素类型相同），遵循的还是跟字符串比较相同的规则：“一旦决出胜负马上停止”；
			比较时，类型不同会引发 TypeError
	
5 更复杂的运算:
		内建函数（Built-in Functions）：
			abs()绝对值	delattr()	hash()	memoryview()	set()
			all()	dict()	help()	min()	setattr()
			any()	dir()	hex()	next()	slice()
			ascii()	divmod()	id()	object()	sorted()
			bin()	enumerate()	input()	oct()	staticmethod()
			bool()	eval()	int()	open()	str()
			breakpoint()	exec()	isinstance()	ord()	sum()
			bytearray()	filter()	issubclass()	pow()	super()
			bytes()	float()	iter()	print()	tuple()
			callable()	format()	len()	property()	type()
			chr()	frozenset()	list()	range()	vars()
			classmethod()	getattr()	locals()	repr()	zip()
			compile()	globals()	map()	reversed()	import()
			complex()	hasattr()	max()	round()	
		调用标准库（Standard Library）中的 math 模块（Module）：
			import math
			math.sin(5)  # .可以被理解为 “操作符”，它的作用是：从其它模块中调用函数。
			# 把 5 这个值，传递给 math 这个模块里的 sin() 函数，让 sin() 根据它内部的代码对这个值进行运算，而后返回一个值（即，计算结果）
		类（Class）中定义的函数，也可以这样被调用
	
6 布尔值的补充：
		每个变量或者常量，除了它们的值之外，同时还相当于有一个对应的布尔值。
		Here are most of the built-in objects considered False:
			constants defined to be false: None and False.
			zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
			empty sequences and collections: '', (), [], {}, set(), range(0)
	
7 值的类型的补充：
		基础数据类型：数字、布尔值、字符串
		基础数据类型的组合：列表（list），还有range()（等差数列）、tuple（元组）、set（集合）、dictionary（字典），Date Type（日期）等等。
			相互运算前要 _Type Casting_，比如将 List 转换为 Set：set()，反之，list()
		
8 备注：
		关于表达式：https://docs.python.org/3/reference/expressions.html
		关于所有操作的优先级：https://docs.python.org/3/reference/expressions.html#operator-precedence
		上一条链接不懂 BNF 的话根本读不懂：https://en.wikipedia.org/wiki/Backus-Naur_form
		Python 的内建函数：https://docs.python.org/3/library/functions.html
		Python 的标准数据类型：https://docs.python.org/3/library/stdtypes.html
	
# Part.1.E.3.controlflow note-chaxiaoli
1 流程控制：分支与循环
2 if 语句
3 for 循环：Python 语言中，for 循环不使用其它语言中那样的计数器，取而代之的是 range() 这个我称其为 “整数等差数列生成器” 的函数。
4 range() 函数
	range(_stop_) #只有一个参数的时候，这个参数被理解为 stop，生成一个从 0 开始，到 stop - 1 的整数数列。
	range(_start, stop[, step]_)
5 Continue、Break 和 Pass
	在循环的过程中，还可以用 continue 和 break 控制流程走向，通常是在某条件判断发生的情况下
	continue 语句：将忽略其后的语句开始下次循环
	break 语句：将从此结束当前循环，开始执行循环之后的语句.
		for 语句块还可以附加一个 else,附加在 for 结尾的 else 语句块，_在没有 break 发生的情况下会运行_。
	pass语句：什么都不干，更多是给写程序的人用的，可以用 pass 占位，而后先写别的部分。
6 while循环
	两种循环结构：
	Collection-controlled loops（以集合为基础的循环）：for ... in ...。更适合处理序列类型的数据（Sequence Type）的迭代
	Condition-controlled loops（以条件为基础的循环）:while循环。更为灵活，因为它后面只需要接上一个逻辑表达式即可。
7 总结：
	只处理一种情况，用 if ...
	处理 True/False 两种情况，用 if ... else ...
	处理多种情况，用 if ... elif ... elif ... else ...
	迭代有序数据类型，用 for ... in ...，如果需要处理没有 break 发生的情况，用 for ... else ...
	其它循环，用 while ...
	与循环相关的语句还有 continue、break、pass
	函数从控制流角度去看其实就是子程序

# Part.1.E.3.controlflow note-chaxiaoli
