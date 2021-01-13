import re
import string


def is_hex(s):
    try:
        int(s, 16)
        print("jah")
    except ValueError:
        print("ei")


lines = open("input-day4.txt").read().split('\n\n')
passports = [dict(x.split(':') for x in line.split()) for line in lines]

c1 = 0
c2 = 0
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for passport in passports:
    # print(passport)
    if all(key in passport for key in (keys)):
        c1 += 1
        # print(c1)
        byr = passport.get("byr")
        iyr = passport.get("iyr")
        eyr = passport.get("eyr")
        hgt = passport.get("hgt")
        if "in" in hgt:
            hgtin = hgt[: -2]
        elif "cm" in hgt:
            hgtcm = hgt[: -2]
        hcl = passport.get("hcl")
        hclint = hcl[1:]
        ecl = passport.get("ecl")
        pid = passport.get("pid")
        if 1920 <= int(byr) >= 2002:
            if 2010 <= int(iyr) >= 2020:
                if 2020 <= int(eyr) >= 2030:
                    if (59 <= int(hgtin) >= 75) or (150 <= int(hgtcm) >= 193):
                        if is_hex(hclint) == True:
                            print("jee")

# if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth":'''
