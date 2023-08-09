class Element:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return None


class Water(Element):
    def __init__(self):
        super().__init__("Water")

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return super().__add__(other)


class Air(Element):
    def __init__(self):
        super().__init__("Air")

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return super().__add__(other)


class Fire(Element):
    def __init__(self):
        super().__init__("Fire")

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return super().__add__(other)


class Earth(Element):
    def __init__(self):
        super().__init__("Earth")

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return super().__add__(other)


class Storm(Element):
    def __init__(self):
        super().__init__("Storm")


class Steam(Element):
    def __init__(self):
        super().__init__("Steam")


class Mud(Element):
    def __init__(self):
        super().__init__("Mud")


class Lightning(Element):
    def __init__(self):
        super().__init__("Lightning")


class Dust(Element):
    def __init__(self):
        super().__init__("Dust")


class Lava(Element):
    def __init__(self):
        super().__init__("Lava")


def main():
    water = Water()
    air = Air()
    fire = Fire()
    earth = Earth()
    result1 = water + air
    print(result1.name)  

    result2 = water + fire
    print(result2.name)  

    result3 = water + earth
    print(result3.name)  

    result4 = air + fire
    print(result4.name)  

    result5 = air + earth
    print(result5.name) 

    result6 = fire + earth
    print(result6.name)  

    result7 = air + water
    print(result7)  


if __name__ == "__main__":
    main()