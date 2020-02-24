a = [5,10,100,500,5000000000000,517245467890000000000]
def getMaxList(numbers):
    maxNumber = numbers[0]
    for i in numbers:
        if i > maxNumber:
            maxNumber = i
    return maxNumber
print(getMaxList(a))