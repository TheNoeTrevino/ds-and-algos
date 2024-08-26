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

        self.head.data = data
        self.head.next = self.head

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, itr)

    def append_values(self, data_list):
        for data in data_list:
            self.append(data)

    def insert_after_value(self, data_after, data_to_insert):
        # TODO: raise exception here if value does not exist, else where also
        if self.head is None:
            self.head = Node(data_to_insert)

        itr = self.head
        while itr.next:
            # this is broken
            if itr.data == data_after:
                # itr.next = Node(data_to_insert, itr, itr.next)
                itr.next.data = data_to_insert
                itr.next.prev = itr
                itr.next.next = itr.next
                return

            itr = itr.next

    def print_forwards(self):
        llstr = ""
        itr = self.head
        if itr is None:
            print("Linked List is empty")
            return

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
            print("Linked List is empty")
            return

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
# ll.push(0)
ll.append_values([2, 1, 4, 32, 9])
# ll.insert_after_value(9, "HERE")
ll.print_forwards()
ll.print_backwards()
