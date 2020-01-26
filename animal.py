import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--action", "-a", help='what action animal should do')
ap.add_argument("--quantity", "-q", help='how much times they should do actions')


class Animal:
    # ВАШ КОД ЗДЕСЬ
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    # ВАШ КОД ЗДЕСЬ
    pass

    def play_with_ball(self):
        print(f"{self.name.capitalize()} run to a ball and become happy")


class Cat(Animal):
    # ВАШ КОД ЗДЕСЬ
    pass

    def nightrunner(self):
        print(f"Everybody wake up, {self.name} is happy")


class Cow(Animal):
    # ВАШ КОД ЗДЕСЬ
    pass

    def walking_with_bell(self):
        print(f"Cow walking on the grass")


def main():
    # ВАШ КОД ЗДЕСЬ
    pass


if __name__ == '__main__':
    args = ap.parse_args()
    main()
