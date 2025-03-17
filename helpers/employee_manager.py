import csv

from helpers.database import Database

class EmployeeManager:
    def __init__(self):
        self.db = Database()

    def add_employee(self,name,age,department,salary):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """INSERT INTO employees (name,age,department,salary) VALUES (%s,%s,%s,%s)"""
            cursor.execute(query,(name, age, department,salary))
            conn.commit()
            print(f"Employee added successfully!")
        except Exception as e:
            print(f"Error adding employee: {e}")
        finally:
            self.db.close()

    def view_employees(self):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """SELECT * FROM employees"""
            cursor.execute(query)
            employees = cursor.fetchall()

            print("\nEmployee List:")
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Age:{emp[2]}, Department: {emp[3]}, Salary: Rs. {emp[4]}")
        except Exception as e:
            print(f"Error fetching employees: {e}")
        finally:
            self.db.close()

    def search_employee(self,name=None, department=None):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """SELECT * FROM employees WHERE name=%s OR department=%s"""
            cursor.execute(query,(name,department))
            employees = cursor.fetchall()

            print(f"\nSearch Results:")
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Age:{emp[2]}, Department: {emp[3]}, Salary: Rs. {emp[4]}")
        except Exception as e:
            print (f"Error searching employees: {e}")
        finally:
            self.db.close()

    def update_employee(self, emp_id, name, age, department,salary):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """UPDATE employees SET name=%s, age=%s,department=%s, salary=%s WHERE id=%s"""
            cursor.execute(query,(name,age,department,salary,emp_id))
            conn.commit()
            print("Employee details updated successfully!")
        except Exception as e:
            print(f"Error while updating employee: {e}")
        finally:
            self.db.close()

    def delete_employee(self,emp_id):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """DELETE FROM employees WHERE id=%s"""
            cursor.execute(query,(emp_id,))
            conn.commit()
            print(f"Employee details deleted successfully!")
        except Exception as e:
            print(f"Error deleting employee: {e}")
        finally:
            self.db.close()

    def salary_statistics(self):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """SELECT MIN(salary), MAX(salary), AVG(salary) FROM employees"""
            cursor.execute(query)
            stats = cursor.fetchone()

            print("\n💰 Salary Statistics:")
            print(f"Min Salary: Rs. {stats[0]}, Max Salary: Rs. {stats[1]}, Average Salary: Rs. {stats[2]:.2f}")
        except Exception as e:
            print(f"Error while calculating salary statistics: {e}")
        finally:
            self.db.close()

    def export_to_csv(self):
        conn = self.db.connect_database()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * from employees")
            employees = cursor.fetchall()

            with open("employees.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID","Name","Age","Departmnet","Salary"])
                writer.writerows(employees)

            print("Data exported successfully to employees.csv")
        except Exception as e:
            print(f"Error while exporting data: {e}")
        finally:
            self.db.close()




