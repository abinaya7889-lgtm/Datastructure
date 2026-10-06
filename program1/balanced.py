def balanced(exp):
    stack = []

    for ch in exp:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

exp = input("Enter expression: ")

if balanced(exp):
    print("Balanced")
else:
    print("Not Balanced")