"""
设并查集的合并操作为`merge(R1,R2)`，给出下列操作的运算结果：

`merge(1,2)`

`merge(1,6)`

`merge(3,4)`

`merge(3,5)`

`merge(10,11)`

`merge(1,10)`

`merge(3,7)`

`merge(8,9)`

`merge(3,8)`

`merge(3,12)`

`merge(3,13)`

`merge(14,15)`

`merge(16,17)`

`merge(14,16)`

`merge(1,3)`

`merge(1,14)`

要求：让结点个数少的子树的根结点的双亲指针指向结点个数多的子树的根结点。
"""


class UnionFind3:

    def __init__(self):
        self.parent = {}  # parent 字典存储每个节点的父节点。
        self.size = {}  # size 字典存储以节点为根的树的节点数（用于按大小合并）。

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def find(self, x):  # find 方法实现路径压缩，使得后续查询更高效。
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

    def display(self):
        print("Node\tParent\tSize")
        for node in sorted(self.parent.keys()):
            print(f"{node}\t{self.parent[node]}\t{self.size[node]}")


MERGE_LIST = [(1, 2), (1, 6), (3, 4), (3, 5), (10, 11), (1, 10), (3, 7),
              (8, 9), (3, 8), (3, 12), (3, 13), (14, 15), (16, 17), (14, 16),
              (1, 3), (1, 14)]

if __name__ == '__main__':
    uf = UnionFind3()
    for i in range(1, 18):
        uf.add(i)
    for a, b in MERGE_LIST:
        uf.merge(a, b)
    uf.display()
