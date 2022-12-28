def calculating_math_func(data, fact={}):
    if data in fact:
        result = fact[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
            fact[index] = result
    result /= data ** 3
    result = result ** 10
    print(fact)
    return result


print(calculating_math_func(6))
print(calculating_math_func(5))
