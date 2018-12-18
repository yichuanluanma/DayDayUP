class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int result = 0;
        int left, mid, right;

        result = nums[0] + nums[1] + nums[2];
        sort(nums.begin(), nums.end());
        for(left = 0; left < nums.size() - 2; left ++)
        {
            mid = left + 1;
            right = nums.size() - 1;
            while(right > mid)
            {
                int sum = nums[left] + nums[mid] + nums[right];
                if(sum == target) return target;
                if(abs(sum - target) < abs(result - target))
                {
                    result = sum;
                }
                if(sum > target)
                {
                    right --;
                }
                else
                {
                    mid ++;
                }
            }
        }
        return result;
    }
};