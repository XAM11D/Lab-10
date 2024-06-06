# Lab-10
Лабораторна робота 10: Робота з класами у Python

Мета роботи
Метою даної лабораторної роботи є ознайомлення з об'єктно-орієнтованим програмуванням у Python. Студенти навчаться створювати класи, реалізовувати наслідування та використовувати методи класів для обробки даних.

Опис завдання
Завдання 1: Створити клас Student з атрибутами name, age та grade, а також методом для відображення інформації про студента.
Завдання 2: Створити базовий клас Animal з атрибутами name та sound, і методом для виведення звуку тварини. Реалізувати клас-нащадок Dog, що успадковує від Animal і додає атрибут breed.

Виконання роботи

Завдання 1:
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Приклад використання класу:
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info())  # Output: Name: Ivan, Age: 30, Grade: 2

Завдання 2:
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

# Приклад використання класу:
animal = Animal(name="Lala", sound="meow")
print(animal.make_sound())  # Output: Lala: meow

dog = Dog(name="Buddy", sound="bark", breed="Golden Retriever")
print(dog.make_sound())  # Output: Buddy: bark

Результати
Завдання 1: Створено клас Student, який містить атрибути name, age, grade і метод display_info, що повертає інформацію про студента у форматованому рядку.
Завдання 2: Створено базовий клас Animal з методами та атрибутами, а також клас-нащадок Dog, що успадковує від Animal і додає атрибут breed. Перевірено роботу методів обох класів.

Вимоги до середовища:Python 3.x
