textfile = open("input-day3.txt", "r")
forest = textfile.readlines()

""" index = 28
row = 1
maxindex = 32
x = 0

# part 1

for f in forest:
    if index <= 27:
        index += 3
        print(index)
        print(f[index])
        if f[index] == "#":
            x += 1
    elif index == 28:
        index = 0
        print(index)
        print(f[index])
        if f[index] == "#":
            x += 1
    elif index == 29:
        index = 1
        print(index)
        print(f[index])
        if f[index] == "#":
            x += 1
    elif index == 30:
        index = 2
        print(index)
        print(f[index])
        if f[index] == "#":
            x += 1

print(x)
 """
# part 2

a = 0 # right 1, down 1
b = 0 # right 3, down 1
c = 0 # right 5, down 1
d = 0 # right 7, down 1
e = 0 # right 1, down 2

# right 1, down 1
index = 30
for f in forest:
    if index <= 29:
        index += 1
        if f[index] == "#":
            a += 1
    elif index == 30:
        index = 0
        if f[index] == "#":
            a += 1

# right 3, down 1
index = 28
for f in forest:
    if index <= 27:
        index += 3
        if f[index] == "#":
            b += 1
    elif index == 28:
        index = 0
        if f[index] == "#":
            b += 1
    elif index == 29:
        index = 1
        if f[index] == "#":
            b += 1
    elif index == 30:
        index = 2
        if f[index] == "#":
            b += 1

# right 5, down 1
index = 26
for f in forest:
    if index <= 25:
        index += 5
        if f[index] == "#":
            c += 1
    elif index == 26:
        index = 0
        if f[index] == "#":
            c += 1
    elif index == 27:
        index = 1
        if f[index] == "#":
            c += 1
    elif index == 28:
        index = 2
        if f[index] == "#":
            c += 1
    elif index == 29:
        index = 3
        if f[index] == "#":
            c += 1
    elif index == 30:
        index = 4
        if f[index] == "#":
            c += 1

# right 7, down 1
index = 24
for f in forest:
    if index <= 23:
        index += 7
        if f[index] == "#":
            d += 1
    elif index == 24:
        index = 0
        if f[index] == "#":
            d += 1
    elif index == 25:
        index = 1
        if f[index] == "#":
            d += 1
    elif index == 26:
        index = 2
        if f[index] == "#":
            d += 1
    elif index == 27:
        index = 3
        if f[index] == "#":
            d += 1
    elif index == 28:
        index = 4
        if f[index] == "#":
            d += 1
    elif index == 29:
        index = 5
        if f[index] == "#":
            d += 1
    elif index == 30:
        index = 6
        if f[index] == "#":
            d += 1

# right 1, down 2 
index = 30
for f in forest[::2]:
    if index <= 29:
        index += 1
        if f[index] == "#":
            e += 1
    elif index == 30:
        index = 0
        if f[index] == "#":
            e += 1

print(a, b, c, d, e)
print(a * b * c * d * e)

# when going offscreen to the left, we can loop back to the right
# move three right and one down = listindex[+3] and next line/list
# if listindex goes out of range, loop back to one and continue as necessary
# end if out of lines
# if listindex == "#": counter + 1  
# maxindex = 32