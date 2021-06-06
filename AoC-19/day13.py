from intcode import Intcode

game = Intcode()

level = [[0] * 44 for _ in range(20)]
score = 0

# 0 -> 43, 0 -> 19
# 3874

while game.status != "halted":
    if game.status == "awaiting output":
        x = game.output_signal()
        y = game.output_signal()
        t_id = game.output_signal()

        if x == -1 and y == 0:
            score = t_id
        else:
            level[y][x] = t_id
    elif game.status == "awaiting input":
        game.input_signal(0)

print(score)