/* 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2 */


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
    int longestUnivaluePath(TreeNode* root) {
        int res=0;
        dfs(root,res);
        return res;
    }
    
    int dfs(TreeNode*root,int & res)
    {
        if(!root)
            return 0;
        int left=dfs(root->left,res);
        int right=dfs(root->right,res);
        left=(root->left && root->left->val == root->val) ? left+1:0;   // 此种形式 简介明了
        right=(root->right && root->right->val==root->val) ? right+1:0;
        res=max(left+right,res);
        return max(left,right);  // 返回值的性式 让人意想不到。
//而调用当前节点值的函数只能返回left和right中的较大值，因为如果还要跟父节点组path，就只能在左右子节点中选一条path，当然选值大的那个了
    }
};