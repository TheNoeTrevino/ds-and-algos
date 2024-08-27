class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        new_node = Node(data, None, self.head)
        self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, itr, None)

    def append_values(self, data_list):
        for data in data_list:
            self.append(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("This linked list is empty")

        itr = self.head
        while itr:
            if itr.data == data_after:
                new_node = Node(data_to_insert, itr, itr.next)

                if itr.next:
                    itr.next.prev = new_node

                itr.next = new_node
                break

            itr = itr.next

    def delte_value(self, data_to_delete):
        if self.head is None:
            raise Exception("This linked list is empty")

        itr = self.head
        while itr.next:
            if itr.next.data == data_to_delete:
                itr.next = itr.next.next
                itr.next.prev = itr

            itr = itr.next

    def print_forwards(self):
        llstr = ""
        itr = self.head
        if itr is None:
            raise Exception(
                "Linked List is empty, consider using push to make a new Linked List"
            )

        while itr:
            llstr += str(itr.data)

            if itr.next is not None:
                llstr += "-->"

            itr = itr.next

        print(llstr)

    def print_backwards(self):
        itr = self.head
        llstr = ""

        if itr is None:
            raise Exception(
                "Linked List is empty, consider using push to make a new Linked List"
            )

        # just traverse
        while itr.next:
            itr = itr.next

        # traverse backwards
        while itr:
            llstr += str(itr.data)

            if itr.prev is not None:
                llstr += "<--"

            itr = itr.prev

        print(llstr)


ll = DoublyLinkedList()
ll.append(1)
ll.append(2)
ll.append_values([4, 5])
ll.insert_after_value(2, 3)
ll.push(0)
print("before delete: ")
ll.print_forwards()
ll.print_backwards()
ll.delte_value(3)
print("after delete: ")
ll.print_forwards()
ll.print_backwards()
