import numpy as np

class Grafo:
  def __init__(self,vertices):
    self.vertices = vertices
    self.grafo = np.zeros((vertices,vertices))

  def adicionarArestas(self, u, v, peso):
    self.grafo[u][v] = peso

  def imprimirGrafo(self):
    print('Matriz de adjacencia: ')
    print(self.grafo)
    print('Distancia')
    print(self.distancia)
    print('Pais')
    print(self.pais)

  def floydWarsahll(self):
    self.distancia = np.full((self.vertices, self.vertices), np.inf)
    self.pais = np.full((self.vertices, self.vertices), None)

    for i in range(self.vertices):
      for j in range(self.vertices):
        if self.grafo[i][j] != 0:
          self.distancia[i][j] = self.grafo[i][j]
          self.pais[i][j] = i

    for k in range(self.vertices):
      for i in range(self.vertices):
        for j in range(self.vertices):
          if self.distancia[i][j] > self.distancia[i][k] + self.distancia[k][j]:
            self.distancia[i][j] = self.distancia[i][k] + self.distancia[k][j]
            self.pais[i][j] = self.pais[k][j]

  def reconstruirCaminho(self, u, v):
    caminho = [v]
    v_atual = v
    while v_atual != u:
      anterior = self.pais[u][v_atual]
      caminho.insert(0,anterior)
      v_atual = anterior

    return caminho

g = Grafo(5)

g.adicionarArestas(0, 1, 10)
g.adicionarArestas(0, 2, 5)
g.adicionarArestas(1, 2, 2)
g.adicionarArestas(1, 3, 1)
g.adicionarArestas(2, 1, 3)
g.adicionarArestas(2, 3, 9)
g.adicionarArestas(3, 4, 4)
g.adicionarArestas(4, 0, 7)


g.floydWarsahll()
print(g.reconstruirCaminho(0,2))

g.imprimirGrafo()
