 #!/usr/local/bin/python3
 
 # Filename: longestCommonPrefix.py
 # author by: Lexi
 
 class Solution(object):
     def longestCommonPrefix(self, strs):
         res = ""
         if len(strs) == 0:
             return ""
         #zip()函数用于将可迭代对象作为参数，\
         #将对象中对应的元素打包成一个个元组，\
         #然后返回由这些元组组成的列表
         for each in zip(*strs):
             #利用集合创建一个无序不重复元素集
             if len(set(each)) == 1:
                 res += each[0]
             else:
                 return res
         return res
 
 s = Solution()
 res = s. longestCommonPrefix(["flower","flow","flight"])
 print(res)
