people = {
          1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
        }
#print all of the nested dictionary
print(people)

#print one of the nested dictionary elements
print(people[2])

#print specific elements of one dictionary
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

#add a new element to a nested dictionary
people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])

#alternatively, add another dictionary to the nested dictionary (similar to above)
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])


#print all of the nested dictionary again
print(people)

#delete elements from a nested dictionary
del people[3]['married']
del people[4]['married']

print(people[3])
print(people[4])

#delete dictionary from a nested dictionary
del people[3], people[4]
print(people)

#iterate through a Nested dictionary
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])
