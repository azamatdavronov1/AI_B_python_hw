def addNewEmployee():
    with open("employees.txt", "a") as file:  # Use "a" to append instead of overwriting
        emp_id = input("Enter employee ID: ")
        name = input("Enter name: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee added successfully!\n")


def viewEmployees():
    with open("employees.txt", "r") as file:
        print(file.read())


def searchEmployee():
    id = input("Enter employee ID to search: ")
    with open("employees.txt", "r") as file:
        for line in file:
            if id in line:
                print("Employee found: ", line.strip())
                return
    print("Employee not found!")


def updateEmployee():
    id = input("Enter Employee ID to update: ")

    with open("employees.txt", "r") as file:
        lines = file.readlines()

    with open("employees.txt", "w") as file:
        for line in lines:
            if line.startswith(id + ","):
                name = input("New Name: ")
                position = input("New Position: ")
                salary = input("New Salary: ")
                file.write(f"{id}, {name}, {position}, {salary}\n")
            else:
                file.write(line)

    print("Employee updated!")


def deleteEmployee():
    id = input("Enter employee ID to delete: ")
    lines = [ ]
    with open("employees.txt", "r") as file:
        for line in file:
            if not line.startswith(id + ","):
                lines.append(line)

    with open("employees.txt", "w") as file:
        file.writelines(lines)

    print("Employee deleted!")


def exitProgram():
    print("Exiting... Goodbye!")
    exit()


