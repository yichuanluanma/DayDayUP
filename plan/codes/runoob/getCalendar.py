 #!/usr/local/bin/python3
 # -*- Filename: calendar.py
 
 # Filename: test.py
 # author by: Lexi
 
 # 生成日历
 # 引入日历模块
 import calendar
 
 # 输入指定年月
 yy = int(input("输入年份："))
 mm = int(input("输入月份："))
 
 # 显示日历
 print(calendar.month(yy, mm))
 
 # 计算每个月天数
 monthRange = calendar.monthrange(yy, mm)
 
 print(monthRange)
 print("{0}年{1}的第一天是星期{2},当月总天数是{3}".format(yy,mm,monthRange[0]+1,monthRange[1]))
