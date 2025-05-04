#elif的用法

x = 20
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else :
    print('LARGE')
print('all done')

#try 代码 for finding if code has problem
astr = 'hello Bob'
try:
    istr = int(astr) #dangerous code 字符不能转成整数int
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)