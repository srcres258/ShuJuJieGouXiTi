/*
【题目】
设计一个算法，通过一趟遍历确定长度为n的单链表中值最大的结点。
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

// 获取链表中值最大的结点。
Node *findMax(Node *head) {
    if (!head) {
        return nullptr;
    }
    Node *max = head;
    Node *p = head->next;
    while (p) {
        if (p->value > max->value) {
            max = p;
        }
        p = p->next;
    }
    return max;
}

int main() {
    std::cout << "接下来输入链表" << std::endl;
    Node *list = inputList();

    Node *max = findMax(list);

    std::cout << "链表中值最大的结点：" << max->value << std::endl;

    return 0;
}