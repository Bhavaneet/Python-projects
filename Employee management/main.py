import mysql.connector

class EmployeeDatabase:
    def __init__(self, host, user, password, database):
        self.con = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.con.cursor()

    def check_employee(self, employee_id):
        sql = 'SELECT * FROM employees WHERE id=%s'
        self.cursor.execute(sql, (employee_id,))
        result = self.cursor.fetchone()
        return result is not None

    def add_employee(self, Id, Name, Post, Salary):
        if self.check_employee(Id):
            print("Employee already exists. Please try again.")
            return False
        
        sql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
        data = (Id, Name, Post, Salary)
        try:
            self.cursor.execute(sql, data)
            self.con.commit()
            print("Employee Added Successfully")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.con.rollback()
            return False

    def remove_employee(self, Id):
        if not self.check_employee(Id):
            print("Employee does not exist. Please try again.")
            return False
        
        sql = 'DELETE FROM employees WHERE id=%s'
        data = (Id,)
        try:
            self.cursor.execute(sql, data)
            self.con.commit()
            print("Employee Removed Successfully")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.con.rollback()
            return False

    def promote_employee(self, Id, Amount):
        if not self.check_employee(Id):
            print("Employee does not exist. Please try again.")
            return False
        
        try:
            sql_select = 'SELECT salary FROM employees WHERE id=%s'
            self.cursor.execute(sql_select, (Id,))
            current_salary = self.cursor.fetchone()[0]
            new_salary = int(current_salary) + int(Amount)

            sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
            self.cursor.execute(sql_update, (new_salary, Id))
            self.con.commit()
            print("Employee Promoted Successfully")
            return True
        except (ValueError, mysql.connector.Error) as e:
            print(f"Error: {e}")
            self.con.rollback()
            return False

    def display_employees(self):
        try:
            sql = 'SELECT * FROM employees'
            self.cursor.execute(sql)
            employees = self.cursor.fetchall()
            for employee in employees:
                print("Employee Id : ", employee[0])
                print("Employee Name : ", employee[1])
                print("Employee Post : ", employee[2])
                print("Employee Salary : ", employee[3])
                print("------------------------------------")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close_connection(self):
        if self.con.is_connected():
            self.cursor.close()
            self.con.close()
            print("Database connection closed.")

def menu(employee_db):
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")
        
        ch = input("Enter your Choice: ")

        if ch == '1':
            Id = input("Enter Employee Id: ")
            Name = input("Enter Employee Name: ")
            Post = input("Enter Employee Post: ")
            Salary = input("Enter Employee Salary: ")
            employee_db.add_employee(Id, Name, Post, Salary)
        elif ch == '2':
            Id = input("Enter Employee Id: ")
            employee_db.remove_employee(Id)
        elif ch == '3':
            Id = input("Enter Employee's Id: ")
            Amount = input("Enter increase in Salary: ")
            employee_db.promote_employee(Id, Amount)
        elif ch == '4':
            employee_db.display_employees()
        elif ch == '5':
            employee_db.close_connection()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    try:
        employee_db = EmployeeDatabase(host="localhost", user="root", password="password", database="emp")
        menu(employee_db)
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")