inputfile = open("input-day4.txt", "r")
#airportSecurity = inputfile.read().split("\n\n")
batches = [passports.split() for passports in inputfile.read().split("\n\n")]


for batch in batches:
    passport = dict([el.split(":") for el in batch])
#    print(passport)


x = list(passport.keys())
x.sort()
print(str(x)) #tee listiks


# if ["iyr" and "byr" and "eyr" and "hgt" and "hcl" and "ecl" and "pid"] in x: counter +=1
# if ["iyr" and "byr" and "eyr" and "hgt" and "hcl" and "ecl" and "pid" and "cid"] in x: counter +=1 

# sorteeri, tähestiku järjekorras



#passport = dict([el.split(":") for el in batches.split()])
#print(passport)


#valid_ecl = ["gry", "blu", "red"]

#if passport["ecl"] in valid_ecl:
#    print("sobib")