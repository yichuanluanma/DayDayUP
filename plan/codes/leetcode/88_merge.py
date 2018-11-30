 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: merge.py
 # author by: Lexi
 
 class Solution:
     def merge(self, nums1, m, nums2, n):
         """
         :type nums1: List[int]
         :type m: int
         :type nums2: List[int]
         :type n: int
         :rtype: rtype: void Do not return anything, modify nums1 in-place instead.
         """
         nums1[m:m+n] = nums2[:n]
         nums1.sort()
         return nums1
 
 s = Solution()
 res = s.merge([1,2,3,0,0], 3, [2,5,6], 3)
 print(res)
