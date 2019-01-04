# coding=utf-8
class Solution:
    def isHappy(self, n):
        """
        :param n: int
        :return: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

s = Solution()
res = s.isHappy(18)
print(res)