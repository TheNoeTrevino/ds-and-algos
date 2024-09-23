from collections import deque


def is_valid(s: str) -> bool:

    sym_dict = {")": "(", "]": "[", "}": "{"}
    stack = deque()

    for c in s:
        if c in sym_dict:
            if len(stack) == 0:
                return False
            elif stack.pop() == sym_dict[c]:
                continue
            else:
                return False
        else:
            stack.append(c)

    if len(stack) > 0:
        return False

    return "helo"


print(is_valid("([])"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("()"))
