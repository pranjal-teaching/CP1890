student = {
    'firstname': 'Pranjal',
    'lastname': 'Patra',
    'age': 35,
    'college': 'CNA',
    'vaccinated': True,
    'courses': ['Python', 'Java', 'C++']
}

for david in student:
    print(david, student[david])

for oliver, sabina in student.items():
    print(oliver, sabina)
