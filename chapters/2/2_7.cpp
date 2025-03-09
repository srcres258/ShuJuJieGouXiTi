/*
【题目】
设计一个算法，将链表中所有结点的链接方向“原地”逆转，即要求仅利用原表的存储空间，换句话说，要求算法的空间复杂度为O(1)。
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
    Node *head = new Node; // 头结点
    Node *cur = head;
    for (int i = 0; i < len; i++) {
        Node *p = new Node;
        std::cin >> p->value; 
        cur->next = p;
        cur = p;
    }

    return head;
}

// 逆置带头结点的单链表。
void inverse(Node *head) {
    Node *p = head->next; // p指向首元结点
    head->next = nullptr; // 头结点的指针域置为空
    while (p) { // 遍历链表，如果下一个结点存在
        Node *q = p->next; // q指向p的后继
        p->next = head->next;
        head->next = p; // p插入在头结点之后
        p = q;
    }
}

int main() {
    std::cout << "接下来输入链表" << std::endl;
    Node *list = inputList();

    inverse(list); // 逆置链表

    std::cout << "逆置后的链表：";
    Node *p = list->next;
    while (p) {
        std::cout << p->value << " ";
        p = p->next;
    }
    std::cout << std::endl;

    return 0;
}