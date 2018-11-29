 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: addBinary.py
 # author by: Lexi
 
 class Solution:
     def addBinary(self, a, b):
         """
         :type a: str
         :type b: str
         :rtype: str
         """
         num = int(a,2) + int(b,2)
         n = bin(num)
         return n[2:]
 
         #return bin(int(a,2) + int(b,2))[2:]
 
     """
     类型转换
     dec = int(input("输入数字："))
     print("十进制数为：",dec)
     print("转换为二进制为：", bin(dec))
     print("转换为八进制为：", oct(dec))
     print("转换为十六进制为：", hex(dec))
     """
 
 s = Solution()
 res = s.addBinary('11', '10')
 print(res)
