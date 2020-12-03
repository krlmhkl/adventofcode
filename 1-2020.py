textfile = open("input1-2020.txt", "r")
expenses = list(map(int, textfile.readlines()))

x = 0
y = 0
z = 0

while True:
    if x < 200:
        if expenses[x] + expenses[y] + expenses[z] == 2020:
            print(expenses[x], expenses[y], expenses[z])
        elif y < 200:
            if expenses[x] + expenses[y] + expenses[z] == 2020:
                print(expenses[x], expenses[y], expenses[z])
            elif z < 200:
                if expenses[x] + expenses[y] + expenses[z] == 2020:
                    print(expenses[x], expenses[y], expenses[z])
                elif expenses[x] + expenses[y] + expenses[z] != 2020:
                    z += 1
                    print(x, y, z)
            elif z == 200:
                z -= 200
                y += 1
                print(x, y, z)
                if expenses[x] + expenses[y] + expenses[z] == 2020:
                    print(expenses[x], expenses[y], expenses[z])
                elif expenses[x] + expenses[y] + expenses[z] != 2020:
                    z += 1
        elif y == 200 and z == 0:
            z -= 200
            y -= 200
            x += 1
            print(x, y, z)
            if expenses[x] + expenses[y] + expenses[z] == 2020:
                print(expenses[x], expenses[y], expenses[z])
            elif expenses[x] + expenses[y] + expenses[z] != 2020:
                y += 1
        elif y == 200:
            y -= 200
            x += 1
            print(x, y, z)
            if expenses[x] + expenses[y] + expenses[z] == 2020:
                print(expenses[x], expenses[y], expenses[z])
            elif expenses[x] + expenses[y] + expenses[z] != 2020:
                y += 1
    elif x == 200:
        print("midad mäda")
