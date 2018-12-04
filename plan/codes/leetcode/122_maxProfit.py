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
         profit = 0
         for i in range(1,len(prices)):
             if prices[i] > prices[i-1]:
                 profit += prices[i] - prices[i-1]
 
         return profit
 
 s = Solution()
 res = s.maxProfit([2,1,4,5,3,6,1])
 print(res)
