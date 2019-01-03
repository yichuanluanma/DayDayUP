# coding=utf-8
class Solution:
    def reverseBits(self, n):
        """
        :param n: int
        :return: int
        """
        b = '{0:032b}'.format(n)
        print(b)
        b = b[::-1]
        return int(b, 2)
s = Solution()
res = s.reverseBits(11111111111111111111111111111101)
print(res)