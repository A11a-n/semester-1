# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):

        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if name == "":
            raise ValueError("Name cannot be empty")

        if not isinstance(birth, date):
            raise TypeError("Birth must be a date object")

        self.name = name
        self.birth = birth

    def initials(self):
        return "".join([part[0].upper() for part in self.name.split()])

    def is_birthday(self):
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day
