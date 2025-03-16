'''
【题目】
从键盘上输入一个后缀表达式，试设计算法计算表达式的值。规定：逆波兰表达式的长度不超过一行，输入以“$”作为结束，操作数之间用空格分隔，操作符只可能有“+”“-”“*”“/”4种。
例如：234 34 + 2*$。
'''

from typing import List, Tuple

SElemType = float

# 定义操作状态码
Status = bool
OK = True
ERROR = False

MAXSIZE = 100  # 栈的最大容量


class SqStack:
    """顺序栈的存储结构"""

    __slots__ = ('data', 'base', 'top', 'stacksize')

    def __init__(self):
        self.data: List[SElemType | None] | None = None  # 栈中的数据
        self.base: int = 0  # 栈底指针
        self.top: int = 0  # 栈顶指针
        self.stacksize: int = 0  # 栈可用的最大容量


def init_stack(S: SqStack) -> Status:
    """构造一个空栈S"""

    S.data = [None] * MAXSIZE  # 为顺序栈动态分配一个最大容量为MAXSIZE的数组空间
    S.top = 0  # top初始为0，空栈
    S.stacksize = MAXSIZE  # stacksize置为栈的最大容量MAXSIZE

    return OK


def push(S: SqStack, e: SElemType) -> Status:
    """插入元素e为新的栈顶元素"""

    if S.top - S.base == S.stacksize:
        return ERROR  # 栈满
    # 将元素e压入栈顶，栈顶指针加1
    S.data[S.top] = e
    S.top += 1

    return OK


def pop(S: SqStack) -> Tuple[SElemType | None, Status]:
    """删除S的栈顶元素，用e返回其值"""

    if S.top == 0:
        return None, ERROR  # 栈空
    # 栈顶指针减1，将栈顶元素赋给e
    S.top -= 1
    e = S.data[S.top]

    return e, OK


def get_top(S: SqStack) -> Tuple[SElemType | None, Status]:
    """返回S的栈顶元素，不修改栈顶指针"""

    if S.top != 0:  # 栈非空
        return S.data[S.top - 1], OK  # 返回栈顶元素的值，栈顶指针不变
    else:
        return None, ERROR


CHI = 0
LINE = ""


def getchar() -> str:
    global CHI

    CHI += 1
    return LINE[CHI - 1]


def postfix() -> float:
    """计算以'$'结尾的后缀表达式的值"""

    global LINE

    OPND = SqStack()
    init_stack(OPND)  # 操作数栈初始化
    num = 0.0  # 数字初始化
    LINE = input().strip()  # 输入表达式

    ch = getchar()  # 读入后缀表达式的第一个字符
    while ch != '$':  # 表达式没有扫描完毕
        data = ""
        while ord('0') <= ord(ch) <= ord('9') or ch == '.':
            # 拼数，将读入的数字或小数点依次保存在data中
            data += ch
            ch = getchar()
        if len(data) > 0:
            num = float(data)
            push(OPND, num)  # 操作数进栈
        match ch:
            case ' ':
                # 遇到空格，继续读入表达式中的下一个字符
                pass
            case '+':
                b, _ = pop(OPND)
                a, _ = pop(OPND)
                push(OPND, a + b)
            case '-':
                b, _ = pop(OPND)
                a, _ = pop(OPND)
                push(OPND, a - b)
            case '*':
                b, _ = pop(OPND)
                a, _ = pop(OPND)
                push(OPND, a * b)
            case '/':
                b, _ = pop(OPND)
                a, _ = pop(OPND)
                push(OPND, a / b)
        ch = getchar()  # 读入表达式中的下一个字符

    return get_top(OPND)[0]  # 输出运算结果


if __name__ == '__main__':
    print("运算结果为：" + str(postfix()))
