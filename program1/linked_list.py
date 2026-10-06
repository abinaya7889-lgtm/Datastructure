class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(value, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            value = self.top.data
            self.top = self.top.next
            print(value, "popped")

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        current = self.top

        print("Stack:", end=" ")

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.peek()
s.pop()
s.display()