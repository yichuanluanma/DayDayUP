/* 给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]
 

示例 1：

输出："IDID"
输出：[0,4,1,3,2]
示例 2：

输出："III"
输出：[0,1,2,3]
示例 3：

输出："DDI"
输出：[3,2,0,1] */

class Solution {
public:
    vector<int> diStringMatch(string S) {
        int nSmall = 0;
        int nBig = S.length();
        vector<int>vecAns;
        for(int i = 0; i < S.length(); ++i)
        {
            if(S[i] == 'I')
                vecAns.push_back(nSmall++);
            else 
                vecAns.push_back(nBig--);
        }
        vecAns.push_back(nSmall);
        return vecAns;
    }
};