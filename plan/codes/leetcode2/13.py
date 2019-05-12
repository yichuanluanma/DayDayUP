# coding=utf-8
"""
罗马数字转整数
"""

class Solution:
    def RomanToInt(self, s):
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = roman[s[-1]]
        print(res)
        print(len(s)-2)
        for i in range(len(s)-2, -1, -1): #!!!range的用法
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
s = Solution()
result = s.RomanToInt("MCMLXXX")
print(result)