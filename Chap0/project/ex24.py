# coding:utf-8
# py2转py3的练习 打印 转义序列 格式化字符 函数定义和调用 除法运算

# 这个练习在py2中运行完全没有问题，但是在py3里运行，会有提醒：classic int division 
# 这个是对除法运算的提醒。在py3中整数形的除法用的是//，而不是/（这个是用于浮点数类型计算的）
# 可以知道在编程中对于数据类型的定义和运算还是非常严苛的，不能马虎
# 数据类型在python中一个非常重要的知识点

print ("Let's practice everything.")
print ('You\'d need to know the \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an exlplanation
\n\twhere there is none.
"""

print "-------------"
print (poem)
print "-------------"

five = 10 - 2 + 3 - 6
print  ("This should be five: {0}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans // 1000
    crates = jars // 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
print ("with a starting point of: {0}".format(start_point))
print ("we'd have {0} beans, {1} jars, {2} crates.".format(beans, jars, crates))

start_point = start_point // 10
print ("we'd have {0} beans, {1} jars, {2} crates".format(beans, jars, crates))