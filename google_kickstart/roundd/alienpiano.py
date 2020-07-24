# second round wrong answer
import numpy
T = int(input())
F = T+1
while T > 0:
    N = int(input())
    line = input().split()
    line = list(map(int, line))
    pos = 0
    neg = 0
    error_count = 0
    for num in range(N-1):
        if neg - pos == 3:
            if line[num+1] < line[num]:
                if line[num+2] < line[num+1]:
                    pos += 2
                else: pos += 3
                continue
        if pos - neg == 3:
            if line[num+1] > line[num]:
                if line[num+2] > line[num+1]:
                    neg += 2
                else: neg += 3
                continue
        if line[num] > line[num+1]:
            pos += 1
        elif line[num] < line[num+1]:
            neg += 1
        else: continue
        if numpy.absolute(pos-neg) == 4:
            error_count += 1
            pos = 0
            neg = 0
    print("Case #"+str(F-T)+":", error_count)
    T -= 1
