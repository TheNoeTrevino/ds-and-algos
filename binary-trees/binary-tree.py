class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            pass

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def in_order_traversal(self):
        elements = []
        # visit the left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit the root
        elements.append(self.data)

        # visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        # visit the left tree
        if self.left:
            elements += self.left.post_order_traversal()

        # visit the right tree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit the root
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []

        # visit the root
        elements.append(self.data)

        # visit the left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit the right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def search(self, value):
        if value == self.data:
            return True

        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_max()
        else:
            return self.data

    def calculate_sum(self):
        sum = 0

        for i in self.in_order_traversal():
            sum += i
        return sum

    def delete(self, value):
        # less than, traverse
        if value < self.data:
            if self.left:
                # this is the most important part. We are updating the pointer here
                # this will eventually evaulate the else statement
                self.left = self.left.delete(value)
            else:
                raise Exception("Value not in tree")

        # greater than, traverse
        elif value > self.data:
            if self.right:
                # this is the most important part. We are updating the pointer here
                # this will eventually evaulate the else statement
                self.right = self.right.delete(value)
            else:
                raise Exception("Value not in tree")

        # equal to, which means we found it, no traversal. Delete
        else:
            # no children
            if self.left is None and self.right is None:
                return None
            # only right child
            if self.left is None:
                return self.right
            # only left child
            if self.right is None:
                return self.left

            # exercise
            max_val = self.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
            # two children
            # min_val = self.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

        return self


def build_tree(values):
    root = BinaryTreeNode(values[0])

    for v in values[1:]:
        root.add_child(v)
    return root


list = [17, 1, 5, 9, 12, 20, 22, 32, 23, 22, 22]

tree = build_tree(list)

print(tree.find_max())
print(tree.find_min())
print(tree.calculate_sum())
print(tree.search(9))
print(tree.search(19))
print(tree.in_order_traversal())
print(tree.post_order_traversal())
print(tree.pre_order_traversal())
tree.delete(2)
print(tree.pre_order_traversal())
