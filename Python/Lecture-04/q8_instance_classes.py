# Create a class Player with: a class variable player_count and instance variables name and level. Track how many players were created

class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

p1 = Player("Lionel", 5)
p2 = Player("Messi", 10)
p3 = Player("Ronaldo", 9)

print("Total Players Created:", Player.player_count)
