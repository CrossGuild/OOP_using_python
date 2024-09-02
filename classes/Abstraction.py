from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):

    @abstractmethod
    def apply_brakes(self):
        pass



class Tesla(Car):

    def apply_brakes(self):
        print("Tesla brakes")

class Audi(Car):
    def apply_brakes(self):
        print("Audi brakes")

if __name__ == '__main__':
    tesla = Tesla()
    tesla.apply_brakes()

    audi = Audi()
    audi.apply_brakes()
    # It's impossible to create a class with abstract class directly
    # car = Car()




