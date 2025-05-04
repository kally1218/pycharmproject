#字符串和编码
#UTF-8的编码,让英文字母用1个字节也就是8个bit(8位01组成的东西)
#函数ord()可以获取字符的整数表示
#chr()函数把编码转换为对应的字符
print(ord('G'))
print(chr(68))
#如果要网络传输or保存到本地硬盘,要把str变为以字节为单位的bytes
x = b'ABD' #对bytes类型用b'' or b"", bytes的每个字符只占用1个字节
print(x)

#计算str有多少字符(bytes),用len()
print(len('ABC'))
print(len('中文'))

#如果要计算bytes,len()则会计算字节数
print(len(b'ABC'))
print(len('中文'.encode('utf-8'))) #中文字符要用utf-8转换,ascii码的数字不够用的

#SO!!!!为了避免乱码, 要坚持使用UTF-8对str和bytes进行转换
##所以!!!py文件开头要经常加上以下两行
#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#第一行是告诉Linux和OS X系统, 也就是mac系统才需要第一句话,但是win会自动忽略
#第二句话就是告诉解释器,要按照utf-8编码读取源代码
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)  #.1f表示浮点数

#练习
s1 = 72
s2 =

