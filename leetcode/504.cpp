//给定一个整数，将其转化为7进制，并以字符串形式输出

class Solution {
public:
    string convertToBase7(int num) {
        if(num == 0) return "0";
        string ans = "";
        if(num < 0) 
        {
           ans="-";
           num = -num;
        }
        while(num)
        {
            ans.push_back(num % 7 + '0');
            num /= 7;
        }
        if(ans[0] == '-') reverse(ans.begin() + 1, ans.end());
        else reverse(ans.begin(), ans.end());
        return ans;
    }
};