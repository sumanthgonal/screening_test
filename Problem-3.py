a = int(input("Enter a number: "))
limit = a if a % 2 != 0 else a - 1
result = [i for i in range(1, limit + 1, 2)]
print(result)
