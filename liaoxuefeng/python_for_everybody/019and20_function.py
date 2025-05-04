#def is to create and store code
def thing():
    print('Hello')
    print('Fun')
thing()

x=5
print('Hello')

def print_lycis():
    print("I'm a lumber, and I'm okay.")
    print('I sleep all night and I work all day.')

#定义一个语言的函数
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

print(greet('es'), "Glenn")

#加法器,用函数做
def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

#return语句, when a function does not return a value, call it void function
