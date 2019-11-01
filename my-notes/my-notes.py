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

# Part.1.E.4.functions note-chaxiaoli
1 函数：是可被调用的完整的程序。它具备输入(参数)、处理、输出(返回值)的功能。又因为它经常在主程序里被调用，所以它总是更像是个子程序。
2 print():最基本的作用就是把传递给它的值输出到屏幕上，如果不给它任何参数，那么它就输出一个空行
	print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)
		sep=' '：接收多个参数之后，输出时，分隔符号默认为空格，' '；
		end='\n'：输出行的末尾默认是换行符号 '\n'；
		file=sys.stdout：默认的输出对象是 sys.stdout（即用户正在使用的屏幕）,可以往文件里写数据的，指定file参数为一个已经打开的文件对象
	print() 这个函数的返回值是 None
		print(print(1)):print() 
		# 这个函数被调用了两次，第一次是 print(1)，它向屏幕输出了一次，完整的输出值实际上是 str(1) + '\n'，而后返回一个值，None；
		# 而第二次调用 print()，这相当于是向屏幕输出这个 None：
3 关键字参数：
	位置参数（Positional Arguments，在官方文档里常被缩写为 arg）： 由位置决定其值的参数，被传递的值的意义就是由参数的位置决定的
	关键字参数（Keyword Arguments，在官方文档里常被缩写为 kwarg）：带有 = 的，即已为其设定了默认值的参数
	可选位置参数（Optional Positional Arguments）:
		pow(x,y[,z])。pow(x, y)：返回值是 x ** y；pow(x, y, z)：返回值是 x ** y % z；
		exec(object[, globals[, locals]])
			object：必选参数，表示需要被指定的Python代码。它必须是字符串或code对象。
			globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
			locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。
	可接收很多值的位置参数:print(*object, ...)
		可以接收很多个参数（或者说，这个位置可以接收一个列表或者元组）；
		一个函数里最多只有一个这种可以接收很多值的位置参数；
		若还有若干个位置参数，那么，能够接收很多值的位置参数只能放置最后；如max(arg1,arg2,*arg[,key])
	Class 也是函数:class bool([x])
4 总结
	你可以把函数当作一个产品，而你自己是这个产品的用户；
	既然你是产品的用户，你要养成好习惯，一定要亲自阅读产品说明书；
	调用函数的时候，注意可选位置参数的使用方法和关键字参数的默认值；
	函数定义部分，注意两个符号就行了，[] 和 =；
	所有的函数都有返回值，即便它内部不指定返回值，也有一个默认返回值：None；
	另外，一定要耐心阅读该函数在使用的时候需要注意什么 —— 产品说明书的主要作用就在这里
		
# Part.1.E.5.strings note-chaxiaoli
1 字符串
	In [1]:1+2
	Out[1]:3.3000000000000003 #最终所有的值都要转换成二进制.此时小数的精度就有损耗，多次浮点数字转换成二进制相互运算之后
		 # 再从二进制转换为十进制之后返回的结果，精度损耗就更大了。因此，在计算机上，浮点数字的精度总有极限。
	字符串：由 0 个字符或者多个字符构成，最终也要被转换成数值，再进一步被转换成二进制数值。
	空字符串的值是 None，即便是这个 None —— 也最终还是要被转换成二进制的 0。
2 字符码表的转换
	ASCII码表：以前计算机的中央处理器最多只能够处理 8 位二进制数值，所以，那时候的计算机只能处理 2^8 个字符
	Unicode码表：现在计算机的中央处理器，大多是 64 位的，所以可以使用 2^64 容量的码表
	ord():把单个字符转换成码值的函数,只接收单个字符，否则会报错
	chr():只接收一个整数作为参数，而后返回相应的字符
3 字符串的标识
	单引号、用双引号，用三个单引号或者三个双引号
4 字符串与数值之间的转换
	由数字构成的字符串，可以被转换成数值，转换整数用 int(只能是整数)，转换浮点数字用 float()。
		注：int() 在接收字符串为参数的时候，只能做整数转换。
	str()，可以将数值转换成字符串类型。
	input() 接收用户的键盘输入，返回字符串。# 它可以接收一个字符串作为参数，会把这个参数输出到屏幕，作为给用户的提示语。
	# 这个参数是可选参数，直接写 input()，即没有提供参数，那么它在要求用户输入的时候，就没有提示语。
5 转义符（Escaping Character）
	也称为 “脱字符”，\
	\t 代表制表符（就是用 TAB ⇥ 键敲出来的东西），\n 代表换行符（就是用 Enter ⏎ 敲出来的东西）
6 字符串的操作符：
	拼接：空格“ ”或“+”
	复制：与整数倍操作符 * 操作
	逻辑：用in和not in操作符，看某个字符或者字符串是否被包含在某个字符串中，返回的是布尔值
7 字符串的索引
	字符串是由一系列的字符构成的。容器（Container）可分为有序的和无序的，字符串是容器的一种，属于有序容器。
	字符串里的每个字符，对应着一个从 0 开始的索引。比较有趣的是，索引可以是负数：
	索引操作符：[] #可提取字符串这个有序容器中的一个或多个元素，即其中的字符或字符串。 “提取” 的动作叫做 “Slicing”（切片）。
	 #索引操作符 [] 中可以有一个、两个或者三个整数参数，如果有两个参数，需要用 : 隔开。它最终可以写成以下 4 种形式：
		s[index] —— 返回索引值为 index 的那个字符
		s[start:] —— 返回从索引值为 start 开始一直到字符串末尾的所有字符
		s[start:stop] —— 返回从索引值为 start 开始一直到索引值为 stop 的那个字符之前的所有字符
		s[:stop] —— 返回从字符串开头一直到索引值为 stop 的那个字符之前的所有字符
		s[start:stop:step] —— 返回从索引值为 start 开始一直到索引值为 stop 的那个字符之前的，以 step 为步长提取的所有字符
		 注：无论是 range(1,2)，或者 random.randrange(100, 1000) 又或者 s[start:stop] 都有一个相似的规律：
			包含左侧的 1, 100, start，不包含右侧的 2, 1000, stop。
8 处理字符串的内建函数
	把字符串当做处理对象的有：ord()、input()、int()、float()、len()、print()
9 处理字符串的 Method
	字符串是一个对象，是 str 类（Class str）的对象。
	一个对象的内部有很多函数，叫做类的方法（Method）。
	字符串有很多可以调用的 Methods。str 类的 Methods 是使用 . 这个符号
	（1）大小写转换：
		转换字符串大小写的是 str.upper(转大写)、 str.lower(转小写) ，以及 str.casefold(转换成小写，多处理欧洲语言字符)
		句首字母大写的 str.capitalize() 和每个单词首字母大写的 str.title()，逐个字符更替大小写的 str.swapcase()
		 注：在 Python 命令行工具之中，单个下划线，是个特殊变量，保存着最近的语句或者表达式的结果，如_.lower()
		处理非英文字符串（比如中文），编码：str.encode()
	（2）搜索和替换
		str.count(sub [,start=0[, end=len(str)]])：搜寻子字符串出现次数的 Method，返回值为字符串中 sub 出现的次数。
			只给定 sub 一个参数的话，于是从第一个字符开始搜索到字符串结束；
			如果，随后给定了一个可选参数的话，那么它是 start，于是从 start 开始，搜索到字符串结束；
			如果 start 之后还有参数的话，那么它是 end；于是从 start 开始，搜索到 end - 1 结束（即不包含索引值为 end 的那个字符）。
		str.find(sub[, start[, end]])：返回字符串sub最早出现的位置index,没有找到就返回 -1
		str.rfind(sub[, start[, end]])：返回字符串sub最后出现的那次的位置,没有找到就返回 -1
		str.index(sub[, start[, end]]):作用与 find() 相同，但如果没找到的话，会触发 ValueError 异常
		str.rindex(sub[, start[, end]]):作用与 rfind() 相同，但如果没找到的话，会触发 ValueError 异常
		str.startswith(prefix[, start[, end]])：判断一个字符串是否以某个子字符串起始的
		str.endswith(suffix[, start[, end]])：判断一个字符串是否以某个子字符串结束的
		in 操作符：为了找到位置而进行搜索之前，先确认需要寻找的字符串在寻找对象中是否存在，返回布尔值
		str.replace(old, new[, count])：用 new 替换 old，替换 count 个实例
		str.expandtabs(tabsize=8)：把字符串中的 TAB（\t）替换成空格，默认是替换成 8 个空格
	 （3）去除子字符
		str.strip([chars])：参数字符串中的所有字母都会被当做需要从首尾剔除的对象，直到新的首尾字母不包含在参数中，
		参数中的字符顺序对结果没影响；没有参数，默认去除一个字符串首尾的所有空白，包括空格、TAB、换行符等。
		str.lstrip([chars])：只对左侧处理；str.rstrip([chars])：只对右侧处理。
	 （4）拆分字符串
		str.splitlines()：返回的是个列表（List）
		str.split(sep=None, maxsplit=-1)：将一个字符串，根据分隔符进行拆分，返回值是列表。
		 sep未传递参数，那么默认为用None分割（各种空白，比如，\t 和 \r 都被当作 None）；maxsplit默认值是 -1，拆分全部，0不拆分；
		str.partition()：用来根据指定的分隔符将字符串进行分割。返回一个3元的元组（分隔符左边的子串，分隔符本身，分隔符右边的子串）
	 （5）拼接字符串
		str.join(_iterable_)
	 （6）字符串排版
		str.center(width[, fillchar])：将字符串居中放置，前提是设定整行的长度；如果宽度参数小于字符串长度，则返回原字符串；
						第2个参数可选，且只接收单个字符，表示空白处的填充字符
		str.ljust(width[, fillchar]),str.rjust(width[, fillchar]):将字符串靠左或者靠右对齐放置
		str(i).zfill(num):将字符串转换成左侧由 0填充的指定长度num字符串,这在批量生成文件名的时候就很有用
	 （7）格式化字符串:
		str.format(*args, **kwargs):将特定变量插入字符串特定位置的过程
			在一个字符串中，插入一个或者多个占位符,大括号 {} 括起来；占位符中可以使用由零开始的索引
			而后将 str.format() 相应的参数，依次插入占位符中；()里可以直接写表达式
			不写占位符索引就默认每个占位符的索引从第一个开始是 0, 1, 2 ...（占位符数量 - 1)
			两个连续使用的大括号，不被认为是占位符,且只打印出一对大括号
		f-string：与 str.format() 的功用差不多，写法简洁些，在字符串标示前加字母f。但str.format()中，索引顺序可以任意指定。
		'{1} is a grown up? {0}'.format(name, age >= 18)
		f'{name} is a grown up? {age >= 18}'
	 （8）字符串属性
		返回的是布尔值，用来判断字符串的构成属性
			'1234567890'.isalnum(): True
			'abcdefghij'.isalpha(): True
			'山巅一寺一壶酒'.isascii(): False
			'0.123456789'.isdecimal(): False
			'0.123456789'.isdigit(): False
			'0.123456789'.isnumeric(): False
			'Continue'.islower(): False
			'Simple Is Better Than Complex'.isupper(): False
			'Simple Is Better Than Complex'.istitle(): True
			'	'.isprintable(): False
			'	'.isspace(): True
			'for'.isidentifier(): True

# Part.1.E.6.containers
1 数据容器（Container）
	 包括字符串、由 range() 函数生成的等差数列、列表（List）、元组（Tuple）、集合（Set）、字典（Dictionary）
	 （1）可变容器（Mutable）：列表、集合、字典
	      不可变容器（Immutable）：字符串、range() 生成的等差数列、元组。
	      集合：分为 Set 和 Frozen Set，其中，Set 是可变的，Frozen Set 是不可变的。
	 （2）有序类型（Sequence Type）：字符串、由 range() 函数生成的等差数列、列表、元组
	      无序：集合、字典
2 迭代（Iterate）
	 （1）数据容器里的元素是可以被迭代的（Iterable），它们其中包含的元素，可以被逐个访问，以便被处理。
	 （2）数据容器，有一个操作符in，用来判断某个元素是否属于某个容器。
3 列表（List）:有序类型（Sequence Type）的容器，其中包含着有索引编号的元素。
	数据清洗:遇到由不同类型数据构成的列表，想办法把不同类型的数据分门别类地拆分出来，整理清楚
	列表生成：
	a_list = []
	b_list = [1, 2, 3]
	list(), or list(iterable)            # 这是 Type Casting类型转换
	[(expression with x) for x in iterable] # List Comprehension列表生成式,可以嵌套使用 for、加上条件 if.
	eg:
	a_list = [random.randrange(1, 100) for i in range(n)]
	b_list = [x for x in a_list if x % 2 == 0]
4 列表的操作符——有序容器，同 字符串
	拼接：+（与字符串不一样的地方是，不能用空格 ' ' 了）
	复制：*
	逻辑运算：in 和 not in，<、<=、>、>=、!=、==
5 根据索引提取列表元素——可变序列，不同 字符串
	可以根据索引操作：提取、删除、替换（字符串可根据索引提取，不可删除或替换）
	# 根据索引提取（Slicing）
		print(c_list[a:b])      # 从索引 a 开始，直到索引 b 之前（不包括 6）
		print(c_list[a])        # 返回索引值为 3 的元素值
	# 根据索引删除
	del c_list[3] # del 是个命令，del c_list[3] 是一个语句；不能这么写：print(del c_list[3])
	del c_list[5:8]         
	# 根据索引替换
	c_list[1:5:2] = ['a', 2]  # s[start:stop:step] = t，跟 range 的三个参数类似；
				 # len(t) = len([start:stop:step]) 必须为真
	注：
	字符串常量（String Literal）：不可变有序容器，操作都不改变它们自身，而是在操作后返回一个值给另外一个变量。
	列表：可变容器，可以对它进行操作，结果是它本身被改变了。
6 列表可用的内建函数——容器，同字符串
	len()
	max() # 内建函数内部做了异常处理，可以在字符之间或者数字之间进行比较
	min() # 内建函数内部做了异常处理，可以在字符之间或者数字之间进行比较
7 Methods——可变类型（Mutable type），可以被排序 —— 使用 sort() Method（字符串常量和 range() 都是不可变的（Immutable））
	list.sort(reverse=True) #从大到小排序；reverse 参数，默认是 False，从小到大排序；同一种数据类型元素构成的列表可以使用。
	a.append() # 在末尾追加一个元素
	a.clear() # 清空序列，列表为空
	a.copy() # 对一个拷贝操作，不会更改 “原件”；与赋值 = 的不同，会同时更改 “原件”
	a.extend(t) # 在末尾追加一个列表，相当于 a_list += c_list
	a.insert(i，x) # 在某索引位置i插入一个元素x
	a.reverse() # reverse() 只对当前序列操作，并不返回一个逆序列表；返回值是 None
	删除单个元素
		一个命令：
		del a.[i] #对可变序列中元素下边进行检索删除，不返回删除值
		两个 Methods：
		a.pop([i]) # 去除索引为i的元素，且返回元素的值
		a.remove(x) # 去除元素x，如果有多个只删除第一个, 返回值是 None


# Part.1.E.6.containers
