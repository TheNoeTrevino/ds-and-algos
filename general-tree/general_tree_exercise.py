class TreeNode:
    def __init__(self, employee_information):
        self.employee_information = employee_information
        self.children = []
        self.parent = None

    def add_child(self, employee):
        employee.parent = self
        self.children.append(employee)

    def get_level(self):
        level = 0

        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, choice):
        # look up how to do a dictionray comprehention
        # also use .join(', ' + the comprehention
        #
        selection = "ABOVE"

        if self.get_level() > 0:
            print(("  " * self.get_level()) + "|__" + selection)
        else:
            print(self.employee_information[choice])

        for child in self.children:
            child.print_tree(choice)


scuzzy = {"position": "senior dev", "name": "scuzzy"}
drew = {"position": "manager", "name": "drew"}
noe = {"position": "intern", "name": "noe"}
connor = {"position": "intern", "name": "connor"}
taylor = {"position": "designer", "name": "taylor"}
nathalie = {"position": "intern", "name": "nathalie"}
david = {"position": "vice president", "name": "david"}

david = TreeNode(david)
scuzzy = TreeNode(scuzzy)
drew = TreeNode(drew)
noe = TreeNode(noe)
connor = TreeNode(connor)
taylor = TreeNode(taylor)
nathalie = TreeNode(nathalie)

david.add_child(scuzzy)
david.add_child(taylor)
scuzzy.add_child(drew)
drew.add_child(noe)
drew.add_child(connor)
taylor.add_child(nathalie)

root = david

root.print_tree(["position"])
