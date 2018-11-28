 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: searchInsertPosition.py
 # author by: Lexi
 
 class Solution:
     def searchInsertPosition(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         j = 0
         for i in range(len(nums)):
             if nums[i] < target:
                 j += 1
             elif nums[i] == target:
                 return j
             else:
                 nums.insert(j, target)
                 print(nums)
                 return j
         nums.insert(j, target)
         return j
 
 if __name__ == '__main__':
     s = Solution()
     a = s.searchInsertPosition([1,3,5,6], 7)
     print(a)
