/*
【题目】
将两个非递减的有序链表合并为一个非递增的有序链表。要求结果链表仍使用原两个链表的存储空间，不另外占用其他的存储空间。表中允许有重复的数据。

【解题思路】
1. 合并为一个非递减链表
    - 使用两个指针，分别指向两个链表的头部。
    - 比较两个指针所指元素的值，并将小的元素链接到结果链表。
    - 移动选中的指针到下一个结点。
    - 重复上述过程，直到一个链表为空。
    - 如果还有一个链表没有遍历完，将其生育部分全部链接到结果链表。

2. 反转合并后的链表
    - 初始化三个指针：`prev`、`curr`和`next`。开始时，`prev`为空，`curr`为链表的头结点。
    - 遍历链表，对于每一个结点，首先保存`curr->next`到`next`，然后更新`curr->next`指向`prev`，最后移动`prev`和`curr`指针到下一个位置。
    - 当`curr`到达链表末尾，`prev`将是新链表的头。
*/

#include <iostream>

struct Node {
    int value = 0;
    Node *next = nullptr;

    Node() = default;
    Node(int v) : value(v) {}
};

// 从控制台读取一行链表输入。
Node *inputList() {
    std::cout << "请输入链表长度：";
    int len;
    std::cin >> len;

    std::cout << "请依次输入链表中的元素：";
    Node *prev = nullptr, *head = nullptr;
    for (int i = 0; i < len; i++) {
        Node *p = new Node;
        std::cin >> p->value; 
        if (prev) {
            prev->next = p;
        } else {
            head = p;
        }
        prev = p;
    }

    return head;
}

// 合并两个链表，同时翻转链表的顺序（由非递减变为非递增）。
Node *mergeAndReverse(Node *list1, Node *list2) {
    Node *dummy = new Node;
    Node *tail = dummy;
    while (list1 && list2) {
        if (list1->value <= list2->value) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }
    if (list1) {
        tail->next = list1;
    } else {
        tail->next = list2;
    }
    Node *mergedList = dummy->next;
    // 反转链表
    Node *prev = nullptr;
    Node *curr = mergedList;
    while (curr) {
        Node *nextTemp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextTemp;
    }
    delete dummy;
    return prev;
}

int main() {
    std::cout << "接下来输入第一个链表（非递减顺序）" << std::endl;
    Node *la = inputList();

    std::cout << "接下来输入第二个链表（非递减顺序）" << std::endl;
    Node *lb = inputList();

    Node *merged = mergeAndReverse(la, lb);

    std::cout << "合并后的链表（非递增顺序）：" << std::endl;
    Node *p = merged;
    while (p) {
        std::cout << p->value << " ";
        p = p->next;
    }
    std::cout << std::endl;

    return 0;
}