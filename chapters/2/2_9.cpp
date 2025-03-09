/*
【题目】
已知p指向双向循环链表中的一个结点，其结点结构为data、prior、next这3个域，设计算法change(p)，交换p所指向的结点及其前驱结点的顺序。
*/

#include <iostream>

struct Node {
    int data;
    Node* prior;
    Node* next;

    Node(int data = 0, Node *prior = nullptr, Node *next = nullptr) : data(data), prior(prior), next(next) {}
};

void change(Node *p) {
    // p 是双向循环链表中的一个结点，本算法将 p 所指结点与其前驱结点交换
    Node *q = p->prior;

    // 将 p 的前驱的前驱的后继设置为 p
    q->prior->next = p;

    // p 的前驱指向其前驱的前驱
    p->prior = q->prior;

    // p 的前驱的后继设置为 p 的后继
    q->next = p->next;

    // p 的前驱指向 p
    q->prior = p;

    // p 的后继的前驱设置为 q
    p->next->prior = q;

    // p 的后继指向 q
    p->next = q;
}

int main() {
    // 创建一个双向循环链表 1 <-> 3 <-> 5 <-> 7 <-> 9 ，其中 1 和 9 首尾相连
    Node *head = new Node(1);
    Node *p1 = new Node(3, head);
    Node *p2 = new Node(5, p1);
    Node *p3 = new Node(7, p2);
    Node *p4 = new Node(9, p3);
    head->prior = p4;
    head->next = p1;
    p1->next = p2;
    p2->next = p3;
    p3->next = p4;
    p4->next = head;

    // 打印初始链表
    Node *q = head;
    do {
        std::cout << q->data << " ";
        q = q->next;
    } while (q != head);
    std::cout << std::endl;

    // 令p指向第三个结点作为例子
    Node *p = p2;

    // 交换 p 所指结点及其前驱结点的顺序
    change(p);

    // 打印交换后的链表
    q = head;
    do {
        std::cout << q->data << " ";
        q = q->next;
    } while (q != head);
    std::cout << std::endl;

    return 0;
}