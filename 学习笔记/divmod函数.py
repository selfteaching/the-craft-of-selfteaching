from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

divmod(11, 3)
a, b = divmod(11, 3)
print(a)
print(b)

divmod(3, 11)
a, b = divmod(3, 11)
print(a)
print(b)

#元组包典型赋值写法：divmod返回元组包括商和余数，通过a,b=divmod(3,11)赋值给a,b。