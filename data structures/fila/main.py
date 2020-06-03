from node import Node
from typing import Any

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self._size = 0

    def _getnode(self, index: int) -> Node:
        pointer = self.first
        for _ in range(index):
            if (pointer):
                pointer = pointer.next
            else:
                raise IndexError('queue index out of range')
        return pointer

    def push(self, data: Any) -> None:
        new_node = Node(data)
        if (self.last is None):
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        if (self.first is None):
            self.first = self.last
        self._size += 1

    def pop(self) -> Any:
        if (self.first is not None):
            previous = self.first.data
            self.first = self.first.next
            self._size -= 1
            return previous
        raise IndexError('The queue is empty')

    def peek(self) -> Any:
        if (self.first is not None):
            return self.first
        raise IndexError('The queue is empty')

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> None:
        pointer = self._getnode(index)
        if (pointer):
            return pointer
        else:
            raise IndexError('queue index out of range')

    def __setitem__(self, index: int, data: Any) -> None:
        pointer = self._getnode(index)
        if (pointer):
            pointer.data = data
            return
        raise IndexError('queue index out of range')

    def __repr__(self) -> str:
        output = ''
        pointer = self.first
        while (pointer):
            output += '{} -> '.format(pointer)
            pointer = pointer.next
        return output

    def __str__(self) -> str:
        return self.__repr__()