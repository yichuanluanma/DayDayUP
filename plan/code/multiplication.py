#!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: multiplication.py
 # author by: Lexi
 
 # 九九乘法表
 for i in range(1, 10):
     for j in range(1, i+1):
         print('{}x{}={}\t'.format(j, i, i*j), end='')
 
     print()
