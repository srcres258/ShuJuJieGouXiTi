'''
【题目】
已知Ackermann函数定义如下：

Ack(m, n) = n + 1, if m = 0
Ack(m, n) = Ack(m-1, 1), if m > 0 and n = 0
Ack(m, n) = Ack(m-1, Ack(m, n-1)), if m > 0 and n > 0

(1) 写出计算Ack(m, n)的递归算法，并根据此算法给出Ack(2, 1)的计算过程。
(2) 写出计算Ack(m, n)的非递归算法。
'''


def ack_rec(m, n):
    """递归算法"""

    if m == 0:
        return n + 1
    elif m != 0 and n == 0:
        return ack_rec(m - 1, 1)
    else:
        return ack_rec(m - 1, ack_rec(m, n - 1))


def ack_iter(m, n):
    """非递归算法（迭代算法）"""

    top = -1
    sm = [0] * 20
    sn = [0] * 20  # sm和sn是栈，容量足够大，分别存放m和n
    top += 1  # top是栈顶指针
    sm[top] = m
    sn[top] = n
    while True:
        i = sm[top]
        j = sn[top]
        top -= 1  # 参数m和n退栈
        if i == 0:  # m=0时
            k = j + 1
            if top != -1:
                sn[top] = k  # 栈不空，参数n进栈
            else:
                return k
        elif j == 0:  # n=0时
            top += 1
            sm[top] = i - 1
            sn[top] = 1
        else:  # m!=0且n!=0
            top += 1
            sm[top] = i - 1
            top += 1
            sm[top] = i
            sn[top] = j - 1
