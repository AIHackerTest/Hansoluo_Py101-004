# -*- coding: utf-8 -*-

# 功能描述
# 程序随机生成一个20以内的数字，用户有10次机会猜测
# 程序根据用户输入，给予一定提示（大了，小了，正确）
# 猜对或用完10次机会，游戏结束

import random

# random.randint(a, b)：Return a random integer N such that a <= N <= b
a = random.randint(1,20)
 
for i in range(1,11):
    b = int(input("请猜测20以内的数字："))
    if a > b:
        print("小了")
    elif a < b:
        print("大了")
    else:
        print("正确")
        break
    
    print("你还有 {0} 次机会".format(10-i))
    i += 1

print ('游戏结束')

    

