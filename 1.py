f = open("input.txt", "r")
line = f.readline()
print(line.count("(") - line.count(")"))

floor = 0

step = 0

for c in line:
    step += 1
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

    if floor == -1:
        print(step)

print(floor)
