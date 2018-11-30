#/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
# Filename: sortedArrayToBST.py
# author by: Lexi


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
#         if not nums:
#             return None
        
#         mid = len(nums)//2  #“//”表示整数除法；“/”浮点数除法；
#         root = TreeNode(nums[mid])
#         left = nums[:mid]
#         right = nums[mid+1:]
#         root.left = self.sortedArrayToBST(left)
#         root.right = self.sortedArrayToBST(right)
#         return root

        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root