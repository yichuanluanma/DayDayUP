/* 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。

注意: next() 和hasNext() 操作的时间复杂度是O(1)，并使用 O(h) 内存，其中 h 是树的高度。 */

// 关键： 读懂题意。 对中序遍历的理解越来越深了。

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        while(root)
        {
            s.push(root);
            root=root->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode* top=s.top();
        int res=top->val;
        s.pop();
        if(top->right)
        {
            TreeNode* root=top->right;
            while(root)
            {
                s.push(root);
                root=root->left;
            }
        }
        return res;
    }
    stack<TreeNode*> s;
};