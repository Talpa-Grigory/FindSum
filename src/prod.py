def prod(array, pow=1):
    total = 1
    for num in array:
        total *= num ** pow
    return total

test_1 = [2, 2, 2]
print(prod(test_1))
print(prod(test_1, 2))
