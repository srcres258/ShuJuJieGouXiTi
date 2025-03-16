'''
【题目】
将编号为0和1的两个栈存放于一个数组空间V[m]中，栈底分别处于数组的两端。当第0号栈的栈顶指针top[0]等于-1时该栈为空；当第1号栈的栈顶指针top[1]等于m时，该栈为空。
两个栈均从两端向中间填充。试编写双栈初始化，判断栈空、栈满、进栈和出栈等算法的函数。
'''

from typing import List, Tuple


SElemType = int  # 指定双栈中元素的类型

# 定义操作状态码
Status = bool
OK = True
ERROR = False


class DblStack:
    """双栈数据结构"""

    __slots__ = ('top', 'bot', 'v', 'm')

    def __init__(self):
        self.top: List[int] = [0] * 2  # 栈顶指针
        self.bot: List[int] = [0] * 2  # 栈底指针
        self.v: List[SElemType | None] | None = None  # 栈数组
        self.m: int = 0  # 栈最大可容纳的元素个数


def init_dbl_stack(S: DblStack, m: int) -> Status:
    """初始化一个大小为m的双向栈S"""

    S.v = [None] * m  # 动态分配一个最大容量为m的数组空间
    S.bot[0] = -1  # 左栈栈底指针
    S.bot[1] = m  # 右栈栈底指针
    S.top[0] = -1  # 左栈栈顶指针
    S.top[1] = m  # 右栈栈顶指针

    return OK


def dbl_push(S: DblStack, i: int, x: SElemType) -> Status:
    """向指定的i号栈中插入元素x"""

    if S.top[1] - S.top[0] == 1:
        return ERROR  # 栈满
    if i == 0:
        # 左栈：栈顶指针先加1，然后按此地址进栈
        S.top[0] += 1
        S.v[S.top[0]] = x
    else:
        # 右栈：栈顶指针先减1，然后按此地址进栈
        S.top[1] -= 1
        S.v[S.top[1]] = x


def dbl_pop(S: DblStack, i: int) -> Tuple[SElemType | None, Status]:
    """删除指定的i号栈的栈顶元素，用x返回其值"""

    if S.top[i] == S.bot[i]:
        return None, ERROR  # 栈空
    if i == 0:
        # 左栈：栈顶指针减1
        x = S.v[S.top[0]]
        S.top[0] -= 1
    else:
        # 右栈：栈顶指针加1
        x = S.v[S.top[1]]
        S.top[1] += 1

    return x, OK


def is_empty(S: DblStack, i: int) -> bool:
    """判断指定的i号栈是否为空，空返回True，否则返回False"""

    return S.top[i] == S.bot[i]


def is_full(S: DblStack) -> bool:
    """判断栈是否满，满返回True，否则返回False"""

    return S.top[0] + 1 == S.top[1]
