 # -*- coding: UTF-8 -*-
 
 # Filename: countAndSay.py
 # author by: Lexi
 
 class Solution:
     def countAndSay(self, n):
         """
         :type n: int
         :rtype: str
         """
         if n < 1 or n > 30:
             return False
 
         res = '1'
         for i in range(n-1):
             new_res, pre, count = '', res[0], 0
             for j in range(len(res)):
                 if res[j] == pre:
                     count += 1
                 else:
                     new_res += str(count) + pre
                     count = 1
                     pre = res[j]
             res = new_res + str(count) + pre
         return res
 
 
 if __name__ == '__main__':
     s = Solution()
     res = s.countAndSay(3)
     print(res)
