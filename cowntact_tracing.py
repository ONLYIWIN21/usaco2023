import math

input()

blocks = []
curr_len = 0
for cow in input():
    if cow == "0":
        if curr_len > 0:
            blocks.append(curr_len)
        curr_len = 0
    else:
        curr_len += 1

if curr_len > 0:
    blocks.append(curr_len)

min_time = 99999
for block in blocks:
    block_time = block // 2 + (block % 2) - 1
    min_time = min(block_time, min_time)

#print("min time: " + str(min_time))
num_cows = 0
for block in blocks:
    cows = math.ceil(block / (min_time * 2 + 1))
    #print(cows)
    num_cows += cows

print(num_cows)
