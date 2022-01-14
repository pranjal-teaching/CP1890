pranjal_car = {
    'make': 'Subaru',
    'model': 'Forester',
    'year': 2015
}

delaney_car = {
    "make": "Ford",
    "model": "Fusion SE",
    "year": 2009
}

ben_car = {
    'make': 'Honda',
    'model': 'Civic',
    'year': 2012
}

matt_car = {
    'make': 'Hyundai',
    'model': 'Tucsan',
    'year': '2021'
}

all_cars = [pranjal_car, delaney_car, ben_car, matt_car]

for car in all_cars:
    print(f"{car['make']} {car['model']} {car['year']}")