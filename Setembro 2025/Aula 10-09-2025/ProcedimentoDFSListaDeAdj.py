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
        return f"Vértice:{self.num} - Adj:{[v.num for v in self.adj]}"

class Grafo:
    def __init__(self, n):
        self.vertices = [Vertice(i) for i in range(n)]
    
    def addArestas(self, u, v):
        self.vertices[u].adj.append(self.vertices[v])

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
        while Q:
            u = Q.pop(0)
            for v in u.adj:
                if v.cor == 'branco':
                    v.d = u.d + 1
                    v.pi = u
                    v.cor = 'cinza'
                    Q.append(v)
            u.cor = 'preto'
        
def printCaminho(g, s, v):
    if v == s:
        print(s.num, end=" ")
    else:
        if v.pi is None:
            print("Não há caminho")
        else:
            printCaminho(g, s, v.pi)
            print(v.num, end=" ")

class DFS:
    def __init__(self, g, s):
        for v in g.vertices:
            v.cor = 'branco'
            v.pi = None
            v.d = None
            v.f = None
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

# ------------------- TESTE -------------------

G = Grafo(3)
G.addArestas(0,1)
G.addArestas(1,2)
G.addArestas(2,1)  # cria ciclo entre 1 <-> 2

print("Lista de Vértices:")
for v in G.vertices:
    print(v)

bfs = BFS(G, 0)
dfs = DFS(G, 0)

# Calcula graus
GrauSaida(G)
GrauEntrada(G)
GrauTotal(G)

# Caminho de 0 até 2
print("\nCaminho de 0 até 2:")
printCaminho(G, G.vertices[0], G.vertices[2])
print("\n")

# Infos de cada vértice
for v in G.vertices:
    print(f"{v} - Grau Saída: {v.grauSaida} - Grau Entrada: {v.grauEntrada} - Grau Total: {v.grauTotal}")
    print(f"  - d: {v.d} - pi: {v.pi.num if v.pi else None} - f: {v.f}")
