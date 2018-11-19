 #!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: str.py
 # author by: Lexi
 
 # 测试实例一
 print("测试实例一")
 str = "hello.com"
 
 print(str.isalnum()) # 判断所有字符都是数字或者字母
 print(str.isalpha()) # 判断所有字符都是字母
 print(str.isdigit()) # 判断所有字符都是数字
 print(str.islower()) # 判断所有字符都是小写
 print(str.isupper()) # 判断所有字符都是大写
 print(str.istitle()) # 判断所有单词都是首字母大写，像标题
 print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r
 
 print("-----------------------")
 
 # 测试实例二
 print("测试实例二")
 str = "hello"
 print(str.isalnum()) # 判断所有字符都是数字或者字母
 print(str.isalpha()) # 判断所有字符都是字母
 print(str.isdigit()) # 判断所有字符都是数字
 print(str.islower()) # 判断所有字符都是小写
 print(str.isupper()) # 判断所有字符都是大写
 print(str.istitle()) # 判断所有单词都是首字母大写，像标题
 print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

 print("-----------------------")
 
 # 测试实例三
 # 字符串大小写转换
 print("测试实例三")
 str = "github.com"
 print(str.upper())   # 把所有字符中的小写字母转换成大写字母
 print(str.lower())   # 把所有大写字母转换成小写字母
 print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
 print(str.title())   # 把每个单词的第一个字母转化为大写，其余小写
