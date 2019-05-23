# coding: utf-8
"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
说明：不要使用任何内置的库函数，如  sqrt。
示例 1：
输入：16
输出：True
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 牛顿迭代公式
        if num == 1: return True
        r = num
        while r * r > num:
            r = (r + (num/r)) // 2
        if r*r == num:
            return True
        else:
            return False