# coding=utf-8
class Solution(object):
    def titleToNumber(self, s):
        """
        :param s: str
        :return: int
        """
        sum = 0
        for c in s:
            print(int(c, 36))
            # sum = sum * 26 + ord(c) - 64
            sum = sum * 26 + int(c, 36) - 9
            print(sum)
        return sum


s = Solution()
res = s.titleToNumber('A')
print(res)


