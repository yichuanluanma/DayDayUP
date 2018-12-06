 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 # Filename: twoSum.py
 # author by: Lexi
 
 class Solution:
     def twoSum(self, numbers, target):
         """
         :type numbers: List[int]
         :type target: int
         :rtype: List[int]
         """
         dict = {}
         for i, num in enumerate(numbers):
             if (target - num) in dict:
                 return [dict[target - num], i+1]
             dict[num] = i + 1
 
 s = Solution()
 res = s.twoSum([1,2,3,5,2], 8)
 print(res)
