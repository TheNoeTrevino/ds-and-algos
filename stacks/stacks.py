from collections import deque

# def append(self, x: _T, /) -> None: ...
# def appendleft(self, x: _T, /) -> None: ...
# def copy(self) -> Self: ...
# def count(self, x: _T, /) -> int: ...
# def extend(self, iterable: Iterable[_T], /) -> None: ...
# def extendleft(self, iterable: Iterable[_T], /) -> None: ...
# def insert(self, i: int, x: _T, /) -> None: ...
# def index(self, x: _T, start: int = 0, stop: int = ..., /) -> int: ...
# def pop(self) -> _T: ...  # type: ignore[override]
# def popleft(self) -> _T: ...
# def remove(self, value: _T, /) -> None: ...
# def rotate(self, n: int = 1, /) -> None: ...


def backwards(string):
    stack = deque()

    bw_str = ""

    for c in string:
        stack.append(c)

    while stack:
        bw_str += stack.pop()
    print(bw_str)


def is_balanced(string):

    stack = deque()

    complements = {"}": "{", "]": "[", ")": "("}

    for c in string:
        if c == "{" or c == "(" or c == "[":
            stack.append(c)
        elif c == "}" or c == ")" or c == "]":

            if len(stack) == 0:
                print("False")
                return False

            elif stack.pop() == complements[c]:
                pass

        # if not a character of concern
        else:
            pass

    if len(stack) == 0:
        print("True")
        return True
    else:
        print("SOMETHING IS WEIRD")  # did not go off B-)


backwards("hello123{}]")
print("({a+b}): ")
is_balanced("({a+b})")  #    --> True
print("))((a+b}{: ")
is_balanced("))((a+b}{")  #  --> False
print("((a+b)): ")
is_balanced("((a+b))")  #    --> True
print(")): ")
is_balanced("))")  #         --> False
print("[a+b]*(x+2y)*{gg+kk}: ")
is_balanced("[a+b]*(x+2y)*{gg+kk}")  # --> True
