 #!/usr/local/bin/python3
 # -*- coding:UTF-8 -*-
 
 # Filename: is_number.py
 # author by : Lexi

 # 通过创建自定义函数 is_number() 方法来判断字符串是否为数字

 def is_number(s):
     try:
         float(s)
         return True
     except ValueError:
         pass
 
     try:
         import unicodedata
         unicodedata.numeric(s)
         return True
     except (TypeError, ValueError):
         pass
     return False
 
 #测试字符串和数字
 print(is_number('foo')) # False
 print(is_number('1'))   #True
 print(is_number('1.3')) #True
 
 # ®字符
 print(is_number('®'))
 # 泰语 2
 print(is_number('๒'))
 
 #Python isdigit() 方法检测字符串是否只由数字组成。
 #Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
