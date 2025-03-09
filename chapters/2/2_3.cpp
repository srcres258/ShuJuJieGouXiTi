/*
【题目】
已知两个链表A和B分别表示两个集合，其元素递增排列。请设计一个算法，用于求出A与B的交集，并将结果存放在A链表中。
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

// 求交集的算法。
Node *findIntersection(Node *a, Node *b) {
    Node *pA = a;
    Node *pB = b;
    Node *intersection = nullptr; // 存放交集的链表。
    Node *pI = nullptr;
    while (pA && pB) {
        if (pA->value == pB->value) { // 找到交集元素
            if (!intersection) {
                intersection = new Node(pA->value);
                pI = intersection;
            } else {
                pI->next = new Node(pA->value);
                pI = pI->next;
            }
            pA = pA->next;
            pB = pB->next;
        } else if (pA->value < pB->value) { // A链表当前结点的值小于B链表当前结点的值
            pA = pA->next;
        } else { // A链表当前结点的值大于B链表当前结点的值
            pB = pB->next;
        }
    }
    return intersection;
}

int main() {
    std::cout << "接下来输入第一个链表（递增顺序）" << std::endl;
    Node *la = inputList();

    std::cout << "接下来输入第二个链表（递增顺序）" << std::endl;
    Node *lb = inputList();

    Node *intersection = findIntersection(la, lb);

    std::cout << "交集：";
    Node *p = intersection;
    while (p) {
        std::cout << p->value << " ";
        p = p->next;
    }
    std::cout << std::endl;

    return 0;
}