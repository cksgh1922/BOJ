n = int(input())

for i in range(n):
    ps = input()
    is_valid = True
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                is_valid=False
                break
            stack.pop()
    if is_valid and not stack:
        print("YES")
    else:
        print("NO")