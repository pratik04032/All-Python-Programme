# Diamond Number Pattern
rows = 9
# Upper part
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # Create leading spaces
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")  # Create leading spaces
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
