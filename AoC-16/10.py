import re

class Bot:
    def __init__(self, bot_id):
        self.bot_id = bot_id
        self.chips = []
        self.target_low = None
        self.target_high = None
    
def bot_make(bot_id, bots):
    if bot_id not in bots:
        bot = Bot(bot_id)
        bots[bot_id] = bot
    return bots[bot_id]

with open("input/10.txt") as f:
    data = f.read().split("\n")

bots = {}
outputs = {}
bots_ready = []

for line in data:
    values = re.findall(r"[a-z]+ \d+", line)
    if len(values) == 2:
        bot = bot_make(values[1], bots)

        bot.chips.append(int(re.search(r"\d+", values[0]).group(0)))
        if len(bot.chips) == 2:
            bots_ready.append(bot)
    else:
        bot = bot_make(values[0], bots)

        bot.target_low = values[1]
        bot.target_high = values[2]

bot_cp_61_17_id = None
while bots_ready:
    bot = bots_ready.pop()
    bot.chips.sort()

    if bot.chips == [17, 61]:
        bot_cp_61_17_id = bot.bot_id

    if bot.target_low in bots:
        bot_low = bots[bot.target_low]
        bot_low.chips.append(bot.chips[0])
        if len(bot_low.chips) == 2:
            bots_ready.append(bot_low)
    else:
        outputs[bot.target_low] = bot.chips[0]

    if bot.target_high in bots:
        bot_high = bots[bot.target_high]
        bot_high.chips.append(bot.chips[1])
        if len(bot_high.chips) == 2:
            bots_ready.append(bot_high)
    else:
        outputs[bot.target_high] = bot.chips[1]

output123_prod = outputs["output 0"] * outputs["output 1"] * outputs["output 2"]
print(f"61-17 Comparison Bot ID: {bot_cp_61_17_id}")
print(f"Output 1-2-3 Product: {output123_prod}")