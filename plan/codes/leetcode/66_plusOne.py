 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: plusOne.py
 # authhor by: Lexi
 
 class Solution:
     def plusOne(self, digits):
         """
         :type digits: List[int]
         :rtype: List[int]
         """
         if not digits:
             return 0
         new_digits = int(''.join(str(i) for i in digits))
         new_digits += 1
         return list(map(int, str(new_digits)))
 
 s = Solution()
 res = s.plusOne([1,2,3])
 print(res)
