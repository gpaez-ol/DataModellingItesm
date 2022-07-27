import math
from matplotlib import pyplot as plt

d = int(input("decimals?\n"))
tenToTheD = math.pow(10,d)
fileName = input("file name?\n")

def parseFloats(str):
    return round(float(str), d)

def roundToNextInt(val):
    return math.floor(val + 1)

def ceilReduceFloat(val):
    return math.ceil(val * tenToTheD) / tenToTheD


fileData = list(map(parseFloats,open(fileName, "r").read().splitlines()))

N = len(fileData)
print("N: {}".format(N))

maxValue = fileData[0]
minValue = fileData[0]

for i in range(1, N-1):
    if fileData[i] > maxValue:
        maxValue = fileData[i]
    if fileData[i] < minValue:
        minValue = fileData[i]

print("Max: {0:.{1}f}".format(maxValue,d))
print("Min: {0:.{1}f}".format(minValue,d))

C = roundToNextInt(1 + 3.3 * math.log(N, 10))
print("C: {}".format(C))

W = ceilReduceFloat((maxValue - minValue) / C)
print("W: {}".format(W))

bucketLimits = [minValue]
for i in range(1, C + 1):
    bucketLimits.append(bucketLimits[i-1] + W)

dataX = []
for i in range(0, C):
    dataX.append("[{0:.{1}f},{2:.{3}f})".format(bucketLimits[i],d,bucketLimits[i+1],d))

dataY = [0] * C
for i in range(0, N):
    index = 0
    for j in range(0, C):
        if fileData[i] < bucketLimits[j]:
            break
        index = j
    dataY[index] += 1

print("{:<15}\t{}".format("Intervals","f"))
for i in range(0, C):
    print("{}\t{}".format("{:<15}".format(dataX[i]),dataY[i]))

sum = 0
for i in range(0,C):
    sum += dataY[i]

print("Sum of frequencies: {}".format(sum))

plt.bar(dataX,dataY)
plt.show()