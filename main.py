from helpers.database import Database
from helpers.employee_manager import EmployeeManager
from models.admin import Admin
from models.user import User


def main():
    while True:
        print("\nEmployee Management System")
        print("1. Login")
        print("2. Migrate Database (one-time)")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": # Login
            username = input("Enter username: ")
            password = input("Enter password: ")

            user = Admin(username,password) if username == "admin" else User(username,password)

            if not user.authenticate():
                print(f"Invalid username or password!")
            else:
                emp_manager = EmployeeManager()
                while True:
                    print("\nEmployee Management System")
                    print("1. Add Employee")
                    print("2. View Employees")
                    print("3. Search Employee")
                    print("4. Update Employee")
                    print("5. Delete Employee")
                    print("6. View Salary Statistics")
                    print("7. Add User (Admin Only)")
                    print("8. Export to CSV")
                    print("9. Logout")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        name = input("Enter Name: ")
                        age = int(input("Enter Age: "))
                        dept = input("Enter Department: ")
                        salary = float(input("Enter Salary: "))
                        emp_manager.add_employee(name,age,dept,salary)
                    elif choice == "2":
                        emp_manager.view_employees()
                    elif choice == "3":
                        name = input("Enter Name (or leave blank): ")
                        dept = input("Enter Department (or leave blank): ")
                        emp_manager.search_employee(name or None,dept or None)
                    elif choice == "4":
                        emp_id = int(input("Enter Employee ID: "))
                        name = input("Enter Name: ")
                        age = int(input("Enter Age: "))
                        dept = input ("Enter Department: ")
                        salary = float(input("Enter Salary: "))
                        emp_manager.update_employee(emp_id,name,age,dept,salary)
                    elif choice == "5":
                        emp_id = int(input("Enter Employee ID to delete: "))
                        emp_manager.delete_employee(emp_id)
                    elif choice == "6":
                        emp_manager.salary_statistics()
                    elif choice == "7" and isinstance(user,Admin):
                        new_user = input("Enter new username: ")
                        new_pass = input("Enter new password: ")
                        role = input("Enter role (admin/employee): ")
                        user.add_user(new_user,new_pass,role)
                    elif choice == "8":
                        emp_manager.export_to_csv()
                    elif choice == "9":
                        print("Logging out...")
                        break
                    else:
                        print(f"Invalid choice, please try again.")

        elif choice == "2": # Migrate Database (one-time)
            database = Database()
            database.setup_database()
        elif choice == "3": # Exit
            print("Exiting...")
            break
        else:
            print("Invalid Choice. Please enter a valid option.")

if __name__ == '__main__':
    main()