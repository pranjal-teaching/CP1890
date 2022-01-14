# create a dict
emp_dict = {}

student = {
    'firstname': 'Pranjal',
    'lastname': 'Patra',
    'age': 35,
    'college': 'CNA',
    'vaccinated': True,
    'courses': ['Python', 'Java', 'C++'],
    10: 'ten',
    3.14: 'pi'
}
# keys must be immutable for example: string, int, tuple, float.
# !lists and dicts cannot be keys!
# values can be any type

print(len(student))

# add details to dictionary
student['email'] = 'pranjal.patra@cna.nl.ca'
print(len(student))

# update details of dictionary
student['age'] = 36 # updates age if age does not exist, otherwise it will create a new key
print(student)

# delete elements from a dictionary
del student['age']
print(student)

# print details of dictionary
print(student)
print(student['firstname'])

