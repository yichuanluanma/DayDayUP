/* 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。 */

//考虑到循环数组，，为了避免超出范围，利用取余的方法，遍历整个数组，除该元素之外。

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, -1);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < i + n; ++j) {
                if (nums[j % n] > nums[i]) {
                    res[i] = nums[j % n];
                    break;
                }
            }
        }
        return res;
    }
};

//利用栈来优化。


// another method
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> ret(nums.size());
        stack<int> stk;
        for (int i = 0; i < 2; ++i){
            for (int j = nums.size() - 1; j >= 0; --j){
                int n = nums[j];
                while (!stk.empty() && stk.top() <= n){
                    stk.pop();
                }
                ret[j] = stk.empty() ? -1 : stk.top();
                stk.push(n);
            }
        }
        return ret;
    }
};