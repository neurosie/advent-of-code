import sys

part = 2

with open(sys.argv[1], 'r') as f:
    logs = []
    for line in f:
        logs.append(line.rstrip())
    logs.sort()

    id = 0
    time = 0
    when_sleeping = {}
    total_minutes = {}
    for log in logs:
        kw = log.split(' ')[3]
        min = int(log[15:17])
        if kw == "asleep":
            time = min
        elif kw == "up":
            if id not in total_minutes:
                total_minutes[id] = 0
                when_sleeping[id] = [0 for _ in range(60)]
            total_minutes[id] += min - time
            for i in range(time, min):
                when_sleeping[id][i] += 1
        else:
            id = int(kw[1:])
    if part == 1:
        sleepiest = max(total_minutes.items(), key=lambda x: x[1])[0]
        sleepy_time = max(enumerate(when_sleeping[sleepiest]),
                          key=lambda x: x[1])[0]
    else:
        sleepiest, (sleepy_time, _) = max(
            ((id, max(enumerate(freq), key=lambda x: x[1]))
                for id, freq in when_sleeping.items()),
            key = lambda x: x[1][1])
    print(sleepiest * sleepy_time)
