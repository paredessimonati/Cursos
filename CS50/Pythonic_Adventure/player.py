class Player:
    def __init__(self) -> None:
        self._hp = 300
        self.name = ""
        self.attack = 10
        self.defense = 0
        self.blind = 0
        self.evasion = 20
        self.accuracy = 80
        self.money = 0

    @property
    def hp(self):
        return self._hp

    # get hit = lose hp
    def damage_received(self, n):
        self._hp -= n

    # get varying degrees of blindness
    def blindness(self, n):
        self.blind = n + 2

    # get armor or lose it
    def armor_upgrade(self, n):
        self.defense = n

    # get weapon maybe?
    def current_attack(self, n):
        self.attack += n
