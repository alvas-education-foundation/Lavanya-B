# github repository- Lavanya-B

from dataclasses import dataclass


@dataclass
class Person:
    '''A simple Person with name and age'''
    name: str
    age: int



person = Person("Lavanya B", 20)
print(person)