 #!/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: reverseInteget.py
 # author by: Lexi
 
 class Solution(object):
     def reverse(self, x):
         x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
         return x if x < 2147483648 and x >= -2147483648 else 0
 
 if __name__ == '__main__':
     s = Solution()
     reverse_int = s.reverse(-120)
     print(reverse_int)
