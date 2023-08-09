import random

class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        if self.house.food >= 1:
            self.satiety += 20
            self.house.food -= 1
            print(f"{self.name} ate and gained 20 satiety.")
        else:
            print(f"{self.name} has no food in the house.")

    def work(self):
        self.satiety -= 10
        self.house.money += 50
        print(f"{self.name} worked and earned 50 money.")

    def play(self):
        self.satiety -= 10
        print(f"{self.name} played and lost 10 satiety.")

    def go_shopping(self):
        if self.house.money >= 10:
            self.house.food += 10
            self.house.money -= 10
            print(f"{self.name} went shopping and bought 10 food.")
        else:
            print(f"{self.name} has no money to go shopping.")

    def live_one_day(self):
        die_number = random.randint(1, 6)

        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50:
            self.work()
        elif die_number == 1:
            self.work()
        elif die_number == 2:
            self.eat()
        else:
            self.play()

        if self.satiety < 0:
            print(f"{self.name} died due to starvation.")
            return False
        else:
            return True


class House:
    def __init__(self):
        self.food = 50
        self.money = 0


def main():
    house = House()

    person1 = Person("Artyom", house)
    person2 = Person("Sophia", house)

    for day in range(1, 366):
        print(f"Day {day}:")
        print("----------")
        person1.live_one_day()
        person2.live_one_day()
        print()

    print("Experiment finished.")


if __name__ == "__main__":
    main()