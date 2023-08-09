class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def provide_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Children:")
        for child in self.children:
            print(f"- {child.name}")

    def calm_child(self, child):
        child.calm = True
        print(f"{self.name} calmed {child.name}.")

    def feed_child(self, child):
        child.hungry = False
        print(f"{self.name} fed {child.name}.")


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True


def main():
    parent = Parent("John", 40)
    child1 = Child("Emily", 10)
    child2 = Child("David", 6)

    parent.children.extend([child1, child2])

    parent.provide_information()

    parent.calm_child(child1)
    parent.feed_child(child1)

    parent.calm_child(child2)
    parent.feed_child(child2)


if __name__ == "__main__":
    main()