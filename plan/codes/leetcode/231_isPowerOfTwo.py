# coding = utf-8
class Solution:
    def isPowerOfTwo(self, n):
        """
        :param n: int
        :return: bool
        """
        # 2的幂次 x 表示成二进制一定是一个1后面若干个0
        return n > 0 and bin(n).count('1') == 1

        # 2的幂次 x 表示成二进制一定是一个1后面若干个0，
        # 那么 x-1 一定是一个0后面若干个1，所以 x & (x-1) = 0 ，非2的幂无法得到0。
        return n > 0 and not (n & n-1)
