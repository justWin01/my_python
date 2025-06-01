import os
import shutil
import time as t

STUDENTS_FILE = 'data/students.txt'
GRADES_FILE = 'data/grades.txt'
BACKUP_DIR, TRASH_DIR = 'backup/', 'trash/'

#File Structure method
def initialize_file_structure():
    for directory in ['data', BACKUP_DIR, TRASH_DIR]:
        os.makedirs(directory, exist_ok=True)

#Read files methods
def read_files():
    try:
        with open(STUDENTS_FILE, 'r') as f1, open(GRADES_FILE, 'r') as f2:
            return [line.strip() for line in f1], [line.strip() for line in f2]
    except (IOError, FileNotFoundError):
        return [], []


#Create Backup method
def create_backup():
    try:
        for file, backup in [(STUDENTS_FILE, 'students_backup.txt'), (GRADES_FILE, 'grades_backup.txt')]:
            if os.path.exists(file):
                shutil.copy(file, os.path.join(BACKUP_DIR, backup))
        print("Backup created.")
    except Exception as e:
         print("\033[91m \033[0m")
         print(f"\033[91mBackup error: {e}\033[0m")
         print("\033[91m \033[0m")
      


#Save Data method
def save_data(records):
    try:
        with open(STUDENTS_FILE, 'w') as f1, open(GRADES_FILE, 'w') as f2:
            for student, grade in records:
                f1.write(f"{student}\n")
                f2.write(f"{grade}\n")
    except IOError as e:
         print("\033[91m \033[0m")
         print(f"\033[91mError saving data: {e}\033[0m")
         print("\033[91m \033[0m")

#Add record method
def add_record(student, grade):
    start_time = t.time()
    students, grades = read_files()
    students.append(student)
    grades.append(grade)
    save_data(zip(students, grades))
    print("------------------------------------------------------------")
    print("Successfully added")
    print("------------------------------------------------------------")
    end_time = t.time()
    print(f"st: {start_time}, et: {end_time}, diff: {end_time - start_time}")

#Delete Record method
def delete_record(student, to_trash=True):
    students, grades = read_files()
    if student in students:
        idx = students.index(student)
        student, grade = students.pop(idx), grades.pop(idx)
        if to_trash: move_to_trash(student, grade)
        save_data(zip(students, grades))
        print(f"Deleted {student}")
    else:
         print("\033[91m \033[0m")
         print(f"\033[91m{student} not found.\033[0m")
         print("\033[91m \033[0m")
        

#Move to Trash method
def move_to_trash(student, grade):
    with open(os.path.join(TRASH_DIR, f"{student}_trash.txt"), 'w') as f:
        f.write(f"{student}\n{grade}")
    print(f"Moved {student} to trash.")

#Restore from Trash method
def restore_from_trash(student):
    trash_file = os.path.join(TRASH_DIR, f"{student}_trash.txt")
    if os.path.exists(trash_file):
        with open(trash_file, 'r') as f:
            student_name, grade = [line.strip() for line in f]
            print(f"Students:  {student_name}, Grade: {grade} " )
        add_record(student_name, grade)
        os.remove(trash_file)
        print(f"Restored {student} from trash.")
    else:
         print("\033[91m \033[0m")
         print(f"\033[91mNo trash for {student}.\033[0m")
         print("\033[91m \033[0m")
      
#Restore all from Trash Method
def restore_all_from_trash():
    restored = 0
    for trash_file in os.listdir(TRASH_DIR):
        with open(os.path.join(TRASH_DIR, trash_file), 'r') as f:
            student_name, grade = [line.strip() for line in f]
        add_record(student_name, grade)
        os.remove(os.path.join(TRASH_DIR, trash_file))
        restored += 1
    print(f"Restored {restored} records.") if restored else print("No records to restore.")

#Search Grade method
def search_grade(student):
    start_time = t.time()
    students, grades = read_files()
    end_time = t.time()
    print(f"st: {start_time}, et: {end_time}, diff: {end_time - start_time}")
    return grades[students.index(student)] if student in students else f"{student} not found."

#Update Grade method
def update_grade(student, new_grade):
    start_time = t.time()
    students, grades = read_files()
    if student in students:
        grades[students.index(student)] = new_grade
        save_data(zip(students, grades))
        print(f"Updated {student}'s grade to {new_grade}")
        end_time = t.time()
        print(f"st: {start_time}, et: {end_time}, diff: {end_time - start_time}")
    else:
         print("\033[91m \033[0m")
         print(f"\033[91m{student} not found.033[0m")
         print("\033[91m \033[0m")
         end_time = t.time()
         print(f"st: {start_time}, et: {end_time}, diff: {end_time - start_time}")

#Get valid Grade
def get_valid_grade():
    while True:
        try:
            return int(input("Enter grade: "))
        except ValueError:
             print("\033[91m \033[0m")
             print("\033[91mInvalid grade. Try again.\033[0m")
             print("\033[91m \033[0m")


#Main Function
def main():
    #call the Initialize_File_Structure
    initialize_file_structure()
    while True:
        print("\n1. Add Record\n2. Load Data\n3. Delete Record\n4. Search Grade\n5. Update Grade\n6. Save to Backup\n7. Restore from Trash\n8. Restore All \n9.Exit")
        choice = input("Select option: ").strip()

        if choice == '1':
            name = input("Enter student name: ")
            if name.lower()in [s.lower() for s in read_files()[0]]:
                print("\033[91m \033[0m")
                print(f"\033[91mError: {name} exists.\033[0m")
                print("\033[91m \033[0m")
            else:
                grade = get_valid_grade()
                add_record(name, grade)
        elif choice == '2':
            students, grades = read_files()
            if students and grades:
                print("----------------------------------------------------------")
                print("\n".join(f"{s}: {g}" for s, g in zip(students, grades)))
                print("----------------------------------------------------------")
            else:
                print("----------------------------------------------------------")
                print("\033[91m \033[0m")
                print("\033[91mNo data.\033[0m")
                print("\033[91m \033[0m")
                print("----------------------------------------------------------")
        elif choice == '3':
            student = input("Enter name to delete: ")
            delete_record(student)
        elif choice == '4':
            student = input("Enter name to search: ")
            print("--------------------------------------------------------------")
            print("GRADE:"+search_grade(student))
            print("--------------------------------------------------------------")
        elif choice == '5':
            print("----------------------------------------------------------")
            student = input("Enter name to update grade: ")
            print("----------------------------------------------------------")
            grade = get_valid_grade()
            update_grade(student, grade)
        elif choice == '6':
            create_backup()
        elif choice == '7':
            print("----------------------------------------------------------")
            student = input("Enter name to restore: ")
            restore_from_trash(student)
            print("----------------------------------------------------------")
        elif choice == '8':
            restore_all_from_trash()
        elif choice == '9':
            print("Exiting.")
            print("----------------------------------------------------------")
            break
        else:
            print("Invalid choice.")
main()
