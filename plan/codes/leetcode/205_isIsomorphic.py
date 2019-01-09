# -*- coding: utf-8 -*-
class Solution:
    def isIsomorphic(self, s, t):
        """
        :param s: str
        :param t: str
        :return: bool
        """

        """
        s有多少种不同的字符，t也有多少种不同的字符。如果我们将映射写成字符对的形式，
        比如 (‘a’,’c’) 表示s中字符’a’映射到t中’c’，那么映射的个数与s中字符的种类数相同。
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

s = Solution()
res = s.isIsomorphic('floor', 'good')
print(res)