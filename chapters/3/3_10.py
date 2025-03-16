'''
【题目】
已知f为单链表的表头指针，链表中存储的都是整型数据，试写出实现下列运算的递归算法：
(1) 求链表中的最大整数；
(2) 求链表的结点个数；
(3) 求所有整数的平均值。
'''


class ListNode:
    __slots__ = ('val', 'next')

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_max_value(head):
    """求链表中的最大整数"""

    if not head:  # 链表为空
        return float('-inf')  # 返回一个较小的整数作为初始最大值
    if not head.next:  # 链表只有一个结点
        return head.val
    return max(head.val, get_max_value(head.next))  # 递归地比较当前结点的值和剩余结点中的最大值


def get_node_count(head):
    """求链表的结点个数"""

    if not head:  # 链表为空
        return 0
    return 1 + get_node_count(head.next)  # 递归地对链表的下一个结点调用该函数，并将结果加1


def get_average(head):
    """求所有整数的平均值"""

    if not head:  # 链表为空
        return 0
    total = head.val
    count = 1
    if head.next:
        sub_total, sub_count = get_average(head.next)
        total += sub_total
        count += sub_count
    return total, count


if __name__ == '__main__':
    # 构造链表
    head = ListNode(5)
    node2 = ListNode(8)
    node3 = ListNode(3)
    node4 = ListNode(2)
    head.next = node2
    node2.next = node3
    node3.next = node4
    # 求链表中的最大整数
    max_value = get_max_value(head)
    print("Max value:", max_value)
    # 求链表的结点个数
    node_count = get_node_count(head)
    print("Node count:", node_count)
    # 求所有整数的平均值
    total, count = get_average(head)
    average = total / count
    print("Average:", average)
