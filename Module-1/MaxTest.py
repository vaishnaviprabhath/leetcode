def getMaxNumber(numbers):
    maxNumber = numbers[0]
    currentIndex = 0
    maxIndex = currentIndex
    for currentNumber in numbers:
        if currentNumber > maxNumber:
            maxNumber = currentNumber
            maxIndex = currentIndex
            currentIndex = currentIndex + 1
    return maxIndex
print(getMaxNumber([9876543211234567890,875465243235647588697,8585577556565656,87654454647,984765637456656656556]))