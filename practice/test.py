from typing import Union


def do_something(glorg: list[Union[int, str]]):
    for i in glorg:
        print(i)


do_something([1, 2, 3, 4, "hello"])
