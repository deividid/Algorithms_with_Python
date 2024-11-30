def factorial(numb):
    if numb <= 1:
        return numb

    return numb * factorial(numb - 1)


number = int(input())
print(factorial(number))