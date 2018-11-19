/* 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :

返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
 

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。 */

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res;
        if(root==NULL)
            return res;
        deque<Node*> d;
        deque<Node*> next;
        d.push_back(root);
        while(!d.empty())
        {
            vector<int> v;
            for(auto cur:d)
            {
                v.push_back(cur->val);
                for(auto i : cur->children)
                {
                    next.push_back(i);
                }
            }
            d.clear();
            swap(d,next);
            res.push_back(v);
        }
        return res;
    }

};