from itertools import cycle, permutations

def practice_game(p1_pos, p2_pos):
    p1_score = 0
    p2_score = 0

    dice = iter(cycle(range(1, 101)))
    p1_winner = None
    roll_count = 0

    while True:
        p1_pos = (p1_pos + next(dice) + next(dice) + next(dice)) % 10
        p1_score += p1_pos + 1
        roll_count += 3

        if p1_score >= 1000:
            p1_winner = True
            break

        p2_pos = (p2_pos + next(dice) + next(dice) + next(dice)) % 10
        p2_score += p2_pos + 1
        roll_count += 3

        if p2_score >= 1000:
            p1_winner = False
            break
        
    return (p2_score if p1_winner else p1_score) * roll_count

def main_game(p1_pos, p2_pos, p1_score, p2_score, turn, turn_scores, cache):
    state = f"{p1_pos}-{p2_pos}-{p1_score}-{p2_score}-{turn}"
    if state in cache:
        return cache[state]

    p1_future_wins, p2_future_wins = 0, 0

    for turn_score in turn_scores:
        if turn % 2 == 0:
            p1_pos_new = (p1_pos + turn_score) % 10
            p1_score_new = p1_score + p1_pos_new + 1

            if p1_score_new >= 21:
                p1_future_wins += 1
                continue

            future_wins = main_game(p1_pos_new, p2_pos, p1_score_new, p2_score, turn + 1, turn_scores, cache)
            p1_future_wins += future_wins[0]
            p2_future_wins += future_wins[1]
        else:
            p2_pos_new = (p2_pos + turn_score) % 10
            p2_score_new = p2_score + p2_pos_new + 1

            if p2_score_new >= 21:
                p2_future_wins += 1
                continue

            future_wins = main_game(p1_pos, p2_pos_new, p1_score, p2_score_new, turn + 1, turn_scores, cache)
            p1_future_wins += future_wins[0]
            p2_future_wins += future_wins[1]

    cache[state] = (p1_future_wins, p2_future_wins)

    return cache[state]

with open("input\\21.txt") as f:
    data = f.read().split("\n")

p1_start = int(data[0].split(": ")[1]) - 1
p2_start = int(data[1].split(": ")[1]) - 1
turn_scores = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9]

practice_final = practice_game(p1_start, p2_start)
p1_wins, p2_wins = main_game(p1_start, p2_start, 0, 0, 0, turn_scores, {})

print(f"Loser Score X Roll Count: {practice_final}")
print(f"Universes Won (P1 : P2) {p1_wins} : {p2_wins}")