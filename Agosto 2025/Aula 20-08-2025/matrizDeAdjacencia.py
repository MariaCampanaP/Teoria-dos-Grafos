class Grafo:
    def __init__(self, qtdVertices):
        self.qtdVertices = qtdVertices
        self.adjMatriz = [[0 for _ in range(self.qtdVertices)] for _ in range(self.qtdVertices)]

    def addAresta(self, u, v):
        self.adjMatriz[u][v] = 1
    
def GrauSaida(g):
    grauSaida = [0] * g.qtdVertices
    for i in range(g.qtdVertices):
        for j in range(g.qtdVertices):
            if g.adjMatriz[i][j] == 1:
                grauSaida[i] += 1
    return grauSaida

G = Grafo(3)
G.addAresta(0, 1)
G.addAresta(1, 2)
G.addAresta(2, 1)
grausS = GrauSaida(G)

print(G.adjMatriz)
print(grausS)