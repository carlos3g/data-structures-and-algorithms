from node import Node
from typing import Any

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def _getnode(self, index: int) -> Node:
        pointer = self.head
        for _ in range(index):
            if (pointer):
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        return pointer

    def append(self, data: Any) -> None:
        if (self.head):
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(data)
        else:
            self.head = Node(data)
        self._size += 1

    def insert(self, index: int, data: Any) -> None:
        new_node = Node(data)
        if (index == 0):
            new_node.next = self.head
            self.head = new_node
        else:
            pointer = self._getnode(index-1)
            new_node.next = pointer.next
            pointer.next = new_node
        self._size -= 1

    def pop(self, index: int) -> None:
        if (self.head == None):
            raise IndexError('pop from empty list')
        elif (index == 0):
            self.head = self.head.next
        else:
            pointer = self.head
            previous = pointer.next
            for _ in range(index):
                previous = pointer
                pointer = pointer.next
            previous.next = pointer.next
            pointer.next = None
        self._size -= 1

    def index(self, data: Any) -> int:
        pointer = self.head
        i = 0
        while (pointer):
            if (str(pointer) == str(data)):
                return i
            pointer = pointer.next
            i += 1
        raise ValueError('{} is not in list'.format(data))

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> [Node, None]:
        pointer = self._getnode(index)
        if (pointer):
            return pointer
        raise IndexError('list index out of range')

    def __setitem__(self, index: int, data: Any) -> None:
        pointer = self._getnode(index)
        if (pointer):
            pointer.data = data
            return
        raise IndexError('list index out of range')

    def __repr__(self) -> str:
        output = ''
        pointer = self.head
        while (pointer):
            output += '{} -> '.format(pointer)
            pointer = pointer.next
        return output

    def __str__(self) -> str:
        return self.__repr__()
