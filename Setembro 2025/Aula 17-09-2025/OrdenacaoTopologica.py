import sys

class Vertice:
    def __init__(self, num):
        self.num = num
        self.adj = []
        self.grauSaida = 0
        self.grauEntrada = 0
        self.grauTotal = 0
        self.cor = 'branco'
        self.d = sys.maxsize
        self.pi = None
        self.f = None  # tempo de finalização no DFS

    def __str__(self):
        return("Vértice:" + str(self.num) + " - Adj:" + str([v.num for v in self.adj]))


class Grafo:
    def __init__(self, n):
        self.vertices = [Vertice(i) for i in range(n)]

    def addArestas(self, u, v):
        self.vertices[u].adj.append(self.vertices[v])
        self.vertices[u].grauSaida += 1


def GrauSaida(g):
    for v in g.vertices:
        v.grauSaida = len(v.adj)

def GrauEntrada(g):
    for v in g.vertices:
        v.grauEntrada = 0
    for v in g.vertices:
        for u in v.adj:
            u.grauEntrada += 1

def GrauTotal(g):
    for v in g.vertices:
        v.grauTotal = v.grauSaida + v.grauEntrada


class BFS:
    def __init__(self, g, s):
        for v in g.vertices:
            v.cor = 'branco'
            v.d = sys.maxsize
            v.pi = None

        origem = g.vertices[s]
        origem.cor = 'cinza'
        origem.d = 0
        origem.pi = None

        Q = [origem]

        while len(Q) > 0:
            u = Q.pop(0)
            for v in u.adj:
                if v.cor == 'branco':
                    v.d = u.d + 1
                    v.pi = u
                    v.cor = 'cinza'
                    Q.append(v)
            u.cor = 'preto'

    def printCaminho(self, g, s, v):
        if v == s:
            print(s.num)
        else:
            if v.pi == None:
                print("Não há caminho")
            else:
                self.printCaminho(g, s, v.pi)
                print(v.num)


class DFS:
    def __init__(self, g):
        for v in g.vertices:
            v.cor = 'branco'
            v.pi = None
        self.time = 0
        for v in g.vertices:
            if v.cor == 'branco':
                self.DFS_Visit(g, v)

    def DFS_Visit(self, g, u):
        self.time += 1
        u.d = self.time
        u.cor = 'cinza'
        for v in u.adj:
            if v.cor == 'branco':
                v.pi = u
                self.DFS_Visit(g, v)
        u.cor = 'preto'
        self.time += 1
        u.f = self.time


class OrdenacaoTopologica:
    def __init__(self, g):
        self.pilha = []
        for v in g.vertices:
            v.cor = 'branco'
            v.pi = None
        self.time = 0
        for v in g.vertices:
            if v.cor == 'branco':
                self.DFS_Visit(g, v)
        self.pilha.reverse()

    def DFS_Visit(self, g, u):
        self.time += 1
        u.d = self.time
        u.cor = 'cinza'
        for v in u.adj:
            if v.cor == 'branco':
                v.pi = u
                self.DFS_Visit(g, v)
        u.cor = 'preto'
        self.time += 1
        u.f = self.time
        self.pilha.append(u)


# ---------- Teste ----------
# ---------- Teste ----------
G = Grafo(4)
G.addArestas(0,1)
G.addArestas(1,2)
G.addArestas(2,3)

print("Vértices e adjacências:")
for v in G.vertices:
    print(v)

# BFS
bfs = BFS(G, 0)
print("\nCaminho BFS 0 → 2:")
bfs.printCaminho(G, G.vertices[0], G.vertices[2])

# Graus
GrauSaida(G)
GrauEntrada(G)
GrauTotal(G)

# DFS para calcular tempos d e f
dfs = DFS(G)

print("\nInformações dos vértices:")
for v in G.vertices:
    print(v, " - Grau Saída:", str(v.grauSaida),
          " - Grau Entrada:", str(v.grauEntrada),
          " - Grau Total:", str(v.grauTotal))
    print("  - Descoberta (d):", str(v.d), 
          " - Finalização (f):", str(v.f),
          " - pi:", str(v.pi.num if v.pi else None))

# Ordenação Topológica
ot = OrdenacaoTopologica(G)
print("\nOrdenação Topológica:")
print([v.num for v in ot.pilha])
