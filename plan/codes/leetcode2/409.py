# coding: utf-8
"""
最长回文串
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        letters = {}
        for i in s:
            letters[i] = letters[i]+1 if i in letters else 1
        res = 0
        for i in letters:
            res += letters[i] - (letters[i] % 2)
        return res + 1 if res < len(s) else res

s = Solution()
res = s.longestPalindrome('qazqdEqR')
print(res)