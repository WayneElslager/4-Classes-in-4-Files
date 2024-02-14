from teacher import Teacher

class Headmaster(Teacher):
    def __init__(self, name, age, subject, department):
        super().__init__(name, age, subject)
        self.department = department

    def manage_department(self):
        print(f"{self.name} is managing the {self.department} department.")
