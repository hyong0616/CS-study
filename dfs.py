#Using Stack with DFS
def dfs(graph, start) :
    visited = []
    stack = [start]
    
    while stack :
        now = stack.pop()
        if now not in visited :
            visited.append(now)
            stack.extend(graph[now])

    return visited


#Using recursive Algorithm with DFS
def dfs_recursive(graph,now,visited):
    visited.append(now)
    for v in graph[now] :
        if v not in visited: 
            dfs_recursive(graph,v,visited)

def dfs2(graph,start):
    visited[]
    dfs_recursive(graph,start,visited)
    return visited
