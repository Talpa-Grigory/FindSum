def sum_pow(array, pow=False):
    total = 0
    for num in array:
        if pow:
            total += num ** pow
        else:
            total += num
    return total

test_1 = [2, 2, 2]
print(sum_pow(test_1))
print(sum_pow(test_1, 2))
