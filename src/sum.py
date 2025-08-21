def sum_pow(array, pow=1):
    total = 0
    for num in array:
        total += num ** pow
    return total

test_1 = [2, 2, 2]
print(sum_pow(test_1))
print(sum_pow(test_1, 2))
