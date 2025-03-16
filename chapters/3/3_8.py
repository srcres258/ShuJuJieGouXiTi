'''
【题目】
如果允许在循环队列的两端进行插入和删除操作。要求：
(1) 写出循环队列的类型定义；
(2) 写出“从队尾删除”和“从队头插入”的算法。
'''


class CircularQueue:
    """循环队列的类型定义"""

    __slots__ = ('capacity', 'queue', 'front', 'rear')

    def __init__(self, capacity):
        self.capacity = capacity  # 队列容量
        self.queue = [None] * capacity  # 初始化队列
        self.front = self.rear = -1  # 初始化队头和队尾指针

    def is_empty(self):
        return self.front == self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def size(self):
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacity - (self.front - self.rear) + 1

    def dequeue_rear(self):
        """从队尾删除元素的算法"""

        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.queue[self.rear]
        self.queue[self.rear] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.capacity
        return data

    def enqueue_front(self, data):
        """从队头插入元素的算法"""

        if self.is_full():
            raise Exception("Queue is full")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = data
