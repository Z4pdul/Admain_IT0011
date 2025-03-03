import json


student_records = [
    (202311, ("Abdullah", "Admain"), 76, 80),
    (202422, ("Rod", "Alvarado"), 98, 98),
    (202533, ("Nicole", "Heinrich"), 91, 95),
]

def save_file(filename="students.json"):
    with open(filename, "w") as f:
        json.dump(student_records, f)
    print("File saved successfully.")

def Open_file(filename="students.json"):
    global student_records
    try:
        with open(filename, "r") as f:
            student_records = json.load(f)
        print("File loaded successfully.")
    except FileNotFoundError:
        print("File not found. Starting with an empty record.")

def show_all_records():
    for s in student_records:
        print(s)

def order_by_lastname():
    for s in sorted(student_records, key=lambda x: x[1][1]):
        print(s)

def order_by_grade():
    for s in sorted(student_records, key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True):
        print(s)

def show_student(student_id):
    for s in student_records:
        if s[0] == student_id:
            print(s)
            return
    print("Student not found.")

def add_record(student_id, first_name, last_name, class_standing, exam_grade):
    student_records.append((student_id, (first_name, last_name), class_standing, exam_grade))
    print("Record added successfully.")

def edit_record(student_id, new_class_standing=None, new_exam_grade=None):
    for i, s in enumerate(student_records):
        if s[0] == student_id:
            student_records[i] = (s[0], s[1], new_class_standing or s[2], new_exam_grade or s[3])
            print("Record updated.")
            return
    print("Student not found.")

def delete_record(student_id):
    global student_records
    student_records = [s for s in student_records if s[0] != student_id]
    print("Record deleted.")

def main():
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Show All Students Record")
        print("4. Order by Last Name")
        print("5. Order by Grade")
        print("6. Show Student Record")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            Open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            show_all_records()
        elif choice == "4":
            order_by_lastname()
        elif choice == "5":
            order_by_grade()
        elif choice == "6":
            student_id = int(input("Enter student ID: "))
            show_student(student_id)
        elif choice == "7":
            student_id = int(input("Enter student ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_standing = float(input("Enter class standing grade: "))
            exam_grade = float(input("Enter major exam grade: "))
            add_record(student_id, first_name, last_name, class_standing, exam_grade)
        elif choice == "8":
            student_id = int(input("Enter student ID: "))
            class_standing = float(input("Enter new class standing grade (or press enter to skip): ") or 0)
            exam_grade = float(input("Enter new exam grade (or press enter to skip): ") or 0)
            edit_record(student_id, class_standing, exam_grade)
        elif choice == "9":
            student_id = int(input("Enter student ID: "))
            delete_record(student_id)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
