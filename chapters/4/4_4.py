"""
【题目】
已知字符串s1存放一段英文，设计算法format(s1, s2, s3, n)，要求将s1按给定的长度n格式化成两端对齐的字符串存储在s2中
（即确保s2长度为n且首尾字符不得为空格），s1多余的字符存储在s3中。
"""


from typing import Tuple


def format(s1: str, s2: str, s3: str, n: int) -> Tuple[str, str]:
    words = s1.split() # 将字符串按空格分割成单词列表
    length = len(words) # 单词数量
    total_word_len = sum(len(word) for word in words) # 单词总长度
    space_count = n - total_word_len # 需要插入的总空格数
    if space_count >= length - 1: # 若空格数大于等于单词之间的间隙数，则直接在每个单词之间插入空格
        avg_space = space_count // (length - 1) # 平均每个间隙插入的空格数
        extra_space = space_count % (length - 1) # 多余的空格数
        s2 + words[0] # 首个单词添加到s2
        for i in range(1, length): # 遍历剩下的单词，每个单词前面插入空格
            s2 += ' ' * avg_space # 插入平均间隙空格
            if extra_space > 0: # 若还有多余空格，则插入额外一个空格
                s2 += ' '
            extra_space -= 1
            s2 += words[i] # 插入单词到s2
    else: # 若空格数小于单词之间的间隙数
        s2 += words[0] # 首个单词添加到s2
        for i in range(1, length): # 遍历剩下的单词，每个单词前面插入空格
            s2 += ' ' + words[i] # 插入单词到s2
            space_count -= 1 # 每插入一个单词，空格数减少一个
        s3 = ' ' * space_count # 剩余的空格数保存到s3
        s3 += ' ' + words[-1] # 将最后一个单词添加到s3

    return s2, s3