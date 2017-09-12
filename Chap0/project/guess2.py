# -*- coding: utf-8 -*-

# 程序内部用0~9生成一个四位数，首位不为0，且各位上的数字不重复，如1942
# 用户输入4位数进行猜测，程序返回相应提示
# 用A表示数字和位置都正确，用B表示数字正确但位置错误
# 用户猜测后，程序返回A和B的数量
# 比如 2A1B表示用户猜测数字，有2个数字和位置都正确，有1个数字，数字正确但位置错误
# 猜对或用完10次机会，游戏结束

import random

a = random.randint(1000,10000)

# 将数字转化成列表类型
# def number_pos(n):
#     n1 = n // 1000 # 获取千位上的数字
#     n2 = (n % 1000) // 100 # 获取百位上的数字
#     n3 = (n % 100) // 10 # 获取十位上的数字
#     n4 = n % 10 # 获取个位上的数字
#     a_list = [n1, n2, n3, n4]
#
#     return a_list

# 有更简短的代码方式
def number_pos(n):
    n_list = []

    while n:
        n_list.append(n % 10)  # 将个位上的数字加到列表第一位
        n = n // 10 # 去掉最后一位

    n_list.reverse() # 逆序返回
    return n_list

# 保证四位数字不重复
while True:

    a_list = number_pos(a)
    if a_list[0] != a_list[1] and a_list[0] != a_list[2] and \
    a_list[0] != a_list[3] and a_list[1] != a_list[2] and \
    a_list[1] != a_list[3] and a_list[2] != a_list[3]:
        break
    else:
        a = random.randint(1000,10000)

 # 返回AB值的判断
def guess(x1, x2):
    x1_list = number_pos(x1)
    x2_list = number_pos(x2)

    count_a = 0
    count_b = 0

    for i, num in enumerate(x1_list):

        if num == x2_list[i]:
            count_a += 1
        elif num in x2_list:
            count_b += 1
        else:
            continue

    return count_a, count_b

# 开始猜测数字
for i in range(1,11):
    b = int(input("请猜测一个4位数："))

    count = guess(a, b)
    #print (type (count)) 测试类型为tuple
    #print ("{0}A{1}B".format(count)) 报错IndexError: tuple index out of range，按下面的是正确的
    print ("{0}A{1}B".format(count[0], count[1]))

    if a != b:
        print ("你还有 {0} 次机会".format(10-i))
        i += 1
    else:
        print ("正确")
        break

print ("游戏结束")
