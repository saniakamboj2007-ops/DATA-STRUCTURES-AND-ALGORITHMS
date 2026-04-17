
# Dynamic Array

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            print(f"Resizing from {self.capacity} to {self.capacity * 2}")
            self.resize()

        self.arr[self.size] = x
        self.size += 1

    def resize(self):
        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def pop(self):
        if self.size == 0:
            return "Array is empty"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def display(self):
        print(self.arr[:self.size], "Size:", self.size, "Capacity:", self.capacity)



# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



# Doubly Linked List

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, x):
        new_node = DNode(x)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = DNode(x)
                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return
            temp = temp.next
        print("Target not found")

    def delete_at_position(self, pos):
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for i in range(pos):
            temp = temp.next
            if temp is None:
                return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")



# Stack using SLL

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return "Stack Underflow"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return "Empty"
        return self.head.data


# Queue using SLL

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return "Queue Underflow"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return "Empty"
        return self.head.data


# Parentheses Checker

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.peek() == pairs[ch]:
                stack.pop()
            else:
                return False

    return stack.head is None



# MAIN TEST CASES

if __name__ == "__main__":

    print("\n--- Dynamic Array ---")
    da = DynamicArray()
    for i in range(10):
        da.append(i)
        da.display()

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    da.display()

    print("\n--- Singly Linked List ---")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(1)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    sll.traverse()
    sll.delete_by_value(3)
    sll.traverse()

    print("\n--- Doubly Linked List ---")
    dll = DoublyLinkedList()
    for i in range(1, 6):
        dll.insert_at_end(i)
    dll.traverse()
    dll.insert_after(3, 99)
    dll.traverse()
    dll.delete_at_position(1)
    dll.traverse()

    print("\n--- Stack ---")
    st = Stack()
    st.push(10)
    st.push(20)
    print("Peek:", st.peek())
    print("Pop:", st.pop())

    print("\n--- Queue ---")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Front:", q.front())
    print("Dequeue:", q.dequeue())

    print("\n--- Parentheses Checker ---")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", "Balanced" if is_balanced(t) else "Not Balanced")