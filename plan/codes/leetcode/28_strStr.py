 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: strStr.py
 # author by: Lexi
 
 class Solution:
     def strStr(self, haystack, needle):
         """
         :type haystack: str
         :type needle: str
         :rtype: int
         """
         #库函数string.find()
         return haystack.find(needle)
 
 
 if __name__ == '__main__':
     s = Solution()
     res = s.strStr('hello', 'll')
     print(res)
