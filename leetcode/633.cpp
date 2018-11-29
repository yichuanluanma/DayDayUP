/* 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
 

示例2:

输入: 3
输出: False */

class Solution {
public:
    bool judgeSquareSum(int c) {
        if( c < 0) return false;
        
        int r = sqrt(c);
        
        int l = sqrt(c - r*r);
        
        while( l <= r)
        {
            int sum = l*l + r*r;
            if( sum > c)
            {
                r--;
            }else if( sum < c){
                l++;
            }else{
                return true;
            }
        }
        
        return false;
    }
};