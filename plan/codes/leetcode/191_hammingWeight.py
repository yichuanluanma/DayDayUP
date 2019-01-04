# coding=utf-8
class Solution:
    def hammingWeight(self, n):
        """
        :param n: int
        :return: int
        """
        return bin(n).count('1')
s = Solution()
res = s.hammingWeight(3)
print(res)
