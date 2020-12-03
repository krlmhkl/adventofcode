textfile = open("expenselist.txt", "r")
expenses = list(map(int, textfile.readlines()))

x = 0
y = 0
z = 0

while True:
    if expenses[x] + expenses[y] + expenses[z] == 2020:
        print(expenses[x], expenses[y], expenses[z])
        break
    elif z < 200 and expenses[x] + expenses[y] + expenses[z] != 2020:
        z += 1
        print(x, y, z)
    if z == 200:
        z -= 200
        if y < 200 and expenses[x] + expenses[y] + expenses[z] != 2020:
            y += 1
            print(x, y, z)
        if y == 200:
            y -= 200
            if x < 200 and expenses[x] + expenses[y] + expenses[z] != 2020:
                x += 1
                print(x, y, z)