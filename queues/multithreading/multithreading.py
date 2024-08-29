import time
import threading


def calc_square(numbers: list[int]):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print("square:", n * n)


def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(1)
        print("cube:", n * n * n)


arr = [2, 3, 8, 9]

t = time.time()

t1 = threading.Thread(
    target=calc_square, args=(arr,)
)  # comma is used to make the tuple
t2 = threading.Thread(target=calc_cube, args=(arr,))

# calc_square(arr)
# calc_cube(arr)

print(
    """
------------- Backwards --------------

                 """
)
time1 = time.time()

print("thread one has started!")
t1.start()  # thread one

time2 = time.time() - time1
print(f"thread two has started {time2} after thread one")
t2.start()  # thread two

########## THREAD 0 just keeps going ############

# Basically says: Hey! wait for these other guys!
t1.join()
t2.join()

then


print("done in : ", time.time() - t)
print("Hah... I am done with all my work now!")
