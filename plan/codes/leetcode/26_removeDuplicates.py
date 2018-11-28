 #!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: removeDuplicates.py
 # author by: Lexi
 
 class Solution:
     def removeDuplicates(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         #for i in range(len(nums)-1):
         #    for j in nums[i+1:]:
         #        if i == j:
         #            nums.remove(nums[i])
         #        else:
         #            break
         #print(nums)
 
         #i = 0
         #while i < len(nums)-1:
         #    if nums[i] == nums[i+1]:
         #        nums.remove(nums[i])
         #    else:
         #        i=i+1
         #return len(nums)
 
         if not nums:
             return 0
         j = 0
         for i in range(1,len(nums)):
             if nums[j] != nums[i]:
                 j += 1
                 nums[j] = nums[i]
         return j+1

 
 if __name__ == '__main__':
     s = Solution()
     res = s.removeDuplicates([0,1,1,2,2,3,3,4,5,5,5,5])
     print(res)