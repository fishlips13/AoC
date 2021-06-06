from collections import deque
import re

def new_molecules_count(original, rep_dict):
    new_molecules = set()
    for mole_to_find, moles_rep in rep_dict.items():
        for i, mole_to_rep in enumerate(original):
            if mole_to_rep != mole_to_find:
                continue
            for mole_new in moles_rep:
                new_molecules.add("".join(original[:i] + mole_new + original[i+1:]))
    return len(new_molecules)
    
def replacement_count(molecule, rep_dict):
    count = 0
    while len(molecule) > 1:

        seg_len = 2
        while seg_len <= min(len(molecule), 8):

            i = 0
            while i + seg_len <= len(molecule):
                seg_str = "".join(molecule[i:i+seg_len])
                if seg_str in rep_dict:
                    molecule = molecule[:i] + [rep_dict[seg_str]] + molecule[i+seg_len:]
                    count += 1
                    i += seg_len
                else:
                    i += 1

            seg_len += 1

    return count

with open("input/19.txt") as f:
    data = f.read().split("\n\n")

mole_re = r"[A-Z][a-z]?"    

medicine = [i for i in re.findall(mole_re, data[1]) if i]
replacements = [i.split(" => ") for i in data[0].split("\n")]

rep_dict_expand = {}
rep_dict_contract = {}

for rep_old, rep_new in replacements:
    if rep_old not in rep_dict_expand:
        rep_dict_expand[rep_old] = []
    rep_dict_expand[rep_old].append(re.findall(mole_re, rep_new))
    rep_dict_contract[rep_new] = rep_old

print(f"Distinct Molecule Count: {new_molecules_count(medicine, rep_dict_expand)}")
print(f"Replacements Minimum: {replacement_count(medicine, rep_dict_contract)}")