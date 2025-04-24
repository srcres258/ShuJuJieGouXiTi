"""
给定一个带权无向图，请给出该图的：

1. 邻接矩阵；

2. 邻接表；

3. 最小生成树。
"""


class WeightedUndirectedGraph:

    def __init__(self):
        self.graph = {}  # 邻接表，结构为：{节点: {邻居: 权重}}

    def add_node(self, name):
        """添加指定名称的节点"""
        if name not in self.graph:
            self.graph[name] = {}

    def add_edge(self, node1, node2, weight):
        """在指定节点间添加带权无向边，自动处理未创建节点"""
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight

    def get_nodes(self):
        """获取所有节点列表"""
        return list(self.graph.keys())

    def get_edges(self):
        """获取所有边列表，格式：(节点1, 节点2, 权重)"""
        edges = []
        for node in self.graph:
            for neighbor, weight in self.graph[node].items():
                if node < neighbor:
                    edges.append((node, neighbor, weight))
        return sorted(edges, key=lambda x: (x[0], x[1]))

    def print_adjacency_matrix(self):
        nodes = sorted(self.get_nodes())
        print("邻接矩阵:")
        print("   " + "  ".join(nodes))
        for row in nodes:
            line = [str(self.graph[row].get(col, 0)) for col in nodes]
            print(f"{row}  {'  '.join(line)}")

    def print_adjacency_list(self):
        print("邻接表:")
        for node in sorted(self.graph.keys()):
            neighbors = sorted(self.graph[node].items(), key=lambda x: x[0])
            neighbors_str = ", ".join([f"{n}({w})" for n, w in neighbors])
            print(f"{node}: {neighbors_str}")

    def get_min_spanning_tree(self):
        edges = sorted(self.get_edges(), key=lambda x: x[2])
        parent = {}

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u

        for node in self.get_nodes():
            parent[node] = node

        mst_edges = []
        for edge in edges:
            u, v, weight = edge
            if find(u) != find(v):
                union(u, v)
                mst_edges.append((u, v, weight))
            if len(mst_edges) == len(self.get_nodes()) - 1:
                break

        return sorted(mst_edges, key=lambda x: (x[0], x[1]))


# 示例用法
if __name__ == "__main__":
    g = WeightedUndirectedGraph()

    # 添加节点
    g.add_node("a")
    g.add_node("b")
    g.add_node("c")
    g.add_node("d")
    g.add_node("e")
    g.add_node("f")
    g.add_node("g")
    g.add_node("h")

    # 添加边
    g.add_edge("a", "b", 4)
    g.add_edge("a", "c", 3)
    g.add_edge("b", "c", 5)
    g.add_edge("b", "d", 5)
    g.add_edge("c", "d", 5)
    g.add_edge("b", "e", 9)
    g.add_edge("d", "e", 7)
    g.add_edge("d", "h", 4)
    g.add_edge("c", "h", 5)
    g.add_edge("e", "f", 3)
    g.add_edge("d", "f", 6)
    g.add_edge("d", "g", 5)
    g.add_edge("f", "g", 2)
    g.add_edge("h", "g", 6)

    # 查询信息
    print("结点列表:", g.get_nodes())
    print("边列表:", g.get_edges())

    # 输出三个问题的结果
    g.print_adjacency_matrix()
    print()  # 空行分隔
    g.print_adjacency_list()
    print("\n最小生成树边列表:", g.get_min_spanning_tree())
