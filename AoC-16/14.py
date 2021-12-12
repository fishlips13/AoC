from hashlib import md5
import re

with open("input\\14.txt") as f:
    salt = f.read()

pattern_3 = r"([a-z0-9])?\1\1"

def rehash(start:str, count):
    hash_new = start
    for _ in range(count):
        hash_new = md5(hash_new.encode()).hexdigest()
    return hash_new

def gen_keys_64(hash_reps):
    i = 0
    otp_count = 0
    hash_cache = {}
    while True:
        salt_and_i = f"{salt}{str(i)}"
        if salt_and_i in hash_cache:
            otp_hash_3 = hash_cache[salt_and_i]
        else:
            otp_hash_3 = rehash(salt_and_i, hash_reps)
            hash_cache[salt_and_i] = otp_hash_3

        hits_3 = re.findall(pattern_3, otp_hash_3)
        if hits_3:

            for j in range(i + 1, i + 1001):
                salt_and_j = f"{salt}{str(j)}"
                if salt_and_j in hash_cache:
                    otp_hash_5 = hash_cache[salt_and_j]
                else:
                    otp_hash_5 = rehash(salt_and_j, hash_reps)
                    hash_cache[salt_and_j] = otp_hash_5

                hits_5 = re.findall(hits_3[0] * 5, otp_hash_5)
                if hits_5:
                    otp_count += 1
                    break

        if otp_count == 64:
            print(i)
            return i

        i += 1
        
print(f"64th index: {gen_keys_64(1)}")
print(f"64th index: {gen_keys_64(2017)}")