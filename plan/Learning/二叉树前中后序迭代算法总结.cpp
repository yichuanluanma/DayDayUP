二叉树遍历的迭代算法，网上有很多。这里记录几种特别的遍历方法。

前序遍历：

前序遍历的普通算法，思路比较简单，很多书里面迭代方法的基本都采用这种方法，用堆栈来模拟递归的思路。

 

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode*> stackTree;
        if(root == NULL)
            return ret;
        TreeNode* curr = root;
        while(1){
            while(curr){
                stackTree.push(curr);
                ret.push_back(curr->val);
                curr = curr->left;
            }
            if(stackTree.empty())
                return ret;
            curr = stackTree.top();
            stackTree.pop();
            curr = curr->right;
        }
        
    }
};
 

后来发现一种算法，解题的算法实现非常的简单。

先看另一种算法的代码：

 

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        if(root == NULL)
            return ret;
        stack<TreeNode*> stackTree;
        stackTree.push(root);
        TreeNode* cur = NULL;
        while(!stackTree.empty()){
            cur = stackTree.top();
            stackTree.pop();
            ret.push_back(cur->val);
            if(cur->right !=NULL)
                stackTree.push(cur->right);
            if(cur->left != NULL)
                stackTree.push(cur->left);
        }
        return ret;
    }
};
 

要理解这个算法，首先要理解下面的这句语句：

stackTree.push(cur->right);

这句语句，不能把它简单想成是把右节点入栈了，而是要想象成，整个右子树入栈了，这样对于理解整个算法可能会有一定的帮助。

整个算法的思想就是，先把整棵树(根节点)入栈，然后进行循环。在循环里面，用curr这个变量来表示子树的根节点。所以按照前序的思想，首先输出根节点，然后再在栈里面存入右子树，然后是左子树。然后下一次迭代的时候，出栈的就是左子树的根节点，左子树继续循环，再栈里面存入它的右子树和左子树，然后继续，直到左子树全部输出了，然后右子树的根节点出栈，在输出右子树……直到把整棵树输出。

算法具体操作就是先输出根节点，然后输出左子树，遍历完左子树，然后再输出右子树，遍历右子树。输出子树的过程采用迭代的方法完成。

这种算法有别于上面的算法，这种算法，感觉是使用迭代的方法，实现了递归的思想。而且实现起来特别的简单。就是先载入根节点，然后载入右子树的根节点，在载入左子树的根节点。然后进行迭代。

如果不是很明白，自己随便找个例子来看看，可能会清楚一点的。


中序遍历：

中序遍历，采用的方法就是和上面的前序遍历的第一种方法，只是把输出的位置换一下，这个好像暂时没有什么特别的方法。

代码：

 

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> stackNode;
        vector<int> inOrder;
        while(1)
        {
            while(root)
            {
                stackNode.push(root);
                root = root->left;
            }
            
            if(stackNode.empty())
                return inOrder;
            root = stackNode.top();
            stackNode.pop();
            inOrder.push_back(root->val);
            root = root->right;
        }
        
    }
};
 

 

后序遍历：

后序遍历是三种遍历里面最麻烦的，因为普通的方法，要记录节点是否是第二次访问，这种方法，这里不多说。下面有两种特别的方法，可以不用对节点做记录。

方法一：

第一种方法，是采用后序遍历和前序遍历的逆序关系。

前序遍历，遍历的顺序是中左右，而后续遍历，遍历的顺序是左右中，那把后续遍历翻一下序，就是中右左，和前序遍历基本是一样的，只是先访问右子树，再访问左子树。所以实现后序遍历的一种方法就是，先实现中右左的遍历，然后把遍历的结果反序。得到的就是后序遍历了。

代码如下：

 

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        if(root == NULL)
            return ret;
        stack<TreeNode*> stackTree;
        stackTree.push(root);
        TreeNode* cur = NULL;
        while(!stackTree.empty()){
            cur = stackTree.top();
            stackTree.pop();
            ret.push_back(cur->val);
            if(cur->left !=NULL)
                stackTree.push(cur->left);
            if(cur->right != NULL)
                stackTree.push(cur->right);
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
观察一下，就可以发现，这个代码基本和上面的前序遍历是一模一样的，只是把子树入栈的顺序换了一下。由原来的先入右子树，再入左子树换成了先入左子树，再入右子树，实现中右左的遍历，然后对遍历的结果进行翻转就可以了。

 


方法二：

上面的代码有点取巧，遍历的过程并不是真正意义上的后序遍历，只是遍历的输出结果和后序遍历一样的罢了。

第二种方法，是实现正真的后序遍历。

先给出代码实现：

 

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> stackTree;
        vector<int> ret;
        if(root == NULL)
            return ret;
        TreeNode* pre = root;
        TreeNode* curr;
        stackTree.push(root);
        while(!stackTree.empty()){
            curr = stackTree.top();
            if(curr->left && pre != curr->left && pre != curr->right)
                stackTree.push(curr->left);
            else if(curr->right && pre != curr->right)
                stackTree.push(curr->right);
            else{
                ret.push_back(curr->val);
                pre =curr;
                stackTree.pop();
            }
            
        }
        return ret;
    }
    
};
在这个方法里面，采用一个新的数据pre，来记录给出结果的上一个遍历输出的节点。是输出的节点，中间过程节点，没有输出的不会被赋予pre。而数据curr则是表示现在指向的节点。

 

首先，给pre赋值root。考虑中间过程，pre和curr的关系有一下几种：

1.pre既不是curr的左节点，又不是curr的右节点，此时就表示，中间节点还没有遍历左右节点，所以要把左节点入栈。

2.pre不是curr的右节点，当情况1不成立的时候，情况2代表pre为中间节点的左节点或者左节点为空，接下来需要遍历中间节点的右节点，所以把右节点入栈。

3.pre是curr的右节点，此时代表，中间节点的左右节点都已经遍历过了，可以输出中间节点了。


这里有一个关键的地方就是，每次迭代开始给curr赋值的时候，只能取出栈顶元素，但是不能删除栈顶元素，因为这只是栈顶元素的第一次访问，还要进行第二次访问，才能删除栈顶元素。所以栈顶元素的删除是要在情况3下，中间元素输出后，才能删除栈顶元素的。

这个方法，要注意2个地方：

1.pre的初值不能使null，对于这个方法来说，最好的办法就是给他赋值为root。因为如果给pre赋值null的话，那如果输入是[1,2].那右子树就是空的，算法会误以为pre所指向的地址是右子树，所以会直接输出root。理论上来说，pre代表的是上一个遍历输出的节点。所以，pre的初值要满足一个条件，即pre刚开始的时候，不能和树里面的节点相同，即对树里面的所有节点，一定要满足下面的条件：

pre != curr->left && pre != curr->right， curr表示树的所有节点。

所以pre可以使root，root明显满足上面的条件。

2.            else if(curr->right && pre != curr->right)可不可以用else if(curr->right && pre == curr->left)来代替？

这句代码对表示上面三种情况的情况2,：在情况1不成立的条件下，pre不是curr的右节点。

情况2和pre是curr的左节点是不等价的。因为curr的左节点可能是空的，此时，也是满足情况2的，但是不满足pre是curr的左节点，所以上面两句话是不等价的。

那 else if(curr->right && pre != curr->right) 可不可以用   else if(curr->right && (pre == curr->left || curr->left == NULL))来代替？

同样不行，后面虽然把left是否是空考虑进去了，但是还是不能。因为，当左子树是空时，右子树不为空，这个条件始终成立，整个迭代就会在这里形成一个死循环。所以，情况二只能用源代码中的语句来表示，这是这个算法中特别要注意的地方。


总结：

对于后序遍历，第一种方法，实现起来比较简单，但确定就是他遍历的过程不是真正的后序遍历，只是给出了后序遍历的结果。

第二种方法过程采用了后序遍历，但是代码的书写中，要注意的点比较多，特别是第二点，针对第二种情况，要载入右节点的情况，这个地方特别容易出错，乍看有很多不同的写法，但是实际上，应该只有这一种写法，其他很多写法都是错误的，至少罗列的两种都是错的。