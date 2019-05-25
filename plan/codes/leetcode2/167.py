# coding: utf-8
# python3

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        newList = {}
        for i, item in enumerate(numbers):
            if target - item in newList:
                return [newList[target - item] + 1, i + 1]
            newList[item] = i
        return None
