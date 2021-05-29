from collections import deque

def combat(player1_base, player2_base, recursive = False, is_base = True):
    player1 = deque(player1_base)
    player2 = deque(player2_base)

    prev_states = set()

    while player1 and player2:
        if recursive:
            state_str = ",".join([str(i) for i in player1]) + ":" + ",".join([str(i) for i in player2])
            if state_str in prev_states:
                return 1
            prev_states.add(state_str)

        player1_card = player1.popleft()
        player2_card = player2.popleft()

        sub_game_winner = None
        if recursive and len(player1) >= player1_card and len(player2) >= player2_card:
            player1_new = [player1[i] for i in range(player1_card)]
            player2_new = [player2[i] for i in range(player2_card)]
            sub_game_winner = combat(player1_new, player2_new, True, False)

        round_winner = sub_game_winner or (1 if player1_card > player2_card else 2)

        if round_winner == 1:
            player1.append(player1_card)
            player1.append(player2_card)
        else:
            player2.append(player2_card)
            player2.append(player1_card)
    
    if is_base:
        return score(player1 if player1 else player2)
    return 1 if player1 else 2

def score(deck):
    score = 0
    value = len(deck)
    for card in deck:
        score += card * value
        value -= 1
    return score

with open("input/22.txt") as f:
    data = f.read().split("\n\n")

player1_base = [int(i) for i in data[0].split("\n")[1:]]
player2_base = [int(i) for i in data[1].split("\n")[1:]]

score_regular = combat(player1_base, player2_base)
score_recursive = combat(player1_base, player2_base, True)

print(f"Regular Combat Score: {score_regular}")
print(f"Recursive Combat Score: {score_recursive}")