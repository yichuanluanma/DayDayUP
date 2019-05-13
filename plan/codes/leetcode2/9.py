# coding=utf-8
"""
回文数
描述：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""

class Solution:
    def isPalindrome(self, x):
        """
        if x < 0:
            return False
        else:
            if x == int(str(x)[::-1]):
                return True
            else:
                return False

        # 优化后
        y = str(x)
        return y == y[::-1]
        """
    # 不将整数转为字符串
        if x < 0: return False
        temp = 0
        y = x
        while y > 0:
            temp = temp * 10 + y % 10
            y //= 10
        return x == temp
s = Solution()
result = s.isPalindrome(12321)
print(result)
