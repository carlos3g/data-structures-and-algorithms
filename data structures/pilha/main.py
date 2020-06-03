from typing import Any

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, data: Any) -> None:
        self.stack.append(data)

    def pop(self) -> [None, Any]:
        if (self.stack):
            return self.stack.pop()
        return None

    def peek(self) -> [None, Any]:
        if (self.stack):
            return self.stack[-1]
        return None

    def __repr__(self) -> list:
        return '{}'.format(self.stack)

    def __str__(self) -> str:
        return self.__repr__()