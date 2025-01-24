import time
import random
from random import randrange

NUM_ROWS = 9

def checkDupes(x):
    if len(x) == 0: 
        return True
    
    n = max(set(x), key=x.count)
    m = not x.count(n) > 1
    #print("Array Valid? ", m)
    return m

def reduceArray(x):
    res = []
    for i in x:
        if i != ".":
            res.append(i)
    #print("Reduced Array: ", res)
    return res

def checkRows(x):
    for i in x:
        #print(reduceArray(i))
        #print(checkDupes(reduceArray(i)))
        if not checkDupes(reduceArray(i)):
            return False
        else:
            continue
    return True

def checkColumns(x):
    #print(x)
    for i in range(0,NUM_ROWS):
        res = []
        for j in x:
            res.append(j[i])

        #print(res)

        if not checkDupes(reduceArray(res)):
            return False
        else:
            continue
    return True


def checkSubboxes(input):
    cornersX = [0,0,0,3,3,3,6,6,6]
    cornersY = [0,3,6,0,3,6,0,3,6]

    #for each 3x3 subbox 
    for i in range(0,NUM_ROWS):
        res = []
        x=cornersX[i]
        y=cornersY[i]

        res.append(input[x][y])
        res.append(input[x+1][y])
        res.append(input[x+2][y])
        res.append(input[x][y+1])
        res.append(input[x][y+2])
        res.append(input[x+1][y+1])
        res.append(input[x+2][y+2])
        res.append(input[x+2][y+1])
        res.append(input[x+1][y+2])

        #print(res)
        
        if not checkDupes(reduceArray(res)):
            return False
        else:
            continue
    return True

def validateBoard(x):
    for i in x:
        print(i)

    if ((checkRows(x)) and (checkColumns(x)) and (checkSubboxes(x))):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False

def randomTester():
    res = []
    for i in range(0,81):
        if randrange(10) > 1:
            res.append(".")
        else:
            res.append(str(randrange(10)))

    return [res[i:i+9] for i in range(0, len(res), 9)]

# Defining main function
def main():
    xx = 0
    while (not validateBoard(randomTester())):
        print('------------------------------')
        xx+=1
        time.sleep(1)
    print("Board found after ", xx, " attempts.")

# Using the special variable 
# __name__
if __name__=="__main__":
    start = time.time()
    main()
    end = time.time()
    print("----------------------------")
    print("Time Elapsed: ", (end - start)*1000, " milliseconds.")
    print((end - start),"seconds.")
    print("----------------------------")

# Function()
# if index in list is empty,
#    check (x + 1) and (x - 1)
#    if current num can fit between, return fine
#    if current num cannot fit between, return lose
#    if (x + 1) and (x - 1) is blank,
#        call Function()