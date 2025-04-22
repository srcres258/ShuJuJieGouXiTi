"""
采用邻接表存储结构，设计一个算法，判别无向图中任意给定的两个顶点之间是否存在一条长度为`k`的简单路径。
"""


def dfs(current, target, k, visited, graph):
    if k == 0:
        return current == target
    visited.add(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(neighbor, target, k - 1, visited, graph):
                return True
    visited.remove(current)
    return False


def has_k_simple_path(graph, u, v, k):
    visited = set()
    return dfs(u, v, k, visited, graph)


# 测试用例
if __name__ == "__main__":
    # 测试用例1：存在路径0-1-2，k=2
    graph1 = {0: [1], 1: [0, 2], 2: [1]}
    assert has_k_simple_path(graph1, 0, 2, 2) == True

    # 测试用例2：不存在路径0-2，k=1
    assert has_k_simple_path(graph1, 0, 2, 1) == False

    # 测试用例3：起点终点相同，k=0
    assert has_k_simple_path(graph1, 0, 0, 0) == True

    # 测试用例4：长路径0-1-2-3，k=3
    graph2 = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
    assert has_k_simple_path(graph2, 0, 3, 3) == True

    # 测试用例5：环状图不存在简单路径
    graph3 = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert has_k_simple_path(graph3, 0, 0, 3) == False

    print("所有测试用例通过！")
