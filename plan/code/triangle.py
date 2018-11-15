 # !/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename : triangle.py
 # author by : Lexi
 
 a = float(input('输入三角形第一条边：'))
 b = float(input('输入三角形第二条边：'))
 c = float(input('输入三角形第三条边：'))
 
 # 计算半周长
 s = (a + b + c) / 2
 
 # 计算面积
 area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
 print('三角形面积 %0.2f' %area)
 
