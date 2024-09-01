import numpy as np

class Player:
    def __init__(self, skill: float, id: int) -> None:
        self.skill = skill
        self.id = id
        self.wl_record = []
        self.game_record = []
    
    def __str__(self) -> str:
        return f"Player ID: {self.id},\t Player Skill: {self.skill}"

    def play(self, player_2) -> None:
        relative_log_difference = np.pow(10, (self.skill - player_2.skill)/0.2)
        result = np.random.random() < relative_log_difference/(relative_log_difference + 1)
        self.wl_record.append(result)
        self.game_record.append(player_2.id)
        player_2.wl_record.append(not result)
        player_2.game_record.append(self.id)