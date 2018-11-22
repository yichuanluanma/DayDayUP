//给定一个 N 叉树，返回其节点值的后序遍历。

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> answer;
        if(root==nullptr)
            return answer;
        stack<Node*> mystack;
        unordered_set<Node*> visited;
        mystack.push(root);
        while(!mystack.empty()){
            root=mystack.top();
            if((root->children).empty()||visited.count(root)){
                answer.push_back(root->val);
                mystack.pop();
            }
            else{
                for(int i=(root->children).size()-1;i>=0;--i)
                    mystack.push((root->children[i]));
                visited.insert(root);
            }
        }
        return answer;
    }
};

//递归的方法很简单