#!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: decimal.py
 # author by : Lexi
 
 # 十进制转二进制、八进制、十六进制
 
 # 获取用户输入的十进制数
 
 dec = int(input("输入数字："))
 
 print("十进制数为：", dec)
 print("转换为二进制为：", bin(dec))
 print("转换为八进制为：", oct(dec))
 print("转换为十六进制为：", hex(dec))

 # 用户输入字符
 c = input("请输入一个字符：")
 
 # 用户输入ASCII码，并将输入的数字转为整型
 a = int(input("请输入一个ASCII码："))
 
 print( c + "的ASCII码为", ord(c))
 print( a, "对应的字符为", chr(a))
 
