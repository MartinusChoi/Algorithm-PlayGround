from collections import deque

def solution(n, k):
    queue = deque([i+1 for i in range(n)])

    while len(queue) > 1:
        for _ in range(k-1) : 
            queue.append(queue.popleft())
        queue.popleft()

    return queue[0]