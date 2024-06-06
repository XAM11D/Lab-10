class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Example of class usage:
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info())  # Output: Name: Ivan, Age: 30, Grade: 2

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name}: {self.sound}"

class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

# Example of class usage:
animal = Animal(name="Lala", sound="meow")
print(animal.make_sound())  # Output: Lala: meow

dog = Dog(name="Buddy", sound="bark", breed="Golden Retriever")
print(dog.make_sound())  # Output: Buddy: bark
