from typing import Self

class Person:
    def login(self):
        pass

    @classmethod
    def from_db(cls, id: int) -> Self:
        # Get from database
        return cls(id=id)

class AdminPerson(Person):
    def sudo(self, task: str):
        ...

me = Person.from_db(123)
me.login()

super_me = AdminPerson.from_db(1234)
super_me.sudo("make sandwich")