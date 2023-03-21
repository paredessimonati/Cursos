import attr


class Enemy:
    def __init__(self, room_variables):
        self._hp = attr.enemies[room_variables["enemy"]]["hp"]
        self.attack = int(attr.enemies[room_variables["enemy"]]["hp"] / 10)
        self.name = room_variables["enemy"]
        self.alive = True
        self.visible = True
        self.aggro = True

    @property
    def hp(self):
        return self._hp

    def damage_received(self, n):
        self._hp -= n

    def is_visible(self, seed, visible_chance):
        if seed[6:8] < str(visible_chance):
            self.visible = True
        else:
            self.visible = False

    def description(self, seed, difficulty, room):
        description = room.current_room["what_in_front"]
        description += self.name
        description += ". "
        self.is_aggro(seed, difficulty)
        return description

    def is_aggro(self, seed, difficulty):
        aggro = int(seed[8]) + difficulty
        if aggro <= attr.enemies[self.name]["likelihood"]:
            self.aggro = True
        else:
            self.aggro = False
