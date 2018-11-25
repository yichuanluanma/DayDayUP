/* 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False */
// 
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
public:
	bool findTarget(TreeNode* root,int k)
	{
		if (!root)return false;
		inOrder(root);
		int left(0), right(int(nums.size()) - 1);
		while (left < right)
		{
			int sum = nums[left] + nums[right];
			if (sum == k)return true;
			else if (sum < k) left++;
			else right--;
		}
		return false;
	}
private:
	vector<int>nums;
	void inOrder(TreeNode* root)
	{
		if (!root)return;
		inOrder(root->left);
		nums.push_back(root->val);
		inOrder(root->right);
	}

};
//没有额外的保存空间，只用递归的方法，利用了二叉搜索树的查找效率 ，，优化到简洁，易理解的程度。
class Solution {
public:
    bool findTarget(TreeNode* root,int k) {
        bool ret;
        
        ret=dfs(root,root,k);
        return ret;
        
    }
    bool dfs(TreeNode*root,TreeNode* start,int k)
    {
        if(!root)
            return false;
        bool ret;
        ret=search(root,start,k-root->val) || dfs(root->left,start,k) || dfs(root->right,start,k);
        return ret;
    }
    
    bool search(TreeNode* cur,TreeNode *root,int t)
    {
        if(!cur)
            return false;
        while(root)
        {
            if(root->val == t && root!=cur)
                return true;
            else if(root->val<t)
                root=root->right;
            else
                root=root->left;
        }
        
        return false;
    }
    
    
};