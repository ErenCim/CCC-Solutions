lines = int(input())
all_data = [[0] * 2 for x in range(lines)]
for i in range(lines):
    data = list(input().split())
    all_data[i][0] = int(data[0])
    all_data[i][1] = int(data[1])


sorted_list = sorted(all_data)
## print(sorted_list)
highest = 0
for e in range(lines-1):
    speed = (abs(sorted_list[e][1]-sorted_list[e+1][1]))/abs(sorted_list[e+1][0]-sorted_list[e][0])
    if speed > highest:
        highest = speed

print(highest)
