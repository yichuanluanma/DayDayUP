 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: getRow.py
 # author by: Lexi
 
 class Solution:
     def getRow(self, rowIndex):
         """
         :type rowIndex: int
         :rtype: List[int]
         """
         #递归
         #if rowIndex == 0:
         #    return([1])
         #li = [1]*(rowIndex+1)
         #prev = self.getRow(rowIndex-1)
         #for i in range(1, rowIndex):
         #    li[i] = prev[i-1] + prev[i]
         #return(li)
 
         #迭代
         pre_row = [1]
         for i in range(rowIndex):
             new_row = [1]
             for j in range(1, len(pre_row)):
                 new_row.append(pre_row[j]+pre_row[j-1])
             new_row.append(1)
             pre_row = list(new_row)
         return pre_row

 s = Solution()
 res = s.getRow(5)
 print(res)
