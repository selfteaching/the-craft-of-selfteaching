#replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
s="""Simple is better than complex.
Complex is better than complicated."""
print(s)
#str.replace(old, new[, count])
print("s.replace:",\
      s.lower().replace("is","IS"))
print("s.replace:",\
      s.lower().replace("is","IS",1))
#count=1,只替换一次
print("s.replace:",\
      s.lower().replace("is","[]",2))
#expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
#str.expandtabs(tabsize=8)
s1="Specail\tcases\tare\tsimple"
print(s1)
print("str.expandtabs:",\
      s1.expandtabs())
print(s1.expandtabs(2))