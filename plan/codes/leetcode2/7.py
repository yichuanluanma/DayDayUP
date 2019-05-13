# -*- coding: utf-8 -*-
"""
整数反转
描述：
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
其数值范围为 [−2**31,  2**31 − 1]。
"""


class Solution:
    def reverse(self, x):
        x = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
        return x if -2**31 < x < 2**31 -1 else 0

if __name__ == '__main__':
    s = Solution()
    result = s.reverse(-12356)
    print(result)