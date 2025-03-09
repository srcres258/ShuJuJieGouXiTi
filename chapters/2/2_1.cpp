/*
【题目】
将两个递增的有序链表合并为一个递增的有序链表。要求结果链表仍使用原来的两个链表的存储空间，不另外占用其他的存储空间。表中不允许有重复的数据。

【解题思路】
可通过一个双指针逐步比较两个有序链表的节点，将较小的节点添加到结果链表中，最终将两个链表合并为一个递增排序的链表，
并利用原有的存储空间完成操作。具体步骤如下：

1. **输入处理**：从控制台读取两个链表的数据。
2. **双指针初始化**：分别以两个链表的下一个节点开始遍历。
3. **逐个比较并连接**：根据当前节点的值比较大小，将较小的节点添加到结果中，移动相应的指针。
4. **处理剩余节点**：当其中一个链表遍历完毕后，将剩下的部分连接到结果链表末尾。
5. **释放内存**：删除第二个链表以避免额外占用空间。

该方法确保合并后的链表满足题目要求，不使用额外的内存资源，并且正确地处理了所有节点，包括两条链表中的最后一个节点。
*/

#include <iostream>

// 链表结点。这个链表有头结点。
struct ListNode {
    bool head = false; // 是否是头节点。
    int val = 0; // 该结点所存数据。
    ListNode *next = nullptr; // 指向下一个结点。
};

// 从控制台读取一行链表输入。
ListNode *inputList() {
    ListNode *head = new ListNode;
    head->head = true;
    
    std::cout << "请输入链表长度：";
    int len;
    std::cin >> len;

    std::cout << "请依次输入链表中的元素：";
    ListNode *prev = head;
    for (int i = 0; i < len; i++) {
        ListNode *p = new ListNode;
        std::cin >> p->val; 
        prev->next = p;
        prev = p;
    }

    return head;
}

// 合并两个递增顺序的有序链表，结果保存在la中。
// 合并后的lb链表将失效（内存将从堆中释放）！
void mergeLists(ListNode *la, ListNode *lb) {
    ListNode *pa = la->next, *pb = lb->next;
    ListNode *lc, *pc;
    lc = pc = la;
    while (pa && pb) {
        if (pa->val < pb->val) {
            pc->next = pa;
            pc = pa;
            pa = pa->next;
        } else if (pa->val > pb->val) {
            pc->next = pb;
            pc = pb;
            pb = pb->next;
        } else {
            pc->next = pa;
            pc = pa;
            pa = pa->next;
            ListNode *q = pb->next;
            delete pb;
            pb = q;
        }
    }
    pc->next = pa ? pa : pb;
    delete lb;
}

int main() {
    std::cout << "接下来输入第一个链表（递增顺序）" << std::endl;
    ListNode *la = inputList();

    std::cout << "接下来输入第二个链表（递增顺序）" << std::endl;
    ListNode *lb = inputList();

    mergeLists(la, lb);

    std::cout << "合并后的链表（递增顺序）：" << std::endl;
    ListNode *p = la->next;
    while (p) {
        std::cout << p->val << " ";
        p = p->next;
    }
    std::cout << std::endl;

    return 0;
}