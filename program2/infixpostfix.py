def priority(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_postfix(exp):
    stack = []
    result = ""

    for ch in exp:
        if ch.isalnum():
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and priority(stack[-1]) >= priority(ch):
                result += stack.pop()
            stack.append(ch)

    while stack:
        result += stack.pop()

    return result

exp = input("Enter infix expression: ")
print("Postfix:", infix_postfix(exp))