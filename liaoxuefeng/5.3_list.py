classmates = ['Michael', 'Bob', 'Tracy']
print (classmates)

print(len(classmates))

#把element插入指定位置
classmates.insert(1, 'Jack')
print(classmates)

#删除指定位置pop(i),i是index位置
classmates.pop(1)
print(classmates)

#tuple和list的区别是1:tuple是圆括号2.tuple一旦初始化就不能更改了
#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

print(L[0][0],L[1][1], L[2][2])