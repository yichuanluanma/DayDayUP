 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: majorityElement.py
 # author by: Lexi
 
 class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         #return sorted(nums)[len(nums)//2]
         nums.sort()
         return nums[len(nums)//2]
 
 s = Solution()
 res = s.majorityElement([2,2,1,1,1,2,2])
 print(res)
