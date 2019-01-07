# coding=utf-8
class Solution:
    def countPrimers(self, n):
        """
        :param n: int
        :return: int
        """
        if n < 3:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, int(n ** 0.5) +1):
            if prime[i] == 1:
                prime[i*i:n:i] = [False]*len(prime[i*i:n:i])
        return sum(prime)

s = Solution()
res = s.countPrimers(10)
print(res)