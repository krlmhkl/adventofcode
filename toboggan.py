textfile = open("tobogganpasswords.txt", "r")
passwords = textfile.readlines()

# separate lines as list
# for each line, separate numbers, single letter, password, by index 0-3
# set first number as min, second number as max
# set letter as thing to check for at password
# if password is valid, +=1 to variable initially set at zero (counter)
#
# to split, a bit of a hacky solution
# text.replace() to change all spaces and non-text symbols into ","
# then split with the "," delimiter

x = 0
line = passwords[x]
minamount = passwords[line[0]]
maxamount = passwords[line[1]]
policy = passwords[line[2]]
password = passwords[line[3]]
