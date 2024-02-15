class Person:
    def __init__(self, name, age): # Se establecen los atributos de la clase en el __init__
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


if __name__ == '__main__':
    person = Person('John', 30)
    print('Age:', person.age)
    person.say_hello()
    # print(person.get_name())
    # print(person.get_age())