class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

    def make_sound(self):
        pass


class Dog(Animal):
    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

    def make_sound(self):
        print(f"{self.name} says wow!")


class Cat(Animal):
    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

    def make_sound(self):
        print(f"{self.name} says meow!")


rex = Dog("Rex")
rex.eat()
rex.sleep()
rex.make_sound()


morist = Cat("Morist")
morist.eat()
morist.sleep()
morist.make_sound()