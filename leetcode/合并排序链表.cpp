//递归的合并链表   That's the biggest difference.
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *slow = head, *fast = head, *pre = head;
        while (fast && fast->next) {
            pre = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        pre->next = NULL;
        return merge(sortList(head), sortList(slow));
    }
    ListNode* merge(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        if (l1->val < l2->val) {
            l1->next = merge(l1->next, l2);
            return l1;
        } else {
            l2->next = merge(l1, l2->next);
            return l2;
        }
    }
        
    
};

// 合并链表使用了迭代的方法

class Solution {
public:
    ListNode* sortTwo(ListNode* left, ListNode* right){
        if (left == NULL)return right;
        if (right == NULL)return left;
        
        ListNode head(0);
        ListNode* tail = &head;
        
        while(left || right)
        {
            if (right == NULL || left !=NULL && left->val < right->val)
            {
                tail->next = left;
                tail = left;
                left = left->next;
            }
            else
            {
                tail->next = right;
                tail = right;
                right = right->next;
            }
        }
        
        return head.next;
    }
    
    int countList(ListNode* head){
        int res = 0;
        while (head)
        {
            head = head->next;
            res++;
        }
        return res;
    }
    
    ListNode* mergesortList(ListNode* head, int len) {
        //cout<<listNodeToString(head)<<len<<endl;
        if (len <= 1) return head;
        
        int half = len/2;
        ListNode* pre = head;
        ListNode* right = head->next;
        while(--half)
        {
            pre = right;
            right = right->next;
        }
        pre->next = NULL;
        
        ListNode* first = mergesortList(head, len/2);
        ListNode* second = mergesortList(right, len - len/2);
        
        //cout<<listNodeToString(first)<<listNodeToString(second)<<endl;
        ListNode*res = sortTwo(first, second);
        //cout<<listNodeToString(res)<<endl;
        return res;
        
    }
    
    ListNode* sortList(ListNode* head) {
        return mergesortList(head, countList(head));
    }
};