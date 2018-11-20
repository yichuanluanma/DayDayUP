 # -*- coding: UTF-8 -*-
 
 # Filename: sumTwo.py
 # author by: Lexi
 
 # 求两数之和
 
 class Solution:
     def twoSum(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: List[int]
         """
         # 方法一
         # 暴力破解法
         #for i in range(len(nums)):
         #    for j in range(len(nums)):
         #        if nums[i] + nums[j] == target:
         #            return (i,j)
 
 
         dict = {}
         for i in range(len(nums)):
             x = nums[i]
             if target-x in dict:
                 return (dict[target-nums[i]], i)
 
             dict[x] = i
 
 if __name__ == '__main__':
     s=Solution()
     result = s.twoSum([1,5,2,7],9)
     print(result)

