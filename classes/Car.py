class Car:

    def __init__(self, name = "Kuma"): # Implicitly called
        self.name = name

    """This is a test car"""
    # name = "Ferrari"
    # variables or class attributes
    # class methods or functions
    #
    # def set_car_name(self, name):
    #     self.name = name
    def accelerate(self):
        color = "red"
        print("Acclerating car {} having color {}". format(self.name, color))

    def applyBrakes(self):
        # Methodの中で定義された引数のみ使用できる
        print("Acclerating car {} having color {}". format(self.name, color))

    @staticmethod
    def repair_car(*args):
        print("Repairing car {}".format(*args))


if __name__ == '__main__':
    # help(Car)
    ferrari = Car()
    # ferrari.set_car_name("Ferrari")
    # ferrari.name = "Ferrari" #関数の変数で初期化
    print(ferrari.name)
    ferrari.accelerate()

    audi = Car("audi")
    # audi.name = ("audi")
    print(audi.name)
    audi.accelerate()
    audi.repair_car("hard")
