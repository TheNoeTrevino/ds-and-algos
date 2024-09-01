class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    # we are not checking for duplicates here, but you can!
    def add_child(self, child):
        # we add this so when we make a new node, the parent of that node is the object that is calling the function!
        # so, a way of linking them, like a linked list!!!
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0

        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        if self.get_level() == 1:
            prefix = "|__"
        else:
            prefix = (" " * self.get_level()) + "|__"

        # check if parent
        if self.parent:
            print(prefix + self.data)
        else:
            print(self.data)

        # check if
        if self.children:
            for child in self.children:
                child.print_tree()
                child.get_level()


def build_product_tree():
    root = TreeNode("Drum Corps")

    troopers = TreeNode("Troopers")
    vanguard = TreeNode("Santa Clara Vanguard")

    noe = TreeNode("Noe T.")
    molly = TreeNode("Molly H.")

    maddie = TreeNode("Maddie W.")
    micheal = TreeNode("Michael D.")

    marimba = TreeNode("Marimba")
    vibraphone = TreeNode("Vibraphone")

    root.add_child(troopers)
    root.add_child(vanguard)

    troopers.add_child(noe)
    troopers.add_child(molly)

    noe.add_child(marimba)
    molly.add_child(vibraphone)

    maddie.add_child(marimba)
    maddie.add_child(vibraphone)
    micheal.add_child(marimba)

    vanguard.add_child(maddie)
    vanguard.add_child(micheal)

    return root


tree = build_product_tree()
tree.print_tree()
