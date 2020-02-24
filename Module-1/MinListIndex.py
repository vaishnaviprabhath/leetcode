def getMinNumberIndex(numbers):
    minNumber = numbers[0]         # tracks minimum number
    currentIndex = 0               # tracks currentIndex
    minIndex = currentIndex        # tracks minIndex
    for currentNumber in numbers:              # i = current number
        if currentNumber < minNumber:
            minNumber = currentNumber
            minIndex= currentIndex
        currentIndex = currentIndex+1
    return minIndex
a = [1,2,87,5,564,0]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(getMinNumberIndex(a))

print(a[getMinNumberIndex(a)])