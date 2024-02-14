from person import Person

class Student(Person):
    def __init__(self, name, age, grade_level):
        super().__init__(name, age)
        self.grade_level = grade_level

    def study(self):
        print(f"{self.name} is studying.")