from collections import defaultdict, deque

# 定义一个图类
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    # 添加边
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # 深度优先搜索
    def dfs(self, start_vertex):
        visited = [False] * (self.V + 1)
        traversal_path = []
        self._dfs_util(start_vertex, visited, traversal_path)
        return traversal_path

    # 辅助的DFS函数
    def _dfs_util(self, v, visited, traversal_path):
        visited[v] = True
        traversal_path.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs_util(i, visited, traversal_path)

    # 广度优先搜索
    def bfs(self, start_vertex):
        visited = [False] * (self.V + 1)
        queue = deque([start_vertex])
        traversal_path = []
        visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            traversal_path.append(vertex)
            for i in self.graph[vertex]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

        return traversal_path

# 根据邻接矩阵创建图
def create_graph_from_adj_matrix(adj_matrix):
    vertices = len(adj_matrix)
    graph = Graph(vertices - 1)  # 因为邻接矩阵的第一行和第一列是顶点的标签，不计入顶点数量
    for i in range(1, vertices):
        for j in range(1, vertices):
            if adj_matrix[i][j] == 1:
                graph.add_edge(i, j)
    return graph

# 定义邻接矩阵
adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # 顶点标签行
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 顶点1
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # 顶点2
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],  # 顶点3
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # 顶点4
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 顶点5
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # 顶点6
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],  # 顶点7
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],  # 顶点8
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 顶点9
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]   # 顶点10
]

# 创建图
graph = create_graph_from_adj_matrix(adj_matrix)

# 计算DFS生成树
dfs_result = graph.dfs(1)
print(f"DFS生成树（从顶点1开始）: {dfs_result}")

# 计算BFS生成树
bfs_result = graph.bfs(1)
print(f"BFS生成树（从顶点1开始）: {bfs_result}")
