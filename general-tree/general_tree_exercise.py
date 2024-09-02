class TreeNode:
    def __init__(self, employee_information: dict):
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
        # dictionary comprehension was overkill
        # attributes = {k: v for k, v in self.employee_information.items() if k in choice}
        # attributes = " (".join(attributes.values()) + ")"

        attr_str = ""
        if "name" in choice:
            attr_str += str(self.employee_information.get("name"))
            if "position" in choice:
                attr_str += " (" + str(self.employee_information.get("position")) + ")"
        elif "position" in choice:
            attr_str += str(self.employee_information.get("position"))

        if self.get_level() > 0:
            # join()
            print(("  " * self.get_level()) + "|__" + attr_str)
        else:
            print(attr_str)

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
root.print_tree(["name"])
root.print_tree(["name", "position"])
