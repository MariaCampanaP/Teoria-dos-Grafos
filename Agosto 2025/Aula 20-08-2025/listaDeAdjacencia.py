class Vertice:
    def __init__(self, num):
        self.num = num
        self.adj = []
        self.grauSaida = 0

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
        v.grauTotal = 0
        
    for v in g.vertices:
        v.grauTotal = v.grauSaida + v.grauEntrada
        

G = Grafo(3)
G.addArestas(0,1)
G.addArestas(1,2)
G.addArestas(2,1)
print(G.vertices)

GrauSaida(G)
GrauEntrada(G)
GrauTotal(G)

for v in G.vertices:
    print(v, " - Grau Saída:", str(v.grauSaida), " - Grau Entrada:", str(v.grauEntrada), " - Grau Total:", str(v.grauTotal))