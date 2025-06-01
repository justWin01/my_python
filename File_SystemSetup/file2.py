import os
import shutil



Student_File = 'data/students.txt'
Grades_File = 'data/students.txt'
Backup_Dir, Trash_Dir = 'backup/', 'trash/'



def initial_file_structure():
    for directory in ['data' , Backup_Dir , Trash_Dir]:
        os.makedirss(directory , exist_ok = True)

def read_files():
     try:
         with open(Student_File , 'r') as f1, open(Grades_File, 'r') as f2:
             return[line.strip() for line in f1], [line.strip() for line in f2]
     except (IOError , FileNotFoundError):
         return [] , []

def add_students(student, grade):
    students, grades = read_files()
    students.append(student)
    grades.append(grade)
    save(zip(students,grades))
    print("Successfully Added.....")

def get_valid_grade():
    while True:
        try:
            return int(input("Enter grade: "))
        except ValueError:
            print("Invalid Grade. try again.....")

def save(records):
    try:
        with open(Student_File, 'w') as f1, open(Grades_File, 'w') as f2:
            for student, grade in records:
                f1.write(f"{student}")
                f2.write(f"{grade}")
         
    except IOError as e:
        print(f"Error saving data: {e}")

def update_grade(student, new_grade):
    students, grades = read_files()
    if student in students:
        grades[students.index(student)] = new_grade
        save(zip(students,grades))
        print*(f"Updated {student}'s grade to {new_grade}")
    else:
        print(f"{student} not found.....")

def search_grade(student):
        students , grades = read_files()
        return grades[students.index(student)] if student in students else f"{student} not found......"

def create_backup():
    try:
        for file, backup in [(Student_File , 'students_backup.txt'), (Grades_File, "grades_backup.txt")]:
            if os.path.exists(file):
                shutil.copy(file, os.path.join(Backup_Dir, backup))
                print("backup crated..........")
    except Exception as e:
        print(f"erorr: {e}")

def delete(student, to_trash = True):
    students , grades = read_files()
    if student in students:
        idx = students.index(student)
        student , grade = students.pop(idx) , grades.pop(idx)
        if to_trash: move_to_trash(student,grade)
        save(zip(students, grades))
        print(f"deleted {student}")
    else:
        print(f"{student} not found.......")

def move_to_trash(student):
    with open(os.path.join(Trash_Dir, f"{student}_trash.text"), 'w') as f:
        f.write(f"{student}\n{grade}")
    print(f"Moved {student} to trash.....")