# -*- coding: utf-8 -*-

#使用Python编程完成算式输入合法性检查，直接使用List实现
#Stack_example2.py
left = ['{', '[', '<', '(']     #left是所有左括号的列表
right = ['}', ']', '>', ')']    #right是所有右括号的列表
L = []  #保存扫描到的左括号，使用列表实现栈的LIFO操作
#输入
string = input("请输入待检测字符串：")
#处理
flag = 0    #flag为标志位，如果在遍历字符串过程中没有遇到左右括号不匹配的情况，则flag = 0，否则，flag = 1
for char in string:                 #对于string中每一个字符char
    if char in left:                #如果char在列表left内，则char为左括号，将其加入堆栈末尾
        L.append(char)
    elif char in right:             #如果char在列表right内，则char为右括号
        if len(L) == 0:         #如果此时stack为空，则将标志位flag置为1，并跳出循环
            flag = 1
            break
        elif left.index(L[len(L)-1]) == right.index(char):#如果此时char与堆栈的最后一个字符（栈顶）匹配，则将堆栈的最后一个字符删除（出栈）
            L.pop()
        else:                       #如果不匹配，则将标志位置为1，并跳出循环
            flag = 1
            break