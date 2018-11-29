 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: lengthOfLastWord.py
 # author by: Lexi
 
 class Solution:
     def lengthOfLastWord(self, s):
         """
         :type s: str
         :rtype: int
         """
         #if not s:
         #    return 0
         #j = 0
         #k = 0
         #s = s[::-1]
         #for i in range(len(s)):
         #    if s[i].isalpha():
         #        k +=1
         #    if s[i].isspace() and k !=0:
         #        return k
         #return k
 
         #split()
         ns = s.rstrip(" ")
         lns = ns.split(" ")
         return len(lns[-1])
 
 s = Solution()
 res = s.lengthOfLastWord("a    ")
 print(res)