 #!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: getYestoday.py
 # arthor: Lexi
 
 # 获取昨天的日期
 import datetime
 
 def getYestoday():
     today=datetime.date.today()
     oneday=datetime.timedelta(days=1)
     yestoday=today-oneday
     return yestoday
 # 输出
 print(getYestoday())
