
/********************************************************************************************
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]


1/ 不用额外空间， hash 表不可取
2/ O(n) 时间复杂度，二叉搜索等不可取
3/ 数组特点  1 ≤ a[i] ≤ n 即，元素值和索引之间存在关联
********************************************************************************************/


class Solution{
	public:
		vector<int> findDulplicates(vector<int>& nums)
		{
			int n=nums.size();
			for(int i=0;i<n;)
			{
				// 确保 当前值 与 当前值的索引 有对应关系
				if(nums[nums[i]-1] !=nums[i])
				{
					swap(nums[i],nums[nums[i]-1]);
				}
				else
					i++;
			}
				 
			vector<int> res;
			
			for(int i=0;i<n;i++)
			{
				if(nums[i]!=i+1)
					res.push_back(nums[i]);
			}
			
	   
			return res;
		}
		/*
		line 27 to line 36 中，排序的时间复杂度不好估计。交换值不妥，不是最佳的方法。
		*/
		
		vector<int> findDuplicates(vector<int>& nums) {
			int n=nums.size();
			vector<int> res;
			for(int i=0;i<n;i++)
			{
				int index=abs(nums[i])-1;
				if(nums[index]<0)
				{
					res.push_back(index+1);
				}
				nums[index]=-nums[index];
				cout<<i<<" run is start:\n";
				for(int j=0;j<n;j++)
					cout<<nums[j]<<" ";
				cout<<i<<"\n";
			}
			return res;
		}
		/*
		这个方法牛逼。
		*/
};


