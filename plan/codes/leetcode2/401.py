# coding: utf-8
"""
二进制手表
"""

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # 枚举小时h和分钟m，然后判断二进制1的个数是否等于num
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h)+bin(m)).count('1') == num:
                    ans.append('%d:%02d' % (h,m))
        return ans
