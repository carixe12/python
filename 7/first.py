students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def get_interests_and_lastname_length(students_dict):
    interests = set()
    lastname_length = 0
    for student in students_dict.values():
        interests.update(student['interests'])
        lastname_length += len(student['surname'])
    return interests, lastname_length

def get_student_id_age_pairs(students_dict):
    return [(id, student['age']) for id, student in students_dict.items()]

pairs = get_student_id_age_pairs(students)
interests, lastname_length = get_interests_and_lastname_length(students)
print("List of student ID-age pairs:", pairs)
print("Full list of interests of all students:", interests)
print("Total length of all students' last names:", lastname_length)