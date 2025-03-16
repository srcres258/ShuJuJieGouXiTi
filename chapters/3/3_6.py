'''
【题目】
假设以带头结点的循环链表表示队列，并且只设一个指针指向队尾元素结点（注意：不设头指针），试编写相应的置空队列、判断队列是否为空、入队和出队等算法。
'''

from typing import Tuple

QElemType = int  # 队列中的元素类型

# 定义操作状态码
Status = bool
OK = True
ERROR = False


class QNode:
    """队列的链式存储结构"""

    __slots__ = ('data', 'next')

    def __init__(self):
        self.data: QElemType | None = None
        self.next: QNode | None = None


class LinkQueue:
    __slots__ = ('rear', )

    def __init__(self):
        self.rear: QNode | None = None  # 只设一个尾指针


def init_queue(Q: LinkQueue) -> None:
    """置空队列"""

    Q.rear = Q.rear.next  # 将尾指针指向头结点
    while Q.rear != Q.rear.next:  # 当列非空时，将队中元素逐个出队
        s = Q.rear.next  # s指向队头元素
        Q.rear.next = s.next  # 尾结点的指针域指向新的队头元素


def empty_queue(Q: LinkQueue) -> bool:
    """判断队列是否为空，空则返回True，否则返回False"""

    # 队列只有一个头结点，即当头结点的指针域指向自己时，队列为空
    return Q.rear.next.next == Q.rear.next


def enqueue(Q: LinkQueue, e: QElemType) -> Status:
    """入队，插入元素e为Q的新的队尾元素"""

    p = QNode()  # 申请新结点
    p.data = e  # 将新结点的数据域置为e
    p.next = Q.rear.next  # 将新结点插入到队尾
    Q.rear.next = p
    Q.rear = p  # 将尾指针移至新结点

    return OK


def dequeue(Q: LinkQueue) -> Tuple[QElemType | None, Status]:
    """出队，删除Q的队头元素，并返回队头元素的值"""

    if Q.rear.next.next == Q.rear.next:
        return None, ERROR  # 若队列空，则返回ERROR
    p = Q.rear.next.next  # p指向队头元素
    e = p.data  # e保存队头元素的值

    if p == Q.rear:
        Q.rear = Q.rear.next  # 修改尾指针，使其指向头结点
        Q.rear.next = p.next
    else:
        Q.rear.next.next = p.next  # 摘下结点p

    return e, OK
