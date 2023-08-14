my_student = {
    'name': 'Murilo Jesus',
    'grades': [10, 9, 8, 7],
    'average': 'something',#something here that calculate the avarege
}

# def calcule_avarange(student):
#     return sum(student['grades']) / len(student['grades'])

# class Zika:
#     def __init__(self, new_name, new_grades):
#         self.name = new_name
#         self.grades = new_grades
    
#     def calc_avarange(self):
#         return sum(self.grades) / len(self.grades)
    
# studant_one = Zika('Murilo jesus', [10, 9, 8, 7])

# print(studant_one.calc_avarange())
# print(Zika.calc_avarange(studant_one))

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
    def __repr__(self):
        return f'<Garage {self.cars}>'
    
    def __str__(self):
        return f'Garage with {len(self)} cars.'
    
ford = Garage()
ford.cars.append('Fista')
ford.cars.append('Fucus')
ford.cars.append('Mustang')

print(ford)
print(ford[0])
print(len(ford))