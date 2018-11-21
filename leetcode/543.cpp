/* 
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。 */
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
    int depth(TreeNode* root,int& ans){
        if(root==NULL)return 0;
        int left=depth(root->left,ans);
        int right=depth(root->right,ans);
        ans=max(ans,left+right);
        return max(left+1,right+1);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int ans=0;
        depth(root,ans);
        return ans;
    }
};


class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if(!root)
            return 0;
        return max(max(deepSum(root),diameterOfBinaryTree(root->right)),diameterOfBinaryTree(root->left));
    }
    int deepSum(TreeNode*root)
    {
        if(!root)
            return 0;
        return deep(root->left)+deep(root->right);
    }
    
    int deep(TreeNode*root)
    {
       if(!root)
           return 0;
        return max(deep(root->left),deep(root->right))+1;
    }
};