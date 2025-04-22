"""
试基于图的深度优先搜索策略设计一算法，判别以邻接表方式存储的有向图中是否存在由顶点 $v_i$ 到顶点 $v_j$ 的路径（i!=j）。
"""


def has_path_dfs(adj_list, start, end):
    """
    使用DFS判断有向图中是否存在从start到end的路径
    :param adj_list: 邻接表，结构为[[...], [...], ...]
    :param start: 起点索引
    :param end: 终点索引
    :return: 存在路径返回True，否则返回False
    """
    if start == end:
        return False  # 根据题目要求i != j，这里可以直接返回False

    visited = [False] * len(adj_list)

    def dfs(current):
        if current == end:
            return True
        visited[current] = True
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        return False

    return dfs(start)


# 测试代码
if __name__ == '__main__':
    # 测试用例1: 简单存在路径
    test_case1 = [
        [1],  # 0->1
        [2],  # 1->2
        []  # 2
    ]
    print("测试用例1:", has_path_dfs(test_case1, 0, 2))  # 应输出True

    # 测试用例2: 无路径存在
    test_case2 = [
        [1],  # 0->1
        [0],  # 1->0
        []  # 2
    ]
    print("测试用例2:", has_path_dfs(test_case2, 0, 2))  # 应输出False

    # 测试用例3: 存在环且有路径
    test_case3 = [
        [1],  # 0->1
        [2],  # 1->2
        [3],  # 2->3
        [1]  # 3->1
    ]
    print("测试用例3:", has_path_dfs(test_case3, 0, 3))  # 应输出True

    # 测试用例4: 多路径包含自环
    test_case4 = [
        [0, 2],  # 0->0, 0->2
        [],  # 1
        [1]  # 2->1
    ]
    print("测试用例4:", has_path_dfs(test_case4, 0, 1))  # 应输出True

    # 测试用例5: 孤立顶点
    test_case5 = [
        [1],  # 0->1
        [2],  # 1->2
        [0],  # 2->0
        []  # 3（孤立顶点）
    ]
    print("测试用例5:", has_path_dfs(test_case5, 0, 3))  # 应输出False
