 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: singleNumber.py
 # author by: Lexi
 from functools import reduce
 
 class Solution:
     def singleNumber(self,nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         #if not nums:
         #    return 0
         #new_nums = 0
         #for i in nums:
         #    new_nums ^= i
         #return new_nums
 
         '''
         lambda 表达式是一行函数
         reduce()  函数会对参数序列中元素进行累积
         '''
         #return reduce(lambda x,y:x^y, nums)
         #return reduce(operator.xor, nums)
 
         return sum(set(nums)) * 2 - sum(nums)
 s = Solution()
 res = s.singleNumber([1,2,3,1,2])
 print(res)
