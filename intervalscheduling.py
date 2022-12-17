class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def find_max_nonoverlapping(intervals):
    max = 0
    prev_end = 0
    
    intervals.sort(key=lambda interval: interval.end)

    for interval in intervals:
        if interval.start >= prev_end:
            max += 1
            prev_end = interval.end

    return max

numOfIntervals = int(input())
intervals = []
for i in range(numOfIntervals):
    start, end = map(int, input().split())
    intervals.append(Interval(start, end))

print(find_max_nonoverlapping(intervals))
