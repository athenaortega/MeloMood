from person import Person

class Pet:
    def __init__(self, name):
        self.name = name
    def nap(self):
        print(self.name, "is napping")

class Dog(Pet):
    def bark(self):
        print(self.name, "says Woof!")

class Cat(Pet):
    def purr(self):
        print(self.name, "starts to purr.")

d1 = Dog("Buddy")
d1.bark()
c1 = Cat("Biscuit")
c1.purr()


me = Person("Athena")
other_person = Person("Snoopy")

print(me.name)
print(other_person.name)
