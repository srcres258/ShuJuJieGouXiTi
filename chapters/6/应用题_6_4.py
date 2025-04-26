"""
给定带权有向图如下列代码所示，请编写 Python 代码，使用 Dijkstra 算法求出从顶点a到其他各顶点的最短路径，
然后输出把下面的表格补充完整后的内容（`i`表示从a点出发走过i条边，`inf`表示无穷大）。

| 终点 | i = 1 | i = 2 | i = 3 | i = 4 | i = 5 | i = 6 |
| ---- | ----- | ----- | ----- | ----- | ----- | ----- |
| b | 15 (a,b) |   |   |   |   |   |
| c | 2 (a,c) |   |   |   |   |   |
| d | 12 (a,d) |   |   |   |   |   |
| e | inf |   |   |   |   |   |
| f | inf |   |   |   |   |   |
| g | inf |   |   |   |   |   |
| S(终点集) | {a,c} |   |   |   |   |   |
"""

import heapq

class WeightedDirectedGraph:
    def __init__(self):
        # 数据结构：
        # 使用字典嵌套结构存储图信息，外层字典的键为顶点名称，值为记录出边的字典
        # 出边字典的键是目标顶点，值是该边的权重
        self.vertices = {}  # 顶点字典：键为顶点名称，值为出边字典

    def add_vertex(self, name): # add_vertex()：添加顶点，自动处理重复添加
        """添加指定名称的顶点"""
        if name not in self.vertices:
            self.vertices[name] = {}

    def add_edge(self, start, end, weight): # add_edge()：添加有向边，包含严格的顶点存在性检查
        """添加带权有向边"""
        if start not in self.vertices:
            raise ValueError(f"起点 {start} 不存在")
        if end not in self.vertices:
            raise ValueError(f"终点 {end} 不存在")
        self.vertices[start][end] = weight

    def visualize(self): # visualize()：可视化输出，按字母顺序排列顶点和边
        """可视化输出图结构"""
        print("顶点集合:", ", ".join(self.vertices.keys()))
        print("有向边及权重:")
        for start in sorted(self.vertices):
            connections = self.vertices[start]
            for end in sorted(connections):
                print(f"{start} --[{connections[end]}]--> {end}")

    def dijkstra(self, start):
        # 初始化距离字典，所有顶点的距离设为无穷大，起点的距离设为0
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        
        # 优先队列，初始将起点加入队列
        pq = [(0, start)]  # (distance, vertex)
        visited = set()
        path = {start: [start]}  # 用于记录路径
        
        steps = {vertex: [] for vertex in self.vertices}  # 用于记录每一步的结果
        step_count = 0
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = path[current_vertex] + [neighbor]
                    heapq.heappush(pq, (distance, neighbor))
            
            # 记录每一步的结果
            step_count += 1
            for vertex in self.vertices:
                if vertex in visited:
                    steps[vertex].append(f"{distances[vertex]} ({' -> '.join(path[vertex])})")
                else:
                    steps[vertex].append("inf")
        
        return steps

# 测试代码
if __name__ == "__main__":
    # 创建图实例
    g = WeightedDirectedGraph()
    
    # 添加顶点测试
    for v in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        g.add_vertex(v)
    
    # 添加边测试
    edges = [
        ('a', 'b', 15),
        ('a', 'c', 2),
        ('a', 'd', 12),
        ('b', 'e', 6),
        ('c', 'e', 8),
        ('c', 'f', 4),
        ('f', 'd', 5),
        ('e', 'g', 9),
        ('f', 'g', 10),
        ('g', 'b', 4),
        ('d', 'g', 3)
    ]
    for start, end, weight in edges:
        g.add_edge(start, end, weight)
        
    # 可视化测试
    print("=== 完整图结构 ===")
    g.visualize()
    
    # 使用 Dijkstra 算法计算最短路径
    steps = g.dijkstra('a')
    
    # 输出表格
    print("\n| 终点 | i = 1 | i = 2 | i = 3 | i = 4 | i = 5 | i = 6 |")
    print("| ---- | ----- | ----- | ----- | ----- | ----- | ----- |")
    for vertex in steps:
        if vertex == 'a':
            continue
        row = f"| {vertex} | " + " | ".join(steps[vertex]) + " |"
        print(row)
    
    # 输出 S(终点集) 每一步的结果
    s_steps = ['{a}']
    current_set = {'a'}
    for i in range(1, 7):
        for vertex, distance in steps.items():
            if distance[i-1] != 'inf' and vertex not in current_set:
                current_set.add(vertex)
                break
        s_steps.append(str(current_set))
    
    print("\n| S(终点集) | i = 1 | i = 2 | i = 3 | i = 4 | i = 5 | i = 6 |")
    print("| --------- | ----- | ----- | ----- | ----- | ----- | ----- |")
    print("| " + " | ".join(s_steps) + " |")