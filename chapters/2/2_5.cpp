/*
【题目】
设计算法将一个带头结点的单链表A分解为两个具有相同结构的链表B和C，其中B表的结点为A表中值小于0的结点，而C表的结点为A表中值大于0的结点
（链表A中的元素为非零整数，要求B、C表利用A表的结点）。

【解题思路】
题目要求将一个单链表A分解为两个具有相同结构的链表B、C，因此，此题的关键在于：

1. B表的头结点可以使用原来A表的头结点，而需要为C表新申请一个头结点；
2. 对A表进行遍历的同时进行分解，完成结点的重新链接，在此过程中需要记录遍历的后继结点以防止链接后丢失后继结点；
3. 本题并未要求链表中结点的数据值有序，所以在摘取满足条件的结点进行链接时，可以采取前插法，也可以采取后插法。因为前插法的实现相对简单，下面的算法描述中采取了前插法。

首先将B表的头结点初始化A表的头结点，为C表新申请一个头结点，初始化为空表。从A表的首元结点开始，依次对A表进行遍历。p为工作指针，r为p的后继指针。当`p->data < 0`时，
将p指向的结点使用前插法插入到B表；当`p->data > 0`时，将p指向的结点使用前插法插入到C表；然后p指向新的待处理的结点（`p = r`）。
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
    Node *head = new Node; // 带头结点的链表
    Node *cur = head;
    for (int i = 0; i < len; i++) {
        Node *p = new Node;
        std::cin >> p->value; 
        cur->next = p;
        cur = p;
    }

    return head;
}

// 算法主体部分：单链表A分解为两个具有相同结构的链表B和C。
std::pair<Node *, Node *> decompose(Node *a) {
    Node *b = a;
    Node *p = a->next; // p为工作指针
    b->next = nullptr; // 表b初始化
    Node *c = new Node; // 为c申请结点空间
    c->next = nullptr; // c初始化为空表
    while (p) {
        Node *r = p->next; // 暂存p的后继
        if (p->value < 0) {
            // 将小于0的结点链入表b，前插法
            p->next = b->next;
            b->next = p;
        } else {
            // 将大于0的结点链入表c，前插法
            p->next = c->next;
            c->next = p;
        }
        p = r; // p指向新的待处理结点
    }

    return std::make_pair(b, c);
}

int main() {
    std::cout << "请输入非零整数单链表A：" << std::endl;
    Node *la = inputList();

    auto result = decompose(la);

    std::cout << "B表：";
    Node *p = result.first->next;
    while (p) {
        std::cout << p->value << " ";
        p = p->next;
    }
    std::cout << std::endl;

    std::cout << "C表：";
    p = result.second->next;
    while (p) {
        std::cout << p->value << " ";
        p = p->next;
    }
    std::cout << std::endl;

    return 0;
}