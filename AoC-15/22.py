from copy import deepcopy

class SpellEffects:
    @staticmethod
    def magic_missile(gate_state):
        gate_state.boss_hp -= 4

    @staticmethod
    def drain(gate_state):
        gate_state.player_hp += 2
        gate_state.boss_hp -= 2

    @staticmethod
    def shield_apply(gate_state):
        gate_state.shield_timer = 6

    @staticmethod
    def poison_apply(gate_state):
        gate_state.poison_timer = 6

    @staticmethod
    def recharge_apply(gate_state):
        gate_state.recharge_timer = 5

spellbook = [("Magic Missile", 53, SpellEffects.magic_missile),
             ("Drain",         73, SpellEffects.drain),
             ("Shield",       113, SpellEffects.shield_apply),
             ("Poison",       173, SpellEffects.poison_apply),
             ("Recharge",     229, SpellEffects.recharge_apply)]

class GameState:
    def __init__(self, player_hp, player_mana, boss_hp, boss_dmg, hard_mode):
        self.player_hp = player_hp
        self.mana = player_mana

        self.boss_hp = boss_hp
        self.boss_dmg = boss_dmg

        self.shield_timer = 0
        self.poison_timer = 0
        self.recharge_timer = 0

        self.hard_mode = hard_mode

        self.spent_mana = 0
        self.history = []
    
    def get_memo(self):
        states = [self.player_hp, self.boss_hp, self.mana, self.spent_mana,
            self.shield_timer, self.poison_timer, self.recharge_timer]

        return ",".join([str(i) for i in states])

    def can_cast(self, spell):
        if  spell[0] == "Shield"   and self.shield_active() or \
            spell[0] == "Poison"   and self.poison_active() or \
            spell[0] == "Recharge" and self.recharge_active() or \
            spell[1] > self.mana:
            return False
        return True

    def cast(self, spell):
        spell[2](self)
        self.mana -= spell[1]
        self.spent_mana += spell[1]

    def boss_attack_player(self):
        boss_att = max(1, self.boss_dmg - (7 if self.shield_active() else 0))
        self.player_hp -= boss_att

    def shield_active(self):
        return self.shield_timer > 0

    def poison_active(self):
        return self.poison_timer > 0

    def recharge_active(self):
        return self.recharge_timer > 0

    def proc_effects(self):
        if self.shield_active():
            self.shield_timer -= 1

        if self.poison_active():
            self.boss_hp -= 3
            self.poison_timer -= 1

        if self.recharge_active():
            self.mana += 101
            self.recharge_timer -= 1

    def check_win(self):
        if self.boss_hp <= 0:
            return True
        return False

    def check_lose(self):
        if self.player_hp <= 0:
            return True
        return False

def game_turn(game_state, spellbook, cache = set()):

    mana_min = 9999999
    for spell in spellbook:
        game_state_new = deepcopy(game_state)

        # Hard mode damage
        if game_state_new.hard_mode:
            game_state_new.player_hp -= 1

        # Did we lose? (hard mode damage)
        if game_state_new.check_lose():
            break

        # Start of player turn effects
        game_state_new.proc_effects()

        # Can we cast spell?
        if not game_state_new.can_cast(spell):
            continue

        # Cast spell, fail out if it uses too much mana
        game_state_new.cast(spell)
        if game_state_new.spent_mana > mana_min:
            continue

        # Did we win? (missile or drain)
        if game_state_new.check_win():
            mana_min = min(mana_min, game_state_new.spent_mana)
            continue

        # Start of boss turn effects
        game_state_new.proc_effects()

        # Did we win? (poison tick)
        if game_state_new.check_win():
            mana_min = min(mana_min, game_state_new.spent_mana)
            continue

        # Get hit by boss
        game_state_new.boss_attack_player()

        # Did we lose?
        if game_state_new.check_lose():
            continue

        # Skip visited sub-paths
        memo = game_state_new.get_memo()
        if memo in cache:
            continue
        cache.add(memo)

        # Take a new turn (recur)
        mana_min = min(mana_min, game_turn(game_state_new, spellbook, cache))

    # Return the best path
    return mana_min

with open("input/22.txt") as f:
    data = [i.split(": ") for i in f.read().split("\n")]

game_state_normal = GameState(50, 500, int(data[0][1]), int(data[1][1]), False)
game_state_hard = GameState(50, 500, int(data[0][1]), int(data[1][1]), True)

best_mana_normal = game_turn(game_state_normal, spellbook)
print(f"Best Mana Win (Normal): {best_mana_normal}")

best_mana_hard = game_turn(game_state_hard, spellbook)
print(f"Best Mana Win (Hard): {best_mana_hard}")