"""
Given a file with the following rows:
    Student_name subject mark
Get the student from each subject who secured the highest mark
"""

def read_student_records(filename):
    s = {}
    with open(filename) as f:
        for line in f.readlines():
            student, subject, mark = line.split()
            if s.has_key(subject):
                if s[subject]["mark"] < mark:
                    s[subject] = { "student": student, "mark" : mark }
            else:
                s[subject] = { "student": student, "mark" : mark }
    f.close()
    return s


st = read_student_records("student_records.txt")

for course in st:
    print(course, st[course]["student"], st[course]["mark"])
