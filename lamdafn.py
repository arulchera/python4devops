data = [10, 20, 30, 40, 50]
result = sum(map(lambda x: x * 2, filter(lambda x: x % 4 == 0, data)))
print(result)