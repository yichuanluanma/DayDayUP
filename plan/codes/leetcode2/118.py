# coding=utf-8
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

"""
分析：
帕斯卡三角形的规律： 
它是一个三角形矩阵，其顶端第0行是 1；
第1行两个1，这两个1是由他们上头左右两数之和 (不在三角形内的数视为0)。
依此类推产生第2行：0+1=1；1+1=2；1+0=1。第3行：0+1=1；1+2=3；2+1=3；1+0=1。循此产生后面的行。
"""
class Solution:
    def generate(self, numsRows):
        res = []
        for i in range(0, numsRows):
            res.append([1]*(i+1))
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
