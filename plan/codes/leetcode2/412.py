# coding: utf-8
"""
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
"""

class Solution:
    def fizzBuzz(self, n: int):
        s = []
        for i in range(1, n+1):
            print(i)
            if i % 3 == 0 and i % 5 ==0:
                s.append('FizzBuzz')
            elif i % 3 == 0:
                s.append('Fizz')
            elif i % 5 == 0:
                s.append('Buzz')
            else:
                s.append(str(i))
        return s
s = Solution()
res = s.fizzBuzz(15)
print(res)