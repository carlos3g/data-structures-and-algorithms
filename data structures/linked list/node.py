from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return str(self.data)

    def __str__(self) -> str:
        return self.__repr__()