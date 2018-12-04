 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 #Filename: isPalindrome.py
 # author by: Lexi
 class Solution:
     def isPalindrome(self, s):
         """
         :type s: str
         :rtype: bool
         """
         new_str = "".join([i for i in s if i.isalnum() or i.isalpha()]).lower()
         return new_str[::-1] == new_str[:]
 s = Solution()
 res = s.isPalindrome("a man a plan a canal Panama")
 print(res)
