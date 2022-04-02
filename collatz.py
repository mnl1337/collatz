import time
import csv
l = [0]

# the number range you want to calculate
numStart = 1
numEnd = 99999

# creates a csv file with a dynamic name
fileName = ''
fileName = fileName.join('collatz' + str(numStart) + '_' + str(numEnd) + '.csv')

# https://en.wikipedia.org/wiki/Collatz_conjecture
def collatz():    
    global number
    global steps
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
        number = number * 3 + 1
    steps = steps + 1
    print (number)

# calculate the steps to reach 1 for every number defined at the start
for number in range(numStart, numEnd, +1):
    print("Number: ",number)
    steps = 0    
    while number != 1:
        collatz()
    print("Steps: ", steps)

    # extends the list (if needed) and adds 1 were position=steps
    if len(l)<steps:
        for j in range(0, steps-len(l), +1):
            l.append(0)
    l[steps-1] = l[steps-1] + 1
    print()

# prints the list
for j in range(0, len(l), +1):
    print(j+1, ": ",l[j])

# saves the list in collatz.csv
with open(fileName, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(l)