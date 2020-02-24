def getMinimumNumber(numbers):
    minNumber = numbers[0]
    for currentNumber in numbers:
        if currentNumber < minNumber:
            minNumber = currentNumber
    return minNumber

def getMinimumIndex(numbers):
    minNumber = numbers[0]
    currentIndex = 0
    minIndex = currentIndex
    for currentNumber in numbers:
        if currentNumber < minNumber:
            minNumber = currentNumber
            minIndex = currentIndex
        currentIndex = currentIndex+1
    return minIndex

def getMaximumIndex(numbers):
    maxNumber = numbers[0]
    currentIndex = 0
    maxIndex = currentIndex
    for currentNumber in numbers:
        if currentNumber > maxNumber:
            maxNumber = currentNumber
            maxIndex = currentIndex
        currentIndex = currentIndex+1
    return maxIndex


def getMaximumNumber(numbers):
    maxNumber = numbers[0]
    for currentNumber in numbers:
        if currentNumber > maxNumber:
            maxNumber = currentNumber
    return maxNumber

def test():
    testList = [[1,2,3,0,4,5,1] ,[11,-2,-3,0,-1,4,5,1]]
    for testItem in testList:
        assert(testItem[getMinimumIndex(testItem)] == getMinimumNumber(testItem))
        assert (testItem[getMaximumIndex(testItem)] == getMaximumNumber(testItem))
test()