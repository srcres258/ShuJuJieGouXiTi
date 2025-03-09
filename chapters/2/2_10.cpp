/*
【题目】
已知长度为n的线性表A采用顺序存储结构，请设计一个时间复杂度为O(n)、空间复杂度为O(1)的算法，该算法可删除线性表中所有值为item的数据元素。
*/

#include <iostream>

/*
算法思路：

首先，使用两个指针i和j遍历线性表，其中i指向当前要删除的元素，j指向下一个要被检查的元素。

然后，如果当前元素的值不等于item，则将该元素复制到i位置，并将i指针向后移动1个位置。

最后，将线性表的长度设置为i，即删除了所有值为item的元素。
*/
int removeItem(int *A, int n, int item) {
    int i = 0; // 初始化i指向第一个位置
    int j = 0; // 初始化j指向第一个位置
    while (j < n) { // 循环遍历整个线性表
        if (A[j] != item) { // 如果当前元素的值不等于item
            A[i] = A[j]; // 将该元素复制到i位置
            i++; // i指针向后移动1个位置
        }
        j++; // j指针向后移动1个位置
    }
    return i; // 返回删除元素后线性表的长度
}

int main() {
    // 定义一个示例线性表
    int A[] = {11, 45, 14, 19, 19, 81, 0};
    int n = sizeof(A) / sizeof(A[0]);

    // 打印原始线性表
    for (int i = 0; i < n; i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;

    // 删除线性表中所有值为19的元素
    int item = 19; // 要删除的元素
    n = removeItem(A, n, item);

    // 打印删除元素后的线性表
    for (int i = 0; i < n; i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}