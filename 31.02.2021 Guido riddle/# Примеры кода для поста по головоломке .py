# Примеры кода для поста по головоломке от Гвидо  ван Россума
# https://zen.yandex.ru/media/id/5b7ae22633ef9b00a8cc79f3/python-golovolomka-6014e303d3c91450c6c0fd33

# Загадка

x = 0
y = 0

def f():
    x = 1
    y = 1
    class C:
        print(x, y)
        x = 2

f()

# Пример с функцией

x = 0
y = 0

def f():
    x = 1
    y = 1
    def f2():
        print(x, y)
        x = 2
    f2()

f()

# дизассемблирование сниппета с функцией

import dis
dis.dis("""
x = 0
y = 0
def f():
    x = 1
    y = 1
    def f2():
        print(x, y)
        x = 2
    f2()
f()
""")

# дизассемблирование сниппета с классом

import dis 
dis.dis(""" 
x = 0 
y = 0
def f():
     x = 1
     y = 1
     class C:
         print(x, y)
         x = 2
f()
""")
