"""
【题目】
设计算法，实现下面函数的功能。函数insert(s, t, pos)将字符串t插入到字符串s中，插入位置为pos。假设分配给字符串s的空间足够让字符串t插入。
（说明：不得使用任何库函数）
"""


def insert(s: str, t: str, pos: int) -> str:
    s = list(s)
    for i in range(pos, pos + len(t)):
        tmp = s[i]
        s[i] = t[i - pos]
        s[i + pos + 1] = tmp
    return ''.join(s)


if __name__ == '__main__':
    s = "123456" + '\0' * 114
    t = "test"
    pos = 3
    s = insert(s, t, pos)
    print(s)  # 123test456