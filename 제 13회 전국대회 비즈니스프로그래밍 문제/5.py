import bisect
N = int(input()) 
difficulty = list(map(int, input().split()))
lis = []
for diff in difficulty:
    pos = bisect.bisect_left(lis, diff)
    if pos == len(lis):
        lis.append(diff)
    else:
        lis[pos] = diff
print(len(lis))