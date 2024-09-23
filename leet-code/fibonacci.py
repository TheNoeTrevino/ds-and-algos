def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


fib_list = []
num = int(input("Choose a number: "))

# print(fib(34))
print(fib(45))

for i in range(num):
    fib_list.append(fib(i))

print(fib_list)
