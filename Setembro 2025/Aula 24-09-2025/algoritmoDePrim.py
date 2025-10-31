import heapq

def prim(grafo, inicio = 0):
    visitado = set()
    agm = []
    custo_total = 0
    pq = [(0, inicio, -1)] # (peso, vértice_atual, vértice_anterior)

    while pq:
        peso, u, pai = heapq.heappop(pq)
        if u in visitado:
            continue
        visitado.add(u)
        if pai != -1:
            agm.append((pai, u, peso))
            custo_total += peso
        
        for v, w in grafo[u]:
            if v not in visitado:
                heapq.heappush(pq, (w, v, u))
    
    return agm, custo_total

grafo = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 3), (3, 6)],
    2: [(0, 3), (1, 3), (3, 4)],
    3: [(1, 6), (2, 4)]
}

agm, custo = prim(grafo)
print("Arestas da AGM:", agm)
print("Custo total:", custo)