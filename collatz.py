import time
import csv
l = [0]

def collatz():    
    global number
    global counter
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
        number = number * 3 + 1
    counter = counter + 1
    print (number)

for number in range(10000, 99999, +1):
    print("Number: ",number)
    counter = 0    
    #print("Type in a number:" )
    #number = int(input())
    while number != 1:
        collatz()
    print("Steps: ", counter)
    if len(l)<counter:
        for j in range(0, counter-len(l), +1):
            l.append(0)
    l[counter-1] = l[counter-1] + 1
    print()
print(len(l))
for j in range(0, len(l), +1):
    print(j+1, ": ",l[j])
with open('collatz.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(l)