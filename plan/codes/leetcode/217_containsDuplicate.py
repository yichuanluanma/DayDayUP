# coding=utf-8
class Solution:
    def containsDuplicate(self, nums):
        """
        :param nums: List[int]
        :return:  bool
        """

        #利用Python的set，将数组转换成集合，若长度与原来相等则说明没有重复。
        return len(nums) != len(set(nums))

s = Solution()
res = s.containsDuplicate([1,3,5,2])
print(res)