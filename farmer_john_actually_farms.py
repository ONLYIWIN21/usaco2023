def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i][1] <= lst[i + 1][1]:
            return False
    return True

num_tests = int(input())

output = ""
for i in range(num_tests):
    input()

    heights = input().split()
    growths = input().split()
    placements = input().split()

    plants = []
    for i in range(len(heights)):
        plants.append([int(placements[i]), int(heights[i]), int(growths[i])])

    plants.sort(key=lambda plant: plant[0])

    min = -1
    for i in range(10000):
        if is_sorted(plants):
            min = i
            break
        for j in range(len(plants)):
            plants[j][1] += plants[j][2]

    output += str(min)

    output += "\n"

print(output)
