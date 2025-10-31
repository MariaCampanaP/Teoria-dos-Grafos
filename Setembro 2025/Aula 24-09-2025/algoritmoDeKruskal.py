class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)
        if raiz_u == raiz_v:
            return False # já estão conectados
        if self.rank[raiz_u] < self.rank[raiz_v]:
            self.parent[raiz_u] = raiz_v
        elif self.rank[raiz_u] > self.rank[raiz_v]:
            self.parent[raiz_v] = raiz_u
        else:
            self.parent[raiz_v] = raiz_u
            self.rank[raiz_u] += 1
        return True

def kruskal(n, arestas):
    arestas.sort() # ordena pelo peso
    uf = UnionFind(n)
    agm = []
    custo_total = 0

    for peso, u, v in arestas:
        if uf.union(u, v):
            agm.append((u, v, peso))
            custo_total += peso
    
    return agm, custo_total

arestas = [
    (1, 0, 1),
    (3, 0, 2),
    (3, 1, 2),
    (6, 1, 3),
    (4, 2, 3),
]

agm, custo = kruskal(4, arestas)
print("Arestas da AGM:", agm)
print("Custo total:", custo)