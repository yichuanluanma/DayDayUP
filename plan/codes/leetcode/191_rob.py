# coding=utf-8
class Solution:
    def rob(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        now = last = 0
        for i in nums:
            last, now = now, max((i+last), now)
        return now
s = Solution()
res = s.rob([2,7,4,6,9])
print(res)