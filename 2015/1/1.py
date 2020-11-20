f = open("input.txt", "r")
line = f.readline()

for x in line:
    print(line.count("("))
