'''
【题目】
回文是指正读、反读均相同的字符序列，如“abba”、“abdba”均是回文，但“good”不是回文。试设计算法判定给定的字符序列是否为回文。（提示：将一半字符入栈。）
'''

def is_palindrome(s: str) -> bool:
    """判断给定的字符序列是否为回文。"""

    result = True
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            result = False
            break
    return result


if __name__ == '__main__':
    s = input("请输入一个字符串：")
    if is_palindrome(s):
        print(f"{s} 是回文")
    else:
        print(f"{s} 不是回文")
