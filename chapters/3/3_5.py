'''
【题目】
假设以I和O分别表示入栈和出栈操作。栈的初态和终态均为空，入栈和出栈的操作序列可表示为仅由I和O组成的序列，称可以操作的序列为合法序列，否则称为非法序列。写出一个算法，
判定所给的操作序列是否合法。若合法，返回true，否则返回false（假定被判定的操作序列已存入一维数组中）。
'''


def is_valid_sequence(operations: str) -> bool:
    """判定所给的操作序列是否合法"""

    size = 0
    for op in operations:
        match op:
            case 'I':
                size += 1
            case 'O':
                if size == 0:
                    return False
                size -= 1
    return size == 0


if __name__ == '__main__':
    operations = input("请输入操作序列：")
    if is_valid_sequence(operations):
        print("合法序列")
    else:
        print("非法序列")
