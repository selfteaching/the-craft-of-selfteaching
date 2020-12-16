# 需要了解的 Bash 基本命令
* 虽然 Git 也有图形化版本，但无论如何你都会接触到命令行工具。并且，谁都一样，早晚会遇到非使用命令行不可的情况。
* 以下是常用 Bash 命令的简要说明：命令	简要说明
cd	Change Directory 的缩写；转到指定目录
ls	List 的缩写；列出当前目录中的内容
mkdir	Make Directory 的缩写；在当前目录中创建一个新的目录
pwd	Present Working Directory 的缩写；显示当前工作目录
touch	创建一个指定名称的空新文件
rm	Remove 的缩写；删除指定文件
rmdir	Remove Directory 的缩写；删除指定目录
cp	Copy 的缩写；拷贝指定文件
mv	Move 的缩写；移动指定文件
cat	Concatenate 的缩写；在屏幕中显示文件内容
chmod	Change Mode 的缩写；改变文件的权限
man	Manual 的缩写；显示指定命令的使用说明
其中，chmod 最常用的 4 个权限分别是：

* 文件权限模式	简要说明
777	任何人都可以读、写、执行该文件
755	任何人都可以读、执行该文件，但只有所有者可以修改
700	只有所有者才能进行读、写、执行操作
+x	将文件设置为可执行
在使用 man 命令时，系统会使用 vim 文本编辑工具以只读模式打开帮助文件，常用键盘命令如下：

* 键盘命令	简要说明
f	向后翻屏
b	向前翻屏
d	向后翻半屏
u	向前翻半屏
j	向后翻一行
k	向前翻一行
h	查看 vim 帮助
q	退出

# 