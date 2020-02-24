def getProductOfDigits(number):
    finalProduct = 1
    while number>0:
        currentDigit = number % 10
        number = number//10
        finalProduct = finalProduct*currentDigit
    return finalProduct
print(getProductOfDigits(1234))
