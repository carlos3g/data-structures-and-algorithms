from node import Node
from typing import Any

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self._size = 0

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
            pointer = self.head
            for _ in range(index-1):
                if (pointer):
                    pointer = pointer.next
                else:
                    raise IndexError('list index out of range')
            new_node.next = pointer.next
            pointer.next = new_node
        self._size -= 1

    def pop(self, index: int) -> Node:
        if (index == 0):
            self.head = self.head.next
        else:
            pointer = self.head
            for _ in range(index-1):
                if (pointer):
                    pointer = pointer.next
                else:
                    raise IndexError('list index out of range')
            if (pointer):
                pointer.next = pointer.next.next
        self._size -= 1

    def index(self, data: Any) -> int:
        pointer = self.head
        i = 0
        while (pointer):
            if (pointer == data):
                return i
            pointer = pointer.next
            i += 1
        raise ValueError('{} is not in list'.format(data))

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> [Node, None]:
        pointer = self.head
        for _ in range(index):
            if (pointer):
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        if (pointer):
            return pointer
        raise IndexError('list index out of range')

    def __setitem__(self, index, data) -> None:
        pointer = self.head
        for _ in range(index):
            if (pointer):
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        if (pointer):
            pointer.data = data
        raise IndexError('list index out of range')

    # def __repr__(self) -> str:
    #     pass

    # def __str__(self) -> str:
    #     return self.__repr__()
