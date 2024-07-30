import numpy as np

class Player:
    def __init__(self, skill: float, id: int):
        self.skill = skill
        self.id = id
        self.wl_record = []
        self.game_record = []
    
    def __str__(self):
        return f"Player ID: {self.id},\t Player Skill: {self.skill}"

    def play(self, player_2):
        result = self.skill - player_2.skill + np.random.normal(0.0, (1 - max(self.skill, player_2.skill)) * 1) > 0
        self.wl_record.append(result)
        self.game_record.append(player_2.id)
        player_2.wl_record.append(not result)
        player_2.game_record.append(self.id)