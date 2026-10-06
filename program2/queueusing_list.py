queue = []

def insert():
    value = int(input("Enter value: "))
    queue.append(value)
    print(value, "inserted")

def delete():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        value = queue.pop(0)
        print(value, "deleted")

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)


insert()
insert()
insert()

display()

delete()
display()