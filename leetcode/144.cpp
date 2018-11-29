/* 给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3] */

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
		vector<int> pre;
		stack<TreeNode*> s;
		s.push(root);
		TreeNode* ptr = NULL;
		while(!s.empty()){
			ptr = s.top();
			s.pop();
			if(ptr){
				s.push(ptr->right);
				s.push(ptr->left);
				pre.push_back(ptr->val);
			}
			ptr = NULL;
		}
		return pre;
    }
};
// my code according to in order
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode*> s;
        vector<int> v;
        while(root || !s.empty())
        {
            while(root)
            {
                s.push(root);
                v.push_back(root->val); 
                root=root->left;
                
            }
            
            if(!s.empty())
            {
                root=s.top()->right;
                s.pop();
            }
        }
        return v;
    }
};