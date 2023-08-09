class Student:
    def __init__(self, phi, group_number, progress):
        self.phi = phi
        self.group_number = group_number
        self.progress = progress

    def calculate_average_score(self):
        return sum(self.progress) / len(self.progress)


def sort_students_by_average_score(students):
    return sorted(students, key=lambda student: student.calculate_average_score())


def main():
    students = []

    for _ in range(10):
        phi = input("Enter student's PHI: ")
        group_number = input("Enter student's group number: ")
        progress = []
        for i in range(1, 6):
            score = float(input(f"Enter student's progress for item {i}: "))
            progress.append(score)
        student = Student(phi, group_number, progress)
        students.append(student)

    sorted_students = sort_students_by_average_score(students)

    print("Students sorted by average score:")
    for student in sorted_students:
        print(f"PHI: {student.phi}, Group Number: {student.group_number}, Average Score: {student.calculate_average_score()}")


if __name__ == "__main__":
    main()