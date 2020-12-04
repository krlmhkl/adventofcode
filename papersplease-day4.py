inputfile = open("input-day4.txt", "r")
airportSecurity = inputfile.read()

passport = dict([el.split(":") for el in airportSecurity.split()])
print(passport)





#valid_ecl = ["gry", "blu", "red"]

#if passport["ecl"] in valid_ecl:
#    print("sobib")