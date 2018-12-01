/* 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 

示例 1：

输入： "()"
输出： 1
示例 2：

输入： "(())"
输出： 2
示例 3：

输入： "()()"
输出： 2
示例 4：

输入： "(()(()))"
输出： 6
 

提示：

S 是平衡括号字符串，且只含有 ( 和 ) 。
2 <= S.length <= 50 */
// 很迷~~
class Solution {
public:
    int scoreOfParentheses(string S) {
        stack<string> s;
        
        for(auto i : S)
        {
            if(i== '(')
                s.push("(");
            else
            {
                if(!s.empty() && s.top()=="(")
                {
                    s.pop();
                    s.push("1");
                }
                else
                {
                    int sum=0;
                    while(!s.empty() && s.top()!="(")
                    {
                        sum+=stoi(s.top());
                        s.pop();
                    }
                    if(!s.empty())
                    {
                        s.pop();
                    }
                    s.push(to_string(sum*2));
                }
            }
        }
        
        int res=0;
        while(!s.empty())
        {
            res += stoi(s.top());
            cout<<stoi(s.top());
            s.pop();
        }
        return res;
    }
};