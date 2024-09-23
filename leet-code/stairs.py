# https://www.youtube.com/watch?v=Y0lT9Fck7qI&ab_channel=NeetCode
def climb_stairs(n):
    if n <= 1:
        return n
    one, two = 1, 1
    for i in range(n - 1):
        one, two = one + two, one
    return one


print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(5))
print(climb_stairs(10))
print(climb_stairs(20))
print(climb_stairs(990))
