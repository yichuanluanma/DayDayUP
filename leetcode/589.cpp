/* 给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

       1
    /  |  \
   3   2    5
  / \
 5   6

返回其前序遍历: [1,3,5,6,2,4]。

 

说明: 递归法很简单，你可以使用迭代法完成此题吗? */
//递归
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> res;
        preorder(root,res);
        return res;
    }
    void preorder(Node*root ,vector<int> & v)
    {
        if(!root)
            return;
        v.push_back(root->val);
        for(auto it :root->children)
        {
            preorder(it,v);
        }
    }
};
//迭代
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> answer;
        if(root==nullptr)
            return answer;
        stack<Node*> mystack;
        mystack.push(root);
        while(!mystack.empty()){
            root=mystack.top();
            mystack.pop();
            answer.push_back(root->val);
            if(!(root->children).empty())
                for(int i=(root->children).size()-1;i>=0;--i)
                    mystack.push((root->children)[i]);
        }
        return answer;
    }
};



//以下为层次遍历，审错题意
class Solution {
public:
    vector<int> preorder(Node* root) {
        queue<Node*> dq;
        vector<int> res;
        dq.push(root);
        while(!dq.empty())
        {
            int len=dq.size();
            for(int i=0;i<len;i++)
            {
                for(int j=0;j<dq.front()->children.size();j++)
                {
                    dq.push(dq.front()->children[j]);
                }
                res.push_back(dq.front()->val);
                dq.pop();
            }
          
        }
        return res;
    }
};

/*
  stack的成员函数示例

函数名	　　功能	　　 		复杂度
size()	返回栈的元素数			O(1)
top()	返回栈顶的元素			O(1)
pop()	从栈中取出并删除元素	O(1)
push(x)	向栈中添加元素x			O(1)
empty()	在栈为空时返回true		O(1)


*/
