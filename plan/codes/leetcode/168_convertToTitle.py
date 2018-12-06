 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 # Filename: convertToTitle.py
 # author by: Lexi
 
 class Solution:
     def convertToTitle(self, n):
         """
         :type n: int
         :rtype: str
         """
         res = ''
         while n:
             res = chr((n-1)%26 + 65) + res
             n = (n-1) / 26
         return res
