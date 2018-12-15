import sys, heapq

part = 2

graph = {}
incoming = {}
with open(sys.argv[1]) as f:
    for line in f:
        s = line.split(" ")[1]
        d = line.split(" ")[-3]
        if s in graph:
            graph[s].append(d)
        else:
            graph[s] = [d]
        if d not in graph:
            graph[d] = []
        if d in incoming:
            incoming[d] += 1
        else:
            incoming[d] = 1
        if s not in incoming:
            incoming[s] = 0

q = [k for k, v in incoming.items() if v == 0]
heapq.heapify(q)
order = []
if part == 1:
    while len(q) > 0:
        top = heapq.heappop(q)
        order.append(top)
        for next in graph[top]:
            incoming[next] -= 1
            if incoming[next] == 0:
                heapq.heappush(q, next)

    print("".join(order))
else:
    base_duration = 61
    workers = 5

    time = 0

    idle = (None, float('inf'))
    working_on = [idle for _ in range(workers)]

    while len(order) < len(graph):
        # assign tasks
        for i in range(workers):
            if working_on[i][0] == None and len(q):
                task = heapq.heappop(q)
                working_on[i] = (task, time + (ord(task) - ord('A') + base_duration))
        # advance time
        time = min(working_on, key=lambda x: x[1])[1]
        for i in range(workers):
            if working_on[i][1] == time:
                done = working_on[i][0]
                order.append(done)
                for next in graph[done]:
                    incoming[next] -= 1
                    if incoming[next] == 0:
                        heapq.heappush(q, next)
                working_on[i] = idle
    print(time)
