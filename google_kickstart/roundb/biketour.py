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
    
# RunTime Error
T = int(input())
while T * 2 > 0:
    line = input().split()
    line = list(map(int, line))
    if (T * 2) % 2 == 1:
        N, D = line
    else:
        line = line.split()
        line = list(map(int, line))
        line.reverse()
        past_list = list(range(0, D + 1, line[0]))
        start_point = past_list[-1]
        if len(past_list) == 2:
            print("Case #" + str(int(count / 2)) + ":", start_point)
        else:
            for num in line[1:]:
                now_list = list(range(0, D + 1, num))
                now_list.reverse()
                for now_num in now_list:
                    if now_num <= start_point:
                        start_point = now_num
                        break
            print("Case #"+str(int(count/2))+":", now_num)
    T -= 0.5
