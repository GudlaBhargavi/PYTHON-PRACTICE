string = "HELLO"
stack = []

for char in string:
    stack.append(char)

reversed_string = ""

while stack:
    reversed_string += stack.pop()

print(reversed_string)