def is_sorted(lst, key):
    for i in range(len(lst) - 1):
        if key(lst[i]) <= key(lst[i + 1]):
            return i
    return -1

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

    max = 100000000
    plants_sorted = is_sorted(plants, lambda plant: plant[2])
    if plants_sorted != -1:
        if plants[plants_sorted][2] == plants[plants_sorted + 1][2]:
            if plants[plants_sorted][1] <= plants[plants_sorted + 1][1]:
                max = 0
        else:
            max = (plants[plants_sorted][1] - plants[plants_sorted + 1][1]) // (plants[plants_sorted + 1][2] - plants[plants_sorted][2]) + 1

    min = -1
    i = 0
    while i < max:
        plants_sorted = is_sorted(plants, lambda plant: plant[1] + plant[2] * i)
        if plants_sorted == -1:
            min = i
            break
        new_i = (plants[plants_sorted][1] - plants[plants_sorted + 1][1]) // (plants[plants_sorted + 1][2] - plants[plants_sorted][2]) + 1
        if new_i <= i:
            break
        i = new_i

    output += str(min)

    output += "\n"

print(output[:-1])
