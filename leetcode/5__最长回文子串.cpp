/* 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb" */

//暴力法实现  ==>最基础的实现方法。  实现方法的形式和想法值得记住。

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty())
            return "";
        int len=s.size();
        if(len==1)
            return s;
        int start=0;
        int length=0;
        for(int i=0;i<len;i++)
        {
            for(int j=i+1;j<len;j++)
            {
                int index1=i,index2=j;
                while(index1<index2)
                {
                    if(s[index1]==s[index2])
                    {
                        index1++;
                        index2--;
                    }
                    else
                    {
                        break;
                    }
                }
                if(index1>=index2 && j-i+1>length)
                {
                    start=i;
                    length=j-i+1;
                }
            
            }
        }
        cout<<length<<endl;
        if(length>0)
            return s.substr(start,length);
        else
            return s.substr(start,1);
    }
};