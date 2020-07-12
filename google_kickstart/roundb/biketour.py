T = int(input())
count = 1
while T > 0:
    if count%2 == 1:
        N = int(input())
    else:
        line = input().split()
        line = list(map(int, line))
        temp_count = 0
        for num in range(1, N - 1):
            if line[num] > line[num - 1] and line[num] > line[num + 1]:
                temp_count += 1
        print("Case #" + str(int(count / 2)) + ":", temp_count)
    count += 1
    T -= 1
    
# Wrong Answer
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
            now_list = list(range(0, D + 1, num))
            now_list.reverse()
            for now_num in now_list:
                if now_num <= start_point:
                    start_point = now_num
                    break
        print("Case #"+str(F-T)+":", now_num)
    T -= 1
