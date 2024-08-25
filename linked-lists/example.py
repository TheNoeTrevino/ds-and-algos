class Node:
    # elements in a linked list are linked via the node having the address to the next node. AKA: 'next'
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def push(self, data):

        # make a new node with the new data, and the current head as the pointer
        new_node = Node(data, self.head)
        # set the new node as the current head
        self.head = new_node

    def append(self, data):

        # if there is no head, we can make the "insert at end node" the head
        if self.head is None:
            self.head = Node(data, None)
            return

        # if the head is Null, insert! This is computationally expensive compared to a normal array, which does not have to traverse
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def append_values(self, data_list):

        for data in data_list:
            self.append(data)

    def insert(self, data, index):
        if index < 0:
            print("index cannot be a negative number")
        else:
            if self.head is None:
                self.head = Node(data, None)

            count = 0
            itr = self.head

            while itr:
                if count == index - 1:
                    itr.next = Node(data, itr.next)

                itr = itr.next
                count += 1

    def remove_at(self, index):
        if index < 0:
            print("index cannot be a negative number")
        else:
            count = 0
            itr = self.head

            while itr:
                if count == index - 1:
                    if itr.next:
                        itr.next = itr.next.next
                    else:
                        print(
                            "The index is greater than the length of the list. Nothing to remove."
                        )

                itr = itr.next
                count += 1

    def print(self):
        if self.head is None:
            print("Linked List is empty")

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data)

            itr = itr.next

            if itr is not None:
                llstr += "->"

        print(llstr)


# Init linked list
ll = LinkedList()

# add values
ll.append("first")
ll.append("second")
ll.append("third")
ll.append("fourth")
print("Initial Linked List:")
ll.print()


print("\nNew Linked List:")
ll.insert("NEW VALUE", 3)
ll.print()


print("\nNew Linked List:")
ll.remove_at(1)
ll.print()
