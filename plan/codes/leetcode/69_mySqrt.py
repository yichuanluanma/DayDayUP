 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: mySqrt.py
 # author by: Lexi
 import math
 
 class Solution:
     def mySqrt(self, x):
         """
         :type x: int
         :rtype: int
         """
         # return int(x**(0.5))
         if x <= 0:
             return 0
         return math.floor(math.sqrt(x))
 
 s = Solution()
 res = s.mySqrt(8)
 print(res)
