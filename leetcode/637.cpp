/* 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11]. */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 // 递归以及迭代的方法
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            int len=q.size();
            double ans=0;
            for(int i=0;i<len;i++)
            {
                ans+=q.front()->val;
                if(q.front()->left)
                    q.push(q.front()->left);
                if(q.front()->right)
                    q.push(q.front()->right);
                q.pop();
            }
            res.push_back(ans/len);
        }
        return res;
    }
};
class Solution {
public:
    void levelOrder(vector<TreeNode*> &currLevel, vector<double> &avgs){
        if(currLevel.empty()) return; 
        vector<TreeNode*> nextLevel;
        int count = 0;
        double avg = 0.0;
        for(auto n : currLevel){
            avg += n->val;
            ++count;
            if(n->left) nextLevel.push_back(n->left);
            if(n->right) nextLevel.push_back(n->right);
        }
        avgs.push_back(avg/count);
        swap(nextLevel, currLevel);
        levelOrder(currLevel, avgs);
    }
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> avgs;
        vector<TreeNode*> currLevel;
        if(!root) return avgs;
        currLevel.push_back(root);
        levelOrder(currLevel, avgs);
        return avgs;
    }
};
