 #!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename : facorial.py
 # author by : Lexi
 
 # 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
 # 通过用户输入数字计算阶乘
 
 # 获取用户输入的数字
 #num = int(input("请输入一个数字："))
 #factorial = 1
 
 # 查看数字是负数，0 或 正数
 #if num < 0:
 #    print("抱歉，负数没有阶乘")
 #elif num == 0:
 #    print("0 的阶乘为1")
 #else:
 #    for i in range(1, num + 1):
 #        factorial = factorial*i
 #    print("%d 的阶乘为 %d"%(num,factorial))
 
 # 使用递归斐波那契数列
 
 def recur_fibo(n):
     """递归函数
     输出斐波那契数列"""
     if n <= 1:
         return n
     else:
         return(recur_fibo(n-1) + recur_fibo(n-2))
 
 # 获取用户输入
 nterms = int(input("您要输入几项？ "))
 
 # 检查输入的数字是否正确
 if nterms <= 0:
     print("输入正数")
 else:
     print("斐波那契数列")
     for i in range(nterms):
         print(recur_fibo(i))

