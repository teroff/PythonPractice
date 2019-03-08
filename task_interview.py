# Person:
# id
# first
# name
# last
# name
# department
# 
# Department:
# id
# name
#
# PersonService
# get
# person
# by
# id
# add
# person
# to
# department
# remove
# person
# to
# department


# !/usr/bin/python

class Person:

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName


class Department:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonServices:
    # list of persons it already knows about
    self.list_of_persons = []
    self.user_id
    self.department_name

    def __init__(self, person_list):
        self.list_of_persons = person_list

    def add_person_to_dept(self, person):
        self.new_person = []
        for elem in person:
            new_person.append(elem)

    self.list_of_persons.append(self.new_person)

    return self.list_of_persons.append


def get_person_by_id(self, id):
    self.id = id

    if len(self.list_of_persons) < 0:
        return False

    for elem in self.list_of_persons:
        if elem == id:
            index = self.list_of_persons.index(id)

            return self.list_of_persons[index]
        else:
            return "No user % found", (id)


ps = PersonServices()
ps.add_person_to_dept(Person(2, "Name", "LastName"))