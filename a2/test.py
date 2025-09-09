import random

def createStart():
    while True:
        start = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        random.shuffle(start)
        tiles = [num for num in start if num !=0]
        count = 0

        length = len(tiles)
        for i in range(length):
            for j in range(i+1, length):
                if tiles[i] > tiles[j]:
                    count +=1

        if count % 2 == 0:
            print(count)
            return start

count = 0
for i in range(3):
    count += 1
    print(i)

print(count)