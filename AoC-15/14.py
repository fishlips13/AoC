class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time

        self.is_flying = True
        self.state_time = 0
        self.distance = 0
        self.points = 0

    def fly(self):
        if self.is_flying:
            self.distance += self.speed

        self.state_time += 1

        if self.is_flying and self.state_time == self.fly_time:
            self.is_flying = False
            self.state_time = 0
        elif not self.is_flying and self.state_time == self.rest_time:
            self.is_flying = True
            self.state_time = 0

    @staticmethod
    def find_leader(reindeers):
        leader = reindeers[0]
        for reindeer in reindeers:
            if reindeer.distance > leader.distance:
                leader = reindeer
        return leader

    @staticmethod
    def find_winner(reindeers):
        winner = reindeers[0]
        for reindeer in reindeers:
            if reindeer.points > winner.points:
                winner = reindeer
        return winner

    @staticmethod
    def award_leader(reindeers):
        leader = Reindeer.find_leader(reindeers)
        for reindeer in reindeers:
            if reindeer.distance >= leader.distance:
                reindeer.points += 1

with open("input/14.txt") as f:
    data = [i.split(" ") for i in f.read().split("\n")]

reindeers = [Reindeer(i[0], int(i[3]), int(i[6]), int(i[13])) for i in data]

finish_time = 2503
distance_max = 0

for reindeer in reindeers:
    segment_time = reindeer.fly_time + reindeer.rest_time
    full_segments = finish_time // segment_time
    remaining_time = finish_time % segment_time
    last_segment_time = min(remaining_time, reindeer.fly_time)
    distance = (full_segments * reindeer.fly_time + last_segment_time) * reindeer.speed
    distance_max = max(distance, distance_max)

for i in range(finish_time):
    for reindeer in reindeers:
        reindeer.fly()
    
    Reindeer.award_leader(reindeers)

print(f"Old Winner Distance: {distance_max}")
print(f"New Winner: {Reindeer.find_winner(reindeers).points}")