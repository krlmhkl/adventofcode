textfile = open("expenselist.txt", "r")
expenses = list(map(int, textfile.readlines()))

x = 0
y = 0


while True:
    if y < 200:
        if expenses[x] + expenses[y] == 2020:
            print(expenses[x], expenses[y])
            break
        elif expenses[x] + expenses[y] != 2020:
            y += 1
            print(x, y)
    if y == 200:
        print("yyyyy")
        y -= 200
        if x < 200:
            if expenses[x] + expenses[y] == 2020:
                print(expenses[x], expenses[y])
            elif expenses[x] + expenses[y] != 2020:
                x += 1
                print(x, y)
