class UnionFind:
    def __init__(self, n):
        # Initialize the parent and rank arrays
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.groups = n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        # Union the sets that contain p and q
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP  == rootQ:
            return True

        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
            self.rank[rootP] +=self.rank[rootQ]
        else:
                
            self.parent[rootP] = rootQ
            self.rank[rootQ] += self.rank[rootP]
        self.groups-=1
        

  

class Solution:
    def findCircleNum(self, nodes: List[List[int]]) -> int:
        uf = UnionFind(len(nodes))

        
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if   nodes[i][j]==1 :
                    uf.union(i,j)

        father=set(uf.parent)
        return uf.groups