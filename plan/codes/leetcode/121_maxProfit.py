 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: maxProfit.py
 # author by: Lexi
 
 class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         if not prices:
             return 0
         res = 0
         small = prices[0]
         for n in prices[1:]:
             small = min(n, small)
             if res < n - small:
                 res = n - small
         return res
 
 s = Solution()
 res = s.maxProfit([1,2,5,2,1])
 print(res)
