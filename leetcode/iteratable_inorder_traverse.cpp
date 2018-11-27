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

