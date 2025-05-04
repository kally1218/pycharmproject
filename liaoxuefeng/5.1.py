print(1.23e9) #1.23*109
print('I\'m \"OK\"!')
print('I\'m learning\nPython.') #换行转义字符\n
print('\\\n\\')  # 其他: \t表示制表符,\t 会被解释为一个 Tab 宽度的空格，字符\本身也要转义，所以\\表示的字符就是\

print('\\\t\\')
print(r'\\\t\\') #为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('''line1
line2
line3''') #写成代码没有在交互窗口的line2ling3前方三个点

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Bob!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)