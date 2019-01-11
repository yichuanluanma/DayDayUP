# coding=utf-8
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: bool
        """
        d = {}
        for key, value in enumerate(nums):
            if value in d and key-d[value] <= k:
                return True
            d[value] = key
        return False

s = Solution()
res = s.containsNearbyDuplicate([1,2,3,4,1], 1)
print(res)