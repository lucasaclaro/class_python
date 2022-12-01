from random import randint

class Person:
    current_year = 2022

    #Atributos
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Métodos
    def years_birth(self):
        years_of_birth = self.current_year - self.age
        return years_of_birth

    #Método da classe (aqui pode ser criado um método da própria classe para criar um objeto
    @classmethod
    def for_year_birth(cls, name, year_of_birth):
        age = cls.current_year - year_of_birth
        return cls(name, age)

    #Método estático
    @staticmethod
    def generate_id():
        rand = randint(10000, 19999)
        return rand

person1 = Person('Han Solo', 45)
print(f"Name: {person1.name}.")
print(f"Age: {person1.age}.")
print(f"Year of birth: {person1.years_birth()}")

#O método estático pode ser chamado tanto via classe quanto via objeto
print(f"ID: {Person.generate_id()}")

person2 = Person.for_year_birth('Han Solo', 1977)
print(f"\nName: {person2.name}.")
print(f"Age: {person2.age}.")
print(f"Year of birth: {person2.years_birth()}")

#O método estático pode ser chamado tanto via classe quanto via objeto
print(f"ID: {person2.generate_id()}")




