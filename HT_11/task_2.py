""" 
2. Створити клас Person, в якому буде присутнім метод __init__ який 
буде приймати якісь аргументи, які зберігатиме в відповідні змінні.

- Методи, які повинні бути в класі Person - show_age, print_name, 
show_all_information.

- Створіть 2 екземпляри класу Person та в кожному з екземплярів 
створіть атр. profession (його не має інсувати під час ініціалізації)
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show_age(self):
        print(f"The age of this Person is {self.age}")


    def print_name(self):
        print(f"The name of this Person is {self.name}")


    def show_all_information(self):
        print(f"Person's information: {self.__dict__}")


print("\n---------------")
mike = Person("Mike", 25)
mike.show_age()
mike.print_name()
mike.profession = "Python Dev"
mike.show_all_information()

print("\n---------------")
duke = Person("Duke", 35)
duke.show_age()
duke.print_name()
duke.profession = "Data Analyst"
duke.show_all_information()
