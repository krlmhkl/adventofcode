textfile = open("tobogganpasswords.txt", "r")
lines = [l.strip() for l in textfile.readlines()]

x = 0
n = 0

# part 1

for el in lines:
    line = el.split()
    min, max = [int(el) for el in line[0].split("-")]
    char = line[1].strip(":")
    pw = line[2]
    if pw.count(char) <= max and pw.count(char) >= min:
        x += 1
        n += 1
        print(x)
    else:
        print(x)
        n += 1


# part 2
"""
for el in lines:
    line = el.split()
    min, max = [int(el) for el in line[0].split("-")]
    char = line[1].strip(":")
    pw = line[2]
    if char is pw[max - 1] and char is not pw[min - 1]:
        x += 1
        n += 1
        print(x)
    elif char is pw[min - 1] and char is not pw[max - 1]:
        x += 1
        n += 1
        print(x)
    else:
        print(x)
        n += 1
"""
