def bellman_ford(vertices, arestas, origem):

    # Passo 1: Inicialização
    distancia = [float('inf')] * vertices
    distancia[origem] = 0

    # Passo 2: Relaxa as arestas V-1 vezes
    for _ in range(vertices - 1):
        for u, v, peso in arestas:
            if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                distancia[v] = distancia[u] + peso
    
    # Passo 3: Detecta ciclos negativos
    for u, v, peso in arestas:
        if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
            print("Ciclo negativo detectado!")
            return None
        
    return distancia

arestas = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 4),
    (3, 1, 2)
]

distancias = bellman_ford(4, arestas, 0)

if distancias:
    print("Distâncias mínimas a partir do vértice 0:", distancias)