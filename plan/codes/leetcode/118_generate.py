 #/usr/local/bin/python3
 # -*-coding: UTF-8 -*-
 
 # Filename: generate.py
 # author by: Lexi
 
 class Solution:
     def generate(self, numRows):
         """
         :type numRows: int
         :rtype: List[List[int]]
         """
         if not numRows:
             return []
         if numRows == 1:
             return [[1]]
         rows = [[1]]
         i = 1
         while i < numRows:
             j = 0
             temp = 0
             line = []
             while j <= i:
                 if j == 0:
                     temp = rows[i-1][j]
                 elif j == i:
                     temp = rows[i-1][j-1]
                 else:
                     temp = rows[i-1][j] + rows[i-1][j-1]
                 line.append(temp)
                 j += 1
             rows.append(line)
             i += 1
         return rows
 
 s = Solution()
 res = s.generate(6)
 print(res)
