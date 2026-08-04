class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog says Woof")
class Cat(Animal):
    def sound(self):
        print("Cat says Meow")
class Cow(Animal):
    def sound(self):
        print("Cow says Moo")
a1 = Dog()
a2 = Cat()
a3 = Cow()
a1.sound()
a2.sound()
a3.sound()
