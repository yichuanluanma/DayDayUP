 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: maxSubArray.py
 # author by: Lexi
 
 class Solution:
     def maxSubArray(self, nums):
         """
         :type nums:List[int]
         :rtype: int
         """
         for i in range(1, len(nums)):
             subMaxSum=max(nums[i]+nums[i-1],nums[i])
             nums[i]=subMaxSum
         return max(nums)
 
 
 if __name__ == '__main__':
     s = Solution()
     res = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
     print(res)
