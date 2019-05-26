# coding = utf-8
"""

"""


class Solution:
    def reverseWords(self, s):
        new = s.split(' ')
        for i in range(len(new)):
            new[i] = new[i][::-1]
        return "".join(new)

s = Solution()
res = s.reverseWords("Let`s go")
print(res)
