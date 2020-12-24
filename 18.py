from queue import deque

def evaluate(expr, add_prec):

    # Evalute parentheses
    i_curr = 0
    while i_curr < len(expr):
        part = expr[i_curr]

        if part == "(":
            i_par_end = i_curr
            par_stack = deque()
            par_stack.append(i_curr)

            i_par_start = None
            while par_stack:
                i_par_end += 1

                if expr[i_par_end] == "(":
                    par_stack.append(i_par_end)
                elif expr[i_par_end] == ")":
                    i_par_start = par_stack.pop()

            expr = expr[:i_par_start] + [evaluate(expr[i_par_start + 1:i_par_end], add_prec)] + expr[i_par_end + 1:]

        i_curr += 1

    # Evaluate left-right precedence
    if not add_prec:

        result = 0
        op_add = True
        
        i_curr = 0
        while i_curr < len(expr):
            part = expr[i_curr]
            
            if part == "+":
                op_add = True
            elif part == "*":
                op_add = False
            else:
                if op_add:
                    result += expr[i_curr]
                else:
                    result *= expr[i_curr]

            i_curr += 1
        
        return result

    # Evaluate addition precedence
    else:
        i_curr = 0
        while i_curr < len(expr):
            part = expr[i_curr]
            
            if part == "+":
                i_curr -= 1
                expr = expr[:i_curr] + [expr[i_curr] + expr[i_curr + 2]] + expr[i_curr + 3:]

            i_curr += 1

        i_curr = 0
        while i_curr < len(expr):
            part = expr[i_curr]
            
            if part == "*":
                i_curr -= 1
                expr = expr[:i_curr] + [expr[i_curr] * expr[i_curr + 2]] + expr[i_curr + 3:]

            i_curr += 1

        return expr[0]

with open("input/18.txt") as f:
    exprs = [[int(j) if j.isnumeric() else j for j in i.replace(" ", "")] for i in f.read().split("\n")]

total = 0
total_adv = 0
for expr in exprs:
    total += evaluate(expr, False)
    total_adv += evaluate(expr, True)

print(f"Total of all Expressions: {total}")
print(f"Total of all Expressions ADVANCED: {total_adv}")