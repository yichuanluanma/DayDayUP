# coding: utf-8
"""
找不同
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {}
        for c in s:
            letters[c] = letters[c] + 1 if c in letters else 1
        for c in t:
            if c not in letters:
                return c
            letters[c] -= 1
            if letters[c] < 0:
                return c
