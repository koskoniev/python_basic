from student_group import *

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(gr.find_student('Jobs'))
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!
print("OK")


user_list = []
for i in range(10):
    user_list.append((Student("male", i + 20, str(i), str(i), str(i))))

for i in user_list:
    try:
        gr.add_student(i)
    except ValueError as e:
        print(e)
