# -*- coding: utf-8 -*-

#使用Python编程完成算式输入合法性检查，直接使用List实现
#Stack_example2.py

left = ['{', '[', '<', '(']     #left是所有左括号的列表
right = ['}', ']', '>', ')']    #right是所有右括号的列表
L = []  #保存扫描到的左括号，使用列表实现栈的LIFO操作

#输入
string = input("请输入待检测字符串：")