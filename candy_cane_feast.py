input()

cows = [int(cow) for cow in input().split(" ")]
candy_canes = [int(candy_cane) for candy_cane in input().split(" ")]

indexes = [i for i in range(len(cows))]
for cane in candy_canes:
    for i in range(len(indexes) - 1, 0, -1):
        if cows[indexes[i]] <= cows[indexes[i] - 1]:
            indexes.remove(indexes[i]);

    cane_bot = 0
    for i in indexes:
        eaten = max(0, min(cows[i], cane) - cane_bot)
        cows[i] += eaten
        cane_bot += eaten

        if cane_bot >= cane:
            break

for cow in cows:
    print(cow)
