s="""Simple is better than complex.
Complex is better than complicated."""
#str.startswith(prefix[, start[, end]])
print("s.lower().startswitch('S'):",\
      s.lower().startswith('S'))
print("s.lower().startswitch('s'):",\
      s.lower().startswith('s'))
print("s.lower().startswitch('b',10):",\
      s.lower().startswith('b',10))
print("s.lower().startswitch('e',11,20):",\
      s.lower().startswith('e',11,20))

#str.endswith(suffix[, start[, end]])
print("s.lower().endswith('.'):",\
      s.lower().endswith('.'))
print("s.lower().endswith('.',10):",\
      s.lower().endswith('.',10))
print("s.lower().endswith('.',10,20):",\
      s.lower().endswith('.',10,20))

#找sub/prefix/suffix前确认子字符串是否在需要找的字符串中，可以使用in操作符
print('mpl' in s)
print('mple is' in s)
print('mple iso' in s)