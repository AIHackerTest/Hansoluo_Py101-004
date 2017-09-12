# coding:utf-8
# py2转py3的练习  ex32.py

# 定义列表数据类型的变量
the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# 使用for语句循环一个列表，要习惯这种循环语句 for XX in XX 
for number in the_count:
    print ("This is count {0}".format(number))

for fruit in fruits:
    print ("A fruit of type: {0}".format(fruit))

for i in change:
    print ("I got {0}".format(i))

# 定义一个空列表
elements = []

for i in range(0,6):
    print ("Adding {0} to the list.".format(i))
    elements.append(i)  # append()是一个列表类型的变量可调用的函数，它的功能是在列表的尾部追加元素

# 变量i无需事先定义且可重复，每次循环时都会被重新定义
for i in elements:
    print ("Elements was: {0}".format(i)) 