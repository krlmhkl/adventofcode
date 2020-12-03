textfile = open("expenselist.txt", "r")
expenses = list(map(int, textfile.readlines()))

x = 0
y = 0
z = 0

while True:
    if z < 200:
        if expenses[x] + expenses[y] + expenses[z] == 2020:
            print(expenses[x], expenses[y], expenses[z])
        elif expenses[x] + expenses[y] + expenses[z] != 2020:
            z += 1
            print(x, y, z)
    if z == 200:
        print("zzzzz")
        z -= 200
        if y < 200:
            if expenses[x] + expenses[y] + expenses[z] == 2020:
                print(expenses[x], expenses[y], expenses[z])
            elif expenses[x] + expenses[y] + expenses[z] != 2020:
                y += 1
                print(x, y, z)
        if y == 200:
            print("yyyyy")
            y -= 200
            if x < 200:
                if expenses[x] + expenses[y] + expenses[z] == 2020:
                    print(expenses[x], expenses[y], expenses[z])
                elif expenses[x] + expenses[y] + expenses[z] != 2020:
                    x += 1
                    print(x, y, z)
