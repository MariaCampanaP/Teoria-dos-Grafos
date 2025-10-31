import heapq

def dijkstra(grafo, origem):
    distancias = {v: float('inf') for v in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]

    while fila:
        distancia_atual, u = heapq.heappop(fila)

        # Se a distância atual for maior que a já registrada, ignora
        if distancia_atual > distancias[u]:
            continue

        # Relaxamento das arestas
        for vizinho, peso in grafo[u]:
            nova_dist = distancia_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila, (nova_dist, vizinho))
    
    return distancias

grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('D', 3)],
    'D': []
}

dist = dijkstra(grafo, 'A')
print("Distâncias mínimas a partir de A:", dist)