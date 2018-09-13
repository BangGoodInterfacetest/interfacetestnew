# Python解释器、变量、对象
# 1、Python解释器（Cpython）:
# 1.1 python是一种动态解释性语言
# 解释性语言执行过程：1、文本形式的源代码解析并编译成字节码（不同于目标机器代码）；2、解释器运行第一步产生的字节码，运行程序是边解释边执行，甚至可在执行过程中修改代码，产生新结果
# 其他解释性语言
# 编译性语言执行过程：1、先编译成机器能识别的机器指令码，2、执行已经编译好的目标机器指令码；机器指令码执行效率快（c c++等）
#
# java是特殊的编译行语言，不是编译成目标机器码，而是字节码，java虚拟机执行字节码
# python是解释下语言，但是与java类似，用python虚拟机执行字节码（import .pyc 重用）
#
# 1.2 解释逻辑

# 2、变量、对象、引用
# 2.1 简单理解，Python 没有赋值，只有引用
# 2.2 “=”等号实际是创建对象 和引用
# 2.3、可变对象和不可变对象：这里说的不可变指的是值的不可变。对于不可变类型的变量，如果要更改变量，则会创建一个新值，把变量绑定到新值上，而旧值如果没有被引用就等待垃圾回收
#      可变类型数据对对象操作的时候，不需要再在其他地方申请内存，只需要在此对象后面连续申请(+/-)即可，也就是它的内存地址会保持不变，但区域会变长或者变短
# 怎么理解：x=1？
# import sys
# x1=1
# x2=1
# print(id(x1),id(x2),id(1))
# x1=2
# print(id(x1))

# 怎么理解x=x+y 和 x+=y
# x=0
# y=1
# print(id(x),id(y))
# # x=x+y
# # print(id(x),id(y))
# x+=y
# print(id(x),id(y))

# list1=[1]
# print(id(list1))
# lsit2=[2]
# list1.append(lsit2[0])
# print(list1,id(list1))
# list1=list1+lsit2
# print(list1,id(list1))
# 38488344
# 505911008
# 505911024
# 38488344
[[...], 2]


# list1=[1,2]
# print(id(list1))
# print(id(list1[0]))
# print(id(list1[1]))
# list1[0]=list1
# print(id(list1[0]))
# print(list1)



#
#
#
import copy
lista=[1]
sourcelist=[lista,2]
q_copylist=copy.copy(sourcelist)
s_copylist=copy.deepcopy(sourcelist)
print("sourcelist:",sourcelist,"l-id=",id(sourcelist),'\n',"q_copylist:",q_copylist,"q-id=",id(q_copylist),'\n',"s_copylist:",s_copylist,"s-id=",id(s_copylist),'\n',"==========================")

sourcelist[0]=3
print("sourcelist:",sourcelist,"l-id=",id(sourcelist),'\n',"q_copylist:",q_copylist,"q-id=",id(q_copylist),'\n',"s_copylist:",s_copylist,"s-id=",id(s_copylist),'\n',"==========================")

lista[0]=4
print("sourcelist:",sourcelist,"l-id=",id(sourcelist),'\n',"q_copylist:",q_copylist,"q-id=",id(q_copylist),'\n',"s_copylist:",s_copylist,"s-id=",id(s_copylist),'\n',"==========================")

# str0=1
# str1=str0+1
# str2=copy.copy(str1)
# str3=copy.deepcopy(str1)
# print("str1:",str1,"l-id=",id(str1),'\n',"str2:",str2,"q-id=",id(str2),'\n',"str3:",str3,"s-id=",id(str3),'\n',"==========================")

#
#
# sys.getrefcount(a)