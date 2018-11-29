 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: climStairs.py
 # author by: Lexi
 
 class Solution:
     def climStairs(self, n):
         """
         :type n: int
         :rtype: int
         """
         a, b = 1, 2
         result = []
         if n == 1:
             return 1
         i = 0
         while i < n:
             result.append(b)
             a, b = b, a+b
             i += 1
         return result[n-2]
 
 s = Solution()
 res = s.climStairs(6)
 print(res)
