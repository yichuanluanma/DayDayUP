/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 // 先添加一个首节点，然后定义两个指针，分别指向第一和第N个，同时遍历，直到第二个指针指向结尾，第一个指针即为目标
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        
        ListNode *cur = dummyHead;
        ListNode *pre = dummyHead;
        int i =0; 
        for(;i<n+1; i++){
            cur = cur->next;
            // if(!cur)
            //     return head;
        }
        while(cur){
            cur = cur->next;
            pre = pre->next;
        }
        
        ListNode *delNode = pre->next;
        pre->next = delNode->next;
        delete delNode;
        
        ListNode* retNode = dummyHead->next;
        delete dummyHead;
        
        return retNode;
    }
};
