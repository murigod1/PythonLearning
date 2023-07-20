my_student = {
    'name': 'Murilo Jesus',
    'grades': [10, 9, 8, 7],
    'average': 'something',#something here that calculate the avarege
}

# def calcule_avarange(student):
#     return sum(student['grades']) / len(student['grades'])

class Zika:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    
    def calc_avarange(self):
        return sum(self.grades) / len(self.grades)
    
studant_one = Zika('Murilo jesus', [10, 9, 8, 7])

print(studant_one.calc_avarange())
print(Zika.calc_avarange(studant_one))