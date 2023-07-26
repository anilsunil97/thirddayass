class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Dog: Bark! Bark!")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Cat: Meow! Meow!")

def animal_sound_in_zoo(animal):
    animal.make_sound()

# Creating instances of Dog and Cat classes
dog_instance = Dog()
cat_instance = Cat()

# Calling the animal_sound_in_zoo() function with the instances
print("Sounds in the Zoo:")
animal_sound_in_zoo(dog_instance)
animal_sound_in_zoo(cat_instance)
