	vector<int> valSet;
	stack<TreeNode*> stack;
	while(root || !stack.empty()){  //迭代求得中序遍历
		while(root){
			stack.push(root);
			root=root->left;
		}
		if(!stack.empty()){
			valSet.push_back(stack.top()->val);
			root=stack.top()->right;
			stack.pop();
		}
	}
	// 以 root 为核心，栈是个辅助的类别

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> s;
        TreeNode* cur=root;
        while(!s.empty() ||cur){
            if(cur){
                s.push(cur);
                cur=cur->left;
            }
            else{
                cur=s.top();
                res.push_back(cur->val);
                s.pop();
                if(cur->right){
                    //s.push(cur);
                    cur=cur->right;
                }
                else cur=NULL;
            }
        }
        return res;
    }

