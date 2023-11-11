import time
count = 0




start = time.time()

import time
count = 0

with open("text.txt", "r") as file:
    for line in file:
        for char in line:
            if char == "1":
                count +=1

with open('text.txt', 'r') as file:
    lines = file.readlines()
    res = lines[13].split(" ")


count = 0
with open('text.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split(" ")
        for n in numbers:
            count = count + int(n)

print(count) 