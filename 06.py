with (open("input/06.txt")) as f:
    groups = [i.split("\n") for i in f.read().split("\n\n")]

any_total_counts = 0
all_total_counts = 0

for group in groups:

    any_answers = set()
    all_answers = set([i for i in group[0]])

    for person in group:
        any_answers = any_answers | set([i for i in person])
        all_answers = all_answers & set([i for i in person])
        pass
    
    any_total_counts += len(any_answers)
    all_total_counts += len(all_answers)

print(f"Any Count Total: {any_total_counts}")
print(f"All Count Total: {all_total_counts}")