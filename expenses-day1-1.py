textfile = open("expenselist.txt", "r")
expenses = list(map(int, textfile.readlines()))

x = 0
y = 0

while True:
    if expenses[x] + expenses[y] == 2020:
        print(expenses[x], expenses[y])
        break
    elif y < 200 and expenses[x] + expenses[y] != 2020:
        y += 1
        print(x, y)
    if y == 200:
        y -= 200
        if x < 200 and expenses[x] + expenses[y] != 2020:
            x += 1
            print(x, y)
        