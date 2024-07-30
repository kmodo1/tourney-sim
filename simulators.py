from player_class import Player
import numpy as np

def round_robin_tournament(num_players = 100, skill_distribution_function = np.random.random):
    players = [Player(skill_distribution_function(), i) for i in range(num_players)]
    for i, p1 in enumerate(players):
        for p2 in players[i + 1:]:
            p1.play(p2)
    players.sort(key=lambda p : sum(p.wl_record)/(num_players - 1), reverse=True)
    return players