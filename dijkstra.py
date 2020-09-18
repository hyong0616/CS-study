import heapq 

def dijkstra (graph, start) :
    dist = [100001 for _ in range(len(graph))]
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [dist[start],start])

    while queue :
        now_weight, now_node = heapq.heappop(queue)
        
        if dist[now_node] < now_weight :
            continue
        
        for nxt, weight in graph[now_node].items() :
            dis = now_weight + weight

            if dis < dist[nxt] :
                dist[nxt] = dis
                heapq.heappush(queue,[dis, nxt])