# coding=utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
        return nums
if __name__ == '__main__':
    s = Solution()
    res = s.rotate([1,2,3,4,5], 2)
    print(res)