/* 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。

示例 :

输入:

   1
    \
     3
    /
   2

输出:
1

解释:
最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> v;
        inorder(root,v);
        int ret=INT_MAX;
        for(int i=0;i<v.size()-1;i++)
        {
            cout<<v[i]<<" ";
            ret=min(ret,v[i+1]-v[i]);
        }
        return ret;
    }
    
    void inorder(TreeNode* root, vector<int> & v)
    {
        if(root == NULL)
            return;
        
        inorder(root->left,v);
        v.push_back(root->val);
        inorder(root->right,v);
    }
};

class Solution {
public:
    int res = INT_MAX, last = -1;
    
    int getMinimumDifference(TreeNode* root) {
        dfs(root);
        return res;
    }

    void dfs(TreeNode *root) {
        if (!root || !res) return;
        dfs(root->left);
        
        if (last >= 0)
            res = min(abs(root->val - last), res);
        last = root->val;

        dfs(root->right);
        return;
    }
};
class Solution {
public:
	int pre = -1, res = INT_MAX;
	int getMinimumDifference(TreeNode* root) {
		if (!root)
			return res;
		getMinimumDifference(root->left);
		if (pre != -1) {
			res = min(res, abs(root->val - pre));
		}
		pre = root->val;
		getMinimumDifference(root->right);
		return res;
	}
};