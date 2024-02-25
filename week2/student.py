database = {}
info = ["Age", "Grade", "StudentID"]

def add_student():
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    grade = input("Enter the student's grade: ")
    StudentID = input("Enter your student ID: ")
    database[name] = [age, grade, StudentID]
    print(f"{name} has been added to the database.")

def view_student():
    name = input("Enter the student's name: ")
    if name in database.keys():
        print(f"Name: {name}")
        for i in range(len(info)):
            print(f'Your {info[i]}: {database[name][i]}')
    else:
        print(f"{name} is not in the database.")
        option = input("do you want to register ? (Y/N): ")
        if option.upper() == "Y":
            add_student()
        elif option.upper() == "N":
            return
        else:
            print("Invalid input!")
            exit()

def list_students():
    for name in database.keys():
        print(f"Name: {name}")
        for i in range(len(info)):
            print(f'{info[i]}: {database[name][i]}')

def update_student():
    name = input("Enter the student's name: ")
    if name in database.keys():
        age = input("Enter the student's new age: ")
        grade = input("Enter the student's new grade: ")
        StudentID = input("Enter the student's new ID: ")
        database[name][0] = age
        database[name][1] = grade
        database[name][2] = StudentID
        print(f"{name}'s information has been updated.")
    else:
        print(f"{name} is not in the database.")

def delete_student():
    name = input("Enter the student's name: ")
    if name in database.keys():
        del database[name]
        print(f"{name} has been deleted from the database.")
    else:
        print(f"{name} is not in the database.")


def main():
    while True:
        print("What would you like to do?")
        print("1. Add a student")
        print("2. View a student")
        print("3. List all students")
        print("4. Update a student's information")
        print("5. Delete a student")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            list_students()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
