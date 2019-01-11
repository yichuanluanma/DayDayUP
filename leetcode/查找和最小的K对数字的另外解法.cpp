class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int len1 = nums1.size(), len2 = nums2.size(), cnt = min(k, len1*len2);
        vector<int> index(len1, 0);
        vector<pair<int, int>> ans;
        while(cnt-- > 0)
        {
            int temMin = INT_MAX, m = 0;
            for(int i =0; i < len1; i++)
                if(index[i] < len2 && nums1[i]+nums2[index[i]] < temMin) 
                    temMin= nums1[i]+nums2[index[i]], m = i;
            ans.push_back(make_pair(nums1[m], nums2[index[m]++]));
        }
        return ans;
    }
};