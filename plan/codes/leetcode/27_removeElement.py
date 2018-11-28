 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: removeElement.py
 # author by: Lexi
 
 class Solution:
     def removeElement(self, nums, val):
         """
         :type nums: List[int]
         :type val: int
         :rtype: int
         """
         #根据python的语言特性
         #while val in nums:
         #    nums.pop(nums.index(val))
 
         #return len(nums)
 
         j = 0
         for i in range(len(nums)):
             if nums[i] != val:
                 # 赋值，暂时不理解
                 nums[j] = nums[i]
                 j += 1
         return j
 
 if __name__ == '__main__':
     s = Solution()
     a = s.removeElement([0, 4, 4, 0, 4, 4, 4, 0, 2, 1], 4)
     print(a)
