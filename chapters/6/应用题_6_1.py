"""
给定一个有向图，请给出：

1. 每个顶点的入度和出度；

2. 邻接矩阵；

3. 邻接表；

4. 逆邻接表。
"""


class DirectedGraph:

    def __init__(self):
        # 使用字典存储邻接表，key为节点，value为有序集合（避免重复边）
        self.adjacency_dict = {
        }  # 邻接字典：使用字典adjacency_dict存储图结构，键为节点，值为该节点指向的节点集合

    def add_node(self, node):  # add_node()添加节点时自动避免重复
        """添加节点"""
        if node not in self.adjacency_dict:
            self.adjacency_dict[node] = set()

    def remove_node(self, node):  # remove_node()删除节点时会同步删除所有相关边
        """删除节点及关联的边"""
        if node in self.adjacency_dict:
            # 删除节点
            del self.adjacency_dict[node]
            # 删除其他节点指向该节点的边
            for n in self.adjacency_dict:
                if node in self.adjacency_dict[n]:
                    self.adjacency_dict[n].remove(node)

    def add_edge(self, from_node, to_node):  # add_edge()自动处理不存在的节点
        """添加有向边"""
        # 确保节点存在
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_dict[from_node].add(to_node)

    def remove_edge(self, from_node, to_node):  # remove_edge()支持定向删除边
        """删除指定方向的边"""
        if from_node in self.adjacency_dict:
            if to_node in self.adjacency_dict[from_node]:
                self.adjacency_dict[from_node].remove(to_node)

    def get_nodes(self):  # get_nodes()返回所有节点列表
        """获取所有节点"""
        return list(self.adjacency_dict.keys())

    def get_edges(self):  # get_edges()返回所有边的元组列表
        """获取所有边"""
        edges = []
        for from_node in self.adjacency_dict:
            for to_node in self.adjacency_dict[from_node]:
                edges.append((from_node, to_node))
        return edges

    def __str__(self):  # __str__()提供可视化输出
        """可视化图结构"""
        output = []
        for node in self.adjacency_dict:
            neighbors = sorted(self.adjacency_dict[node])
            output.append(f"{node} -> {', '.join(neighbors)}")
        return "\n".join(output)


if __name__ == '__main__':
    # 给定有向图
    graph = DirectedGraph()
    graph.add_node('6')
    graph.add_edge('6', '1')
    graph.add_edge('6', '2')
    graph.add_edge('6', '5')
    graph.add_edge('2', '1')
    graph.add_edge('5', '1')
    graph.add_edge('2', '4')
    graph.add_edge('4', '5')
    graph.add_edge('4', '6')
    graph.add_edge('4', '3')
    graph.add_edge('3', '2')
    graph.add_edge('3', '6')

    # 补充实现代码
    nodes = sorted(graph.get_nodes(), key=lambda x: int(x))

    # 1. 计算入度和出度
    in_degree = {node: 0 for node in nodes}
    edges = graph.get_edges()
    for from_node, to_node in edges:
        in_degree[to_node] += 1

    print("1. 每个顶点的入度和出度：")
    for node in nodes:
        print(
            f"顶点 {node}: 入度={in_degree[node]}, 出度={len(graph.adjacency_dict[node])}"
        )

    # 2. 生成邻接矩阵
    node_index = {node: i for i, node in enumerate(nodes)}
    matrix = np.zeros((len(nodes), len(nodes)), dtype=int)
    for from_node, to_node in edges:
        matrix[node_index[from_node]][node_index[to_node]] = 1

    print("\n2. 邻接矩阵：")
    print("   " + " ".join(nodes))
    for i, row in enumerate(matrix):
        print(f"{nodes[i]}  {' '.join(map(str, row))}")

    # 3. 输出邻接表
    print("\n3. 邻接表：")
    for node in nodes:
        neighbors = sorted(graph.adjacency_dict[node], key=lambda x: int(x))
        print(f"{node} -> {', '.join(neighbors) if neighbors else '无'}")

    # 4. 生成逆邻接表
    reverse_adj = {node: [] for node in nodes}
    for from_node, to_node in edges:
        reverse_adj[to_node].append(from_node)

    print("\n4. 逆邻接表：")
    for node in nodes:
        reverse_neighbors = sorted(reverse_adj[node], key=lambda x: int(x))
        print(
            f"{node} <- {', '.join(reverse_neighbors) if reverse_neighbors else '无'}"
        )
