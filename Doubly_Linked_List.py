from __future__ import annotations
from typing import Any

class Node(object):
    def __init__(self, data: Any, prev_node: Node = None, next_node: Node= None) -> None:
        self.data = data
        self.prev = prev_node
        self.next = next_node

class DoublyLinkedList(object):
    def __init__(self, head: Any = None) -> None:
        self.head = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
