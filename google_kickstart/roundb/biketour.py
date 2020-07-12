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
