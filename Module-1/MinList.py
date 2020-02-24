a = [1,2,3,4,5]
def getMinList(numbers):
    minNumber = numbers[0]
    for i in numbers:
        if i < minNumber:
            minNumber = i
    return minNumber
print(getMinList(a))
print(getMinList([9,3,8,9]))