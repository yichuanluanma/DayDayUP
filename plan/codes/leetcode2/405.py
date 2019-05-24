# coding: utf-8
"""
数字转换为十六进制数
"""

class Solution:
    def toHex(self, num: int) -> str:
        """
        0xf 是16进制写法 ,等于十进制的15,等于二进制的1111
        digits & 0xf 的意思是.取digits这个变量的后4位
        大黄讲解：
        每次获取后四位，数字的表示形式，32位；四位，是一个十六进制；
        一个数 和 0xf 相与 ，获得最后四位的值，转换为相应的字母，向右平移四位，一直到num=0
        """
        if num == 0:
            return "0"
        hex = '0123456789abcdef'
        ans = ''
        while num and len(ans) < 8:
            ans = hex[num&0xf] + ans
            print(num&0xf)
            num >>= 4
        return ans
s = Solution()
res = s.toHex(26)
print(res)