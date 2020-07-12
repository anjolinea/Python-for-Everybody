# Memory Exceeded for Test 2

T = int(input())
F = T+1
while T > 0:
    line = input().split()
    line = list(map(int, line))
    N, D = line
    line = input().split()
    line = list(map(int, line))
    line.reverse()
    # find starting point using last point
    past_list = list(range(0, D + 1, line[0]))
    start_point = past_list[-1]
    if len(line) == 1:
        print("Case #" + str(F-T) + ":", start_point)
    else:
        for num in line[1:]:
            now_list = list(range(0, start_point+1, num))
            start_point = now_list[-1]
        print("Case #"+str(F-T)+":", now_num)
    T -= 1
