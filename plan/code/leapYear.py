#!/usr/local/bin/python3
 # -*- conding: UTF-8 -*-
 
 # Filename : leapYear.py
 # author by : Lexi
 
 # 判断闰年
 #year = int(input("输入一个年份："))
 #if (year % 4) == 0:
 #    if (year % 100) == 0:
 #        if (year % 400) == 0:
 #            print("{0}是闰年".format(year))   #整百年能被400整除的是闰年
 #        else:
 #            print("{0}不是闰年".format(year))
 #    else:
 #        print("{0}是闰年".format(year))        #非整百年能够被4整除的为闰年
 #else:
 #    print("{0}不是闰年".format(year))
 
 #优化
 #while True:
 #    try:
 #        year = int(input("请输入一个年份："))
 #    except ValueError:  #不是纯数字需要重新输入
 #        print("输入的不是整数！")
 #        continue
 #    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
 #        print("{0}是闰年".format(year))
 #    else:
 #        print("{0}不是闰年".format(year))
 #    break

 # 使用calendar 库中已经封装好了一个方法 isleap() 来实现这个判断是否为闰年
 import calendar
 
 while True:
     try:
         year = int(input("请输入年份："))
     except ValueError:
         print("输入的不是整数！")
         continue
     check_year = calendar.isleap(year)
     if check_year == True:
         print("闰年")
     else:
         print("平年")
     break
