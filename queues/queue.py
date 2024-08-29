from collections import deque
from threading import Thread
import time

# from threading import Thread
#
# t = Thread(target=print, args=[1])
#
# t.run()
# 1
#
# t = Thread(target=print, args=(1,))
#
# t.run()


class Queue:

    def __init__(self):
        self.container = deque()

    def get_size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0

    def enqueue(self, data):
        self.container.appendleft(data)

    def enqueue_orders(self, orders):
        for order in orders:
            self.container.appendleft(order)
            time.sleep(0.5)
            print(f"{order} has been ordered.")

    def dequeue(self):
        return self.container.pop()

    def dequeue_orders(self):
        while self.container:
            popped = self.dequeue()
            time.sleep(2.0)
            print(f"{popped} was served.")


orders = ["pizza", "samosa", "pasta", "biryani", "burger"]

queue = Queue()

print(queue.container)

order_thread = Thread(target=queue.enqueue_orders, args=(orders,))
serve_thread = Thread(target=queue.dequeue_orders, args=())

order_thread.start()
serve_thread.start()

order_thread.join()
serve_thread.join()

print("Time to go home.")

# For all exercises use Queue class implemented in main tutorial.
#
#     Design a food ordering system where your python program will run two threads,
#         Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#         Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
#
#     Use this video to get yourself familiar with multithreading in python
#
#     Pass following list as an argument to place order thread,
#
#     orders = ['pizza','samosa','pasta','biryani','burger']
#
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
