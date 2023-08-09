import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        damage = 20
        opponent.health -= damage
        print(f"{self.name} attacked {opponent.name}! {opponent.name} has {opponent.health} health remaining.")

def main():
    warrior1 = Warrior("Warrior 1")
    warrior2 = Warrior("Warrior 2")

    while warrior1.health > 0 and warrior2.health > 0:
        attacker = random.choice([warrior1, warrior2])
        defender = warrior2 if attacker == warrior1 else warrior1

        attacker.attack(defender)

    if warrior1.health <= 0:
        print(f"{warrior2.name} wins!")
    else:
        print(f"{warrior1.name} wins!")

if __name__ == "__main__":
    main()