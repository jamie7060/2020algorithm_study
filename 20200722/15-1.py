graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

def DFS(graph, start):
    stack = []
    visited = []
    if start not in graph:
        print("탐색이 불가능합니다. (시작점 없음)")
        return -1
    else:
        stack.append(start)
    
    while(stack):
        x = stack.pop()
        if x not in visited:
            visited.append(x)
            graph[x].reverse()
            stack.extend(graph[x])
    return visited

print(DFS(graph, 1))

