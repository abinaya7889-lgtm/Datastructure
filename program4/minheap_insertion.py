class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = \
                    self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def display(self):
        print("Min Heap:", self.heap)


h = MinHeap()

h.insert(40)
h.insert(20)
h.insert(30)
h.insert(10)
h.insert(50)

h.display()