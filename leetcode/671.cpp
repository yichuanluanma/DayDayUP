/* 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

示例 1:

输入: 
    2
   / \
  2   5
     / \
    5   7

输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
示例 2:

输入: 
    2
   / \
  2   2

输出: -1
说明: 最小的值是 2, 但是不存在第二小的值。 */

class Solution {
public:
    int findSecondMinimumValue(TreeNode* root) {
        //首先根节点的值是最小的
        //递归左右子树，找到最小的大于root.val 的值，否则，查找所有的子树后，返回-1，如果找到，立刻返回。
  

        queue<TreeNode* > q;
        int ret=INT_MAX;
        q.push(root);
        while(!q.empty())
        {
            int len=q.size();
            
            for(int i=0;i<len;i++)
            {
                if(q.front()->val>root->val)
                {
                    
                    ret=min(ret,q.front()->val);   

                }
                if(q.front()->left) 
                    q.push(q.front()->left);
                if(q.front()->right) 
                    q.push(q.front()->right);
                q.pop();
            }
        }
        if(ret==INT_MAX)
            ret=-1;
        return ret;
    }

	
};

class Solution {
public:
    int findSecondMinimumValue(TreeNode* root) {
        vector<int> ans;
        queue<TreeNode*> que;
        que.push(root);        
        while(!que.empty())
        {
            TreeNode* temp=que.front();
            ans.push_back(temp->val);
            que.pop();
            if(temp->left)
                que.push(temp->left);
            if(temp->right)
                que.push(temp->right);
        }
        if(ans.size()<=1)
            return -1;
        sort(ans.begin(), ans.end());        
        int cur=1,flag=0,past=ans[0];
        while(cur<ans.size())
        {
            if(ans[cur]!=past)
                return ans[cur];
            else
            {
                past=ans[cur];
                cur++;
            }            
        }
        if(!flag)
            return -1;
    }
};