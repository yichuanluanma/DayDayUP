 #!/usr/local/bin/python3
 
 # Filename: longestCommonPrefix.py
 # author by: Lexi
 
class Solution(object):
     def longestCommonPrefix(self, strs):
         #方法一 运用zip()函数
         #res = ""
         #if len(strs) == 0:
         #    return ""
         #zip()函数用于将可迭代对象作为参数，\
         #将对象中对应的元素打包成一个个元组，\
         #然后返回由这些元组组成的列表
         #for each in zip(*strs):
             #利用集合创建一个无序不重复元素集
         #    if len(set(each)) == 1:
         #        res += each[0]
         #    else:
         #        return res
         #return res
 
         #方法二
         if not strs: return ""
 
         #查找最长公共前缀，只需对比最长的字符串和最短的字符串
         s1 = min(strs)
         s2 = max(strs)
         for i, c in enumerate(s1):
             if c != s2[i]:
                 return s1[:i]
         return s1
         
 s = Solution()
 res = s. longestCommonPrefix(["flower","flow","flight"])
 print(res)
