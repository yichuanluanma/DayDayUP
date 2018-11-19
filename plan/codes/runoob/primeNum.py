 #!/usr/local/bin/python3
 # -*- conding: UTF-8 -*-
 
 # Filename:primeNum.py
 # author by : Lexi
 
 # 质数判断
 # 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5,                                  7等），换句话说就是该数除了1和它本身以外不再有其他的因数。
 
 while True:
     try:
         num = int(input('输入一个整数：'))
     except ValueError:
         print("输入的不是整数！")
         continue
     # 质数大于1
     if num > 1:
         #查看因子
         for i in range(2,num):
             if (num % i) == 0:
                 print(num,"不是质数")
                 print(i,"乘以",num//i,"是",num)
                 break
         else:
             print(num,"是质数")
         # 如果输入的数字小于或等于1,不是质数
     else:
         print(num,"不是质数")
     break
