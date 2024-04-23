class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise ValueError('Достигнут максимум')

    def delete_student(self, last_name):
        if self.find_student(last_name):
            self.group.remove(self.find_student(last_name))

    def find_student(self, last_name):
        for student in tuple(self.group):
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students += f"{i.first_name} {i.last_name} {i.gender} {i.age}\n"
        return f'Number: {self.number}\n' + f'{all_students}'
