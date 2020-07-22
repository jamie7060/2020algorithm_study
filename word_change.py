# DFS => stack
# BFS => queue

# 한글자만 차이나는 애들 비교
# len([i for i in range(0,len(words[w])) if words[w][i]!=stack[i]]) == 1 출처: https://khann.tistory.com/79 [khann's IT와 경제 블로그]
def cmp(w1,w2):
    a1 = list(w1)
    a2 = list(w2)
    difference = 0
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            difference += 1
    if difference == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    if target not in words:
        return 0
    graph = {}
    words.append(begin)
    
    for i in words:
        graph[i] = []
    
    for i in graph.keys():
        for j in words:
            if cmp(i,j):
                graph[i].append(j)
    
    stack = [begin]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # extend(): Iterates over its argument and adding each element to the list and extending the list. 
            stack.extend(graph[node])
            if visited[-1] == target:
                break
                
    return len(visited)-1

#BFS 이용 풀이
# from collections import deque


# def get_adjacent(current, words):
#     for word in words:
#         if len(current) != len(word):
#             continue

#         count = 0
#         for c, w in zip(current, word):
#             if c != w:
#                 count += 1

#         if count == 1:
#             yield word


# def solution(begin, target, words):
#     dist = {begin: 0}
#     queue = deque([begin])

#     while queue:
#         current = queue.popleft()

#         for next_word in get_adjacent(current, words):
#             if next_word not in dist:
#                 dist[next_word] = dist[current] + 1
#                 queue.append(next_word)

#     return dist.get(target, 0)