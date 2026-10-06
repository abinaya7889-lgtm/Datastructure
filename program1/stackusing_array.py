stack = []
MAX = 5

def push():
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        value = int(input("Enter value: "))
        stack.append(value)
        print(value, "pushed into stack")

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("Popped:", stack.pop())

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

while True:
    print("\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        print("Stack:", stack)
    elif choice == 5:
        break
    else:
        print("Invalid choice")