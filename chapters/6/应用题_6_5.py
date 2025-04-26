"""
给定某工程的AOE-网如下，试求：

1. 这个工程最早可能在什么时间结束。

2. 求每个活动的最早开始时间和最迟开始时间。

3. 确定哪些活动是关键活动。
"""

from collections import deque


class WeightedDirectedGraph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = {}

    def add_edge(self, start, end, weight):
        if start not in self.vertices:
            raise ValueError(f"起点 {start} 不存在")
        if end not in self.vertices:
            raise ValueError(f"终点 {end} 不存在")
        self.vertices[start][end] = weight

    def visualize(self):
        print("顶点集合:", ", ".join(self.vertices.keys()))
        print("有向边及权重:")
        for start in sorted(self.vertices):
            connections = self.vertices[start]
            for end in sorted(connections):
                print(f"{start} --[{connections[end]}]--> {end}")

    def topological_sort(self):
        in_degree = {v: 0 for v in self.vertices}
        for u in self.vertices:
            for v in self.vertices[u]:
                in_degree[v] += 1

        queue = deque([v for v in self.vertices if in_degree[v] == 0])
        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v in self.vertices[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(topo_order) != len(self.vertices):
            raise ValueError("图中存在环，无法进行拓扑排序")
        return topo_order


if __name__ == "__main__":
    g = WeightedDirectedGraph()
    for i in range(1, 7):
        g.add_vertex(str(i))

    edges = [('1', '2', 2), ('1', '3', 15), ('3', '2', 4), ('2', '5', 19),
             ('3', '5', 11), ('2', '4', 10), ('4', '6', 6), ('5', '6', 5)]
    for start, end, weight in edges:
        g.add_edge(start, end, weight)

    try:
        topo_order = g.topological_sort()
    except ValueError as e:
        print(e)
        exit()

    # 计算最早发生时间
    ve = {v: 0 for v in g.vertices}
    for u in topo_order:
        for v in g.vertices[u]:
            if ve[v] < ve[u] + g.vertices[u][v]:
                ve[v] = ve[u] + g.vertices[u][v]

    # 计算最晚发生时间
    end_node = topo_order[-1]
    vl = {v: ve[end_node] for v in g.vertices}
    for u in reversed(topo_order):
        for v in g.vertices[u]:
            if vl[u] > vl[v] - g.vertices[u][v]:
                vl[u] = vl[v] - g.vertices[u][v]

    # 问题1答案
    print(f"1. 工程最早结束时间：{ve[end_node]}")

    # 问题2答案
    print("2. 每个活动的最早开始时间和最迟开始时间：")
    activities = []
    for u in g.vertices:
        for v in g.vertices[u]:
            act_name = f"{u}->{v}"
            e = ve[u]
            l = vl[v] - g.vertices[u][v]
            activities.append((act_name, e, l))
            print(f"  活动 {act_name}: 最早={e}, 最迟={l}")

    # 问题3答案
    critical_acts = [act[0] for act in activities if act[1] == act[2]]
    print("3. 关键活动：", ", ".join(critical_acts))
