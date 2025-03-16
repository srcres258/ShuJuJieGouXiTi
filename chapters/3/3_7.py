'''
【题目】
假设以数组Q[m]存放循环队列中的元素，同时设置一个标志tag，以tag==0和tag==1来区别在队头指针（front）和队尾指针（rear）相等时，队列状态是“空”还是“满”。
试编写与此结构相应的插入（enqueue）和删除（dequeue）算法。
'''

from typing import List, Tuple


def enqueue(Q: List[int], rear: int, front: int, x: int, tag: int,
            m: int) -> int:
    """插入（enqueue）算法"""

    if front == rear and tag == 1:
        # 队列满的情况
        print("Queue is full!")
        return tag
    Q[rear] = x
    rear = (rear + 1) % m  # 循环移动
    tag = 1  # 设置tag为1，标识队列非空

    return tag


def dequeue(Q: List[int], rear: int, front: int, tag: int,
            m: int) -> Tuple[int, int | None]:
    """删除（dequeue）算法"""

    if front == rear and tag == 0:
        # 队列空的情况
        print("Queue is empty!")
        return tag, None
    x = Q[front]
    front = (front + 1) % m  # 循环移动
    if front == rear:  # 如果删除元素后队列为空
        tag = 0  # 设置tag为0

    return tag, x
