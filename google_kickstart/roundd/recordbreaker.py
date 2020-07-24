T = int(input())
F = T+1
while T > 0:
    N = int(input())
    line = input().split()
    line = list(map(int, line))
    the_largest = line[0]
    count = 0
    if N == 1 or N == 2:
        if N == 1:
            print("Case #" + str(F-T) + ":",1)
        elif N == 2 and line[0] != line[1]:
            print("Case #" + str(F-T) + ":",1)
        else:
            print("Case #" + str(F-T) + ":",0)
        T -= 1
        continue
    if line[0] > line[1]:
        count += 1
    for num in range(1, N - 1):
        if line[num] > line[num + 1] and line[num] > the_largest:
            the_largest = line[num]
            count += 1
    if line[-1] > the_largest:
        count += 1
    print("Case #" + str(F-T) + ":",count)
    T -= 1
