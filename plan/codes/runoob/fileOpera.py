 #!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filebame: fileOpera.py
 # author by: Lexi
 
 # 文件IO
 # 写文件
 with open("./file/test.txt", "wt") as out_file:
     out_file.write("该文本会写入到文件中\n看到我了吧！")
 
 # Read a file
 with open("./file/test.txt", "rt") as in_file:
     text = in_file.read()
 
 print(text)
