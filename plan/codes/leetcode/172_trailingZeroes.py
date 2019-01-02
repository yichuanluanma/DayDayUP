# coding=utf-8
import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :param n: int
        :return: int
        """
        res = 0
        while n > 0:
            n = math.floor(n / 5)
            res += n
        return res
s = Solution()
res = s.trailingZeroes(8)
print(res)
