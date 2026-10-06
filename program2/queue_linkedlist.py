class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(value, "inserted")

    def delete(self):
        if self.front is None:
            print("Queue Underflow")
            return

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(value, "deleted")

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        current = self.front

        print("Queue:", end=" ")

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)

q.display()

q.delete()

q.display()