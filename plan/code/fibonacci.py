 #!/usr/local/bin/python3
 #coding=utf-8

 # Fibonacci series: 斐波那契数列
 # 两个元素的总和确定了下一个数
 def fib(n):     # 定义到 n 的斐波那契数列
     a, b = 0, 1
     while b < n:
         print(b, end=' ')
         a, b = b, a+b
     print()
 
 def fib2(n):    # 返回到 n 的斐波那契数列
     result = []
     a, b = 0, 1
     while b < n:
         result.append(b)
         a, b = b, a+b
     return result