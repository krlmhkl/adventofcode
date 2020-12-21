f = open('input-day7.txt')
lines = f.readlines()

bags = set()


'''def count_colors(color):
    for l in lines:
        splitted = l.split("bags contain")
        if splitted[1].count(color):
            bags.add(splitted[0])
            count_colors(splitted[0]'''


def count_bags(color):
    bag_count = 0
    for l in lines:
        split_line = l.split(" bags contain ")
        if split_line[0] == color:
            contain_bags = split_line[1].split(", ")
            for_bc = 0
            for b in contain_bags:
                if not 'no other bags' in b:
                    words = b.split()
                    c = int(words[0])
                    new_color = words[1] + ' ' + words[2]
                    for_bc = c + c * count_bags(new_color)
                bag_count += for_bc
            return bag_count


count_bags("shiny gold")
count = count_bags("shiny gold")
# print(len(bags))
print(count)


# if "shiny gold" contains colors, check colors in colors,
# then check colors in colors until no more colors.
# also count how many bags in total
