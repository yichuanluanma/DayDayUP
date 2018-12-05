 #/usr/local/bin/python3
 # -*- coding: UTF-8 -*-
 
 # Filename: minStack.py
 # author by: Lexi
 
 class Solution:
     def __init__(self):
         """
         initialize your data structure here
         """
         self.stack = []
     def push(self, x):
         pre_min = 2147483647 if len(self.stack) == 0 else self.stack[-1][1]
         cur_min = min(x, pre_min)
         self.stack.append((x,cur_min))
         
     def pop(self):
         self.stack.pop()
         
     def top(self):
         return self.stack[-1][0]
     
     def getMin(self):
         return self.stack[-1][1]
