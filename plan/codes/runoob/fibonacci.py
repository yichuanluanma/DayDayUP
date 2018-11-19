 #!/usr/local/bin/python3
 #coding=utf-8

 # Fibonacci series: 斐波那契数列
 # 两个元素的总和确定了下一个数
 # def fib(n):     # 定义到 n 的斐波那契数列
 #     a, b = 0, 1
 #     while b < n:
 #         print(b, end=' ')
 #         a, b = b, a+b
 #     print()
 
 # def fib2(n):    # 返回到 n 的斐波那契数列
 #     result = []
 #     a, b = 0, 1
 #     while b < n:
 #         result.append(b)
 #         a, b = b, a+b
 #     return result


 # 斐波那契数列实现
 
 # 获取用户输入数据
 nterms = int(input("你需要几项？"))
 
 # 第一和第二项
 n1 = 0
 n2 = 1
 count = 2
 
 # 判断输入的值是否合法
 if nterms <= 0:
     print("请输入一个正整数：")
 elif nterms == 1:
     print("斐波那契数列：")
     print(n1)
 else:
     print("斐波那契数列：")
     print(n1,",",n2,end=" , ")
     while count < nterms:
         nth = n1 + n2
         print(nth,end=" , ")
         # 更新值
         n1 = n2
         n2 = nth
         count += 1

