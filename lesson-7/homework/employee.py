class EmployeeManager:
    FILE_NAME = "employees.txt"

    def addNewEmployee(self):
        with open(self.FILE_NAME, "a") as file:
            id = input("Enter employee ID: ")
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = input("Enter salary: ")
            file.write(f"{id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!\n")

    def viewEmployees(self):
        with open(self.FILE_NAME, "r") as file:
            print(file.read())

    def searchEmployee(self):
        id = input("Enter employee ID to search: ")
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if id in line:
                    print("Employee found: ", line.strip())
                    return
        print("Employee not found!")

    def updateEmployee(self):
        id = input("Enter Employee ID to update: ")

        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(self.FILE_NAME, "w") as file:
            for line in lines:
                if line.startswith(id + ","):
                    name = input("New Name: ")
                    position = input("New Position: ")
                    salary = input("New Salary: ")
                    file.write(f"{id}, {name}, {position}, {salary}\n")
                else:
                    file.write(line)

        print("Employee updated!")

    def deleteEmployee(self):
        id = input("Enter employee ID to delete: ")
        lines = []
        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(id + ","):
                    lines.append(line)

        with open(self.FILE_NAME, "w") as file:
            file.writelines(lines)

        print("Employee deleted!")

    def exitProgram(self):
        print("Exiting... Goodbye!")
        exit()


def menu():
    manager = EmployeeManager()
    while True:
        choice = input("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit\n> ")
        if choice == "1":
            manager.addNewEmployee()
        elif choice == "2":
            manager.viewEmployees()
        elif choice == "3":
            manager.searchEmployee()
        elif choice == "4":
            manager.updateEmployee()
        elif choice == "5":
            manager.deleteEmployee()
        elif choice == "6":
            manager.exitProgram()
        else:
            print("Invalid choice.")


menu()

