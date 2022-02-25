student_lst = ["Aaron Russell", "Alberta Hansen", "Ari Steeples", "Benjamin Stapleton", "Bilal Uddin", "Brady Hinks",
               "Bradley Collins", "Brandon Johnson", "David Sparks", "Delaney Heffernan", "Imran Moin", "Jason Zhang",
               "Jonathan Brown", "Luke Edmunds", "Marian Tiffany Santos", "Matthew Bouzane", "Noah Tuff", "Rui Hu",
               "Sean Cowan", "Terrence Careen", "Tyler Connolly", "Zheng Wang", ]


class StudentList:
    def __init__(self, list_name: str):
        self.name = list_name
        self.students = []

    # allows us to support for loops by making StudentList class iterable.
    def __iter__(self):
        for student in self.students:
            yield student

    def add_student(self, new_student: str):
        assert isinstance(new_student, str), "must be a string"
        self.students.append(new_student)

    def __len__(self):
        return len(self.students)


sd_2024 = StudentList(list_name="The By's")

for stu in student_lst:
    sd_2024.add_student(stu)

for student in sd_2024:  # TypeError: 'StudentList' object is not iterable
    print(student)

print("length = ",len(sd_2024))
