#!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename : maxNum.py
 # author by: Lexi
 
 # 获取最大值函数
 
 # 最简单的
 print(max(1, 2))
 print(max('a', 'b'))
 
 # 对元组、列表的使用
 print(max([1,2]))
 print(max((1,2)))
 
 print("0, 100, -400最大值为：",max(0, 100, -400))
 
 # 对比任意多个数字的大小
 N = int(input("输入需要对比大小数字的个数：\n"))
 
 num = [ int(input("请输入第%d个对比数字 \n"%(i))) for i in range(1,N+1)]
 
 print("您输入的数字为：",list(num))
 print("最大值为：",max(num))
