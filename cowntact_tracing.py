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

max_time = 99999999
for i in range(len(blocks)):
    block = blocks[i]
    block_time = block // 2 + (block % 2) - 1
    if i == 0 or i == len(blocks) - 1:
        block_time = block - 1
    max_time = min(block_time, max_time)

#print("blocks: " + str(blocks))
#print("max time: " + str(max_time))
num_cows = 0
for block in blocks:
    cows = math.ceil(block / (max_time * 2 + 1))
    #print(cows)
    num_cows += cows

print(num_cows)
