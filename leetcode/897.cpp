/* 给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

 

示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
 

提示：

给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。 */

class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        if(root==nullptr)
        {
            return nullptr;
        }
        vector<TreeNode*> v;
        fun(root,v);
        TreeNode* ptr = v[0];
        root = v[0];
        for(int i=0;i<v.size()-1;i++)
        {
            ptr->left=nullptr;
            ptr->right = v[i+1];
            ptr = ptr->right;
        }
        ptr->left = nullptr;
        ptr->right = nullptr;
        return root;
    }
    void fun(TreeNode* root,vector<TreeNode*>& v)
    {
        if(root==nullptr)
        {
            return;
        }
        fun(root->left,v);
        v.push_back(root);
        fun(root->right,v);
        return;
    }
};