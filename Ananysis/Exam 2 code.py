class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Score: {self.score}"


# func to add a new student
def add_student(students, student):
    students.append(student)


# func to search student by id
def search_student(students, student_id):
    for student in students:  # fixed the typo here
        if student.student_id == student_id:
            return student
    return "Student not found"


# func to sort students in order 
def sort_students(students):
    return sorted(students, key=lambda x: x.score, reverse=True)



students = [
    Student(student_id=1, name="Amedeo", score=93),
    Student(student_id=2, name="Alejandro", score=90),
    Student(student_id=3, name="Jose", score=94),
]

# dem for add student func 
new_student = Student(student_id=4, name="Jonah", score=92)
add_student(students, new_student)


sorted_students = sort_students(students)
print("Sorted List of Students by Score (Descending):")
for student in sorted_students:
    print(student)

# dem for search students func 
search_id = 2
search_result = search_student(students, search_id)
print("\nSearch Result for student_id =", search_id)
print(search_result)

search_id = 5
search_result = search_student(students, search_id)
print("\nSearch Result for student_id =", search_id)
print(search_result)



