/*
【题目】
设计一个算法，删除递增有序链表中值大于mink且小于maxk的所有元素（mink和maxk是给定的两个参数，其值可以和表中的元素相同，也可以不同）。
*/

#include <iostream>

struct Node {
    int value = 0;
    Node *next = nullptr;

    Node() = default;
    Node(int v) : value(v) {}
};

Node *deleteRangeElements(Node *head, int mink, int maxk) {
    Node *dummy = new Node; // 创建一个虚拟头结点
    dummy->next = head;
    Node *current = dummy;
    while (current->next) {
        if (current->next->value > mink && current->next->value < maxk) {
            current->next = current->next->next; // 删除节点
        } else {
            current = current->next;
        }
    }
    return dummy->next; // 返回删除后的链表
}

int main() {
    // 创建一个递增有序链表：1 -> 3 -> 5 -> 7 -> 9
    Node *head = new Node(1);
    Node *current = head;
    int values[] = {3, 5, 7, 9};
    for (int value : values) {
        current->next = new Node(value);
        current = current->next;
    }

    int mink = 3;
    int maxk = 7;
    Node *newHead = deleteRangeElements(head, mink, maxk);

    // 输出删除后的链表：1 -> 3 -> 7 -> 9
    current = newHead;
    while (current) {
        std::cout << current->value << " -> ";
        current = current->next;
    }

    return 0;
}