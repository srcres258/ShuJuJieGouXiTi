'''
【题目】
设从键盘输入一整数的序列a_1，a_2，…，a_n，试设计算法实现：用栈结构存储输入的整数，当a_i!=-1时将a_i进栈；当a_i=-1时，输出栈顶整数并出栈。
算法应对异常情况（栈满等）给出相应的信息。
'''

from typing import List


def in_out_s(s: List[int], n: int, maxsize: int) -> None:
    """
    s是元素为整数的栈，根据读入的数据完成入栈和出栈操作。
    n为总共将要输入的整数序列的长度。
    maxsize为栈的最大容量。
    """

    top = 0  # top为栈顶指针，top=0时为栈空
    for i in range(1, n + 1):
        x = int(input())  # 从键盘读入整数序列
        if x != -1:  # 读入的整数不等于-1时入栈
            if top == maxsize - 1:
                print("栈满")
                return
            else:
                top += 1
                s[top] = x
        else:  # 读入的整数等于-1时退栈
            if top == 0:
                print("栈空")
                return
            else:
                print(f"出栈元素是{s[top]}")
                top -= 1


if __name__ == '__main__':
    s = [0] * 100  # 栈的容量为100
    n = int(input())  # 输入整数序列的长度
    maxsize = 100  # 栈的最大容量
    in_out_s(s, n, maxsize)  # 调用函数
