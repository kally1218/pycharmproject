names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print(l)

n = 1
while n <= 100:
    if n > 10:
        break #可以提前结束循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0 : #if n是偶数,则执行continue用于[跳过]这个循环, 并且后续的print()是不会执行的
        continue
    print(n)