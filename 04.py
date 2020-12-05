import re

with open("input/04.txt") as f:
    data = [{l[0] : l[1] for l in [k.split(":") for k in j.split(" ")]} for j in [i.replace("\n", " ") for i in f.read().split("\n\n")]]

valid_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

yr_re = re.compile(r"^\d{4}$")
hgt_re = re.compile(r"^\d+(cm|in)$")
hcl_re = re.compile(r"^#[\da-f]{6}$")
ecl_re = re.compile(r"^amb|blu|brn|gry|grn|hzl|oth$")
pid_re = re.compile(r"^\d{9}$")

valid_count_1 = 0
valid_count_2 = 0

for passport in data:

    passport_fields = set(passport.keys())
    missing_fields = (valid_fields - passport_fields) - set(["cid"])
    if missing_fields:
        continue

    valid_count_1 += 1
    
    byr = int(yr_re.match(passport["byr"]).group())
    iyr = int(yr_re.match(passport["iyr"]).group())
    eyr = int(yr_re.match(passport["eyr"]).group())

    hgt = hgt_re.match(passport["hgt"])
    if hgt:
        hgt_value = int(hgt.group()[:-2])
        hgt_unit = hgt.group()[-2:]

    hcl = hcl_re.match(passport["hcl"])
    ecl = ecl_re.match(passport["ecl"])
    pid = pid_re.match(passport["pid"])

    if byr >= 1920 and byr <= 2002 and \
        iyr >= 2010 and iyr <= 2020 and \
        eyr >= 2020 and eyr <= 2030 and \
        hgt and (hgt_unit == "cm" and hgt_value >= 150 and hgt_value <= 193 or \
                hgt_unit == "in" and hgt_value >= 59 and hgt_value <= 76) and \
        hcl and ecl and pid:
        valid_count_2 += 1

print(f"Valid Passports: {valid_count_1}")
print(f"Valid Passports: {valid_count_2}")
