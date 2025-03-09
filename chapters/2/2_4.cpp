/*
【题目】
已知两个链表A和B分别表示两个集合，其元素递增排列。请设计算法求出两个集合A和B的差集（仅由在A中出现而不在B中出现的元素所构成的集合），
并将结果以同样的形式存储，同时返回该集合的元素个数。
*/

#include <iostream>
#include <utility>

struct Node {
    int value = 0;
    Node *next = nullptr;

    Node() = default;
    Node(int v) : value(v) {}

    // 返回链表的长度
    int getLength() const {
        int length = 0;
        Node const *p = this;
        while (p) {
            length++;
            p = p->next;
        }
        return length;
    }
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

// 求差集 A - B。
std::pair<Node *, int> getDifferenceSet(Node *headA, Node *headB) {
    // 初始化结果链表和指针
    Node *resultList = new Node;
    Node *pointer = resultList;
    // 比较链表A和链表B的元素
    while (headA && headB) {
        if (headA->value < headB->value) {
            pointer->next = new Node(headA->value);
            headA = headA->next;
            pointer = pointer->next;
        } else if (headA->value > headB->value) {
            headB = headB->next;
        } else {
            headA = headA->next;
            headB = headB->next;
        }
    }
    // 处理剩余的链表A或链表B元素
    while (headA) {
        pointer->next = new Node(headA->value);
        headA = headA->next;
        pointer = pointer->next;
    }
    while (headB) {
        headB = headB->next;
    }
    return std::make_pair(resultList->next, resultList->next->getLength());
}

int main() {
    std::cout << "接下来输入第一个链表（递增顺序）" << std::endl;
    Node *la = inputList();

    std::cout << "接下来输入第二个链表（递增顺序）" << std::endl;
    Node *lb = inputList();

    auto result = getDifferenceSet(la, lb);

    std::cout << "差集：";
    Node *p = result.first;
    while (p) {
        std::cout << p->value << " ";
        p = p->next;
    }
    std::cout << std::endl;

    std::cout << "个数：" << result.second << std::endl;

    return 0;
}