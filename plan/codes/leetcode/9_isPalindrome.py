#!/usr/local/bin/python3
 
 # Filename: isPalindrome.py
 # author by: Lexi
 class Solution(object):
     def isPalindrome(self, x):
         if x < 0:
             return False
         else:
             return True if x == int(str(x)[::-1]) else False
 
 if __name__ == '__main__':
     s = Solution()
     result = s.isPalindrome(123)
     print(result)
