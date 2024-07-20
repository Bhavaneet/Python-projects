import unittest
from unittest.mock import patch
import mysql.connector
from io import StringIO
import sys

# Mocking database connection and cursor
class MockCursor:
    def __init__(self):
        self.data = []

    def execute(self, sql, params=None):
        if sql.startswith('SELECT'):
            self.data = [(1, 'John Doe', 'Manager', 5000)]
        elif sql.startswith('INSERT'):
            self.data.append((params[0], params[1], params[2], params[3]))
        elif sql.startswith('DELETE'):
            self.data = []
        elif sql.startswith('UPDATE'):
            pass

    def fetchone(self):
        return self.data[0] if self.data else None

    def fetchall(self):
        return self.data

class TestEmployeeManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="emp"
        )
        cls.mock_cursor = cls.mock_db.cursor()

    @patch('mysql.connector.connect')
    @patch('mysql.connector.connect.cursor', return_value=MockCursor())
    def test_check_employee(self, mock_cursor, mock_connect):
        from main import check_employee

        # Test case where employee exists
        result = check_employee(1)
        self.assertTrue(result)

        # Test case where employee does not exist
        result = check_employee(2)
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['2', 'John', 'Manager', '5000'])
    def test_add_employee(self, mock_input):
        from main import add_employee

        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        add_employee()

        sys.stdout = sys.__stdout__  # Reset redirect

        # Check if "Employee Added Successfully" is in the captured output
        self.assertIn("Employee Added Successfully", captured_output.getvalue().strip())

    @patch('builtins.input', return_value='2')
    def test_remove_employee(self, mock_input):
        from main import remove_employee

        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        remove_employee()

        sys.stdout = sys.__stdout__  # Reset redirect

        # Check if "Employee Removed Successfully" is in the captured output
        self.assertIn("Employee Removed Successfully", captured_output.getvalue().strip())

    @patch('builtins.input', side_effect=['2', '1000'])
    def test_promote_employee(self, mock_input):
        from main import promote_employee

        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        promote_employee()

        sys.stdout = sys.__stdout__  # Reset redirect

        # Check if "Employee Promoted Successfully" is in the captured output
        self.assertIn("Employee Promoted Successfully", captured_output.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_employees(self, mock_stdout):
        from main import display_employees

        display_employees()

        # Check if employee details are correctly printed
        output = mock_stdout.getvalue().strip()
        self.assertIn("Employee Id :", output)
        self.assertIn("Employee Name :", output)
        self.assertIn("Employee Post :", output)
        self.assertIn("Employee Salary :", output)

    @patch('builtins.input', side_effect=['5'])
    def test_menu_exit(self, mock_input):
        from main import menu

        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        menu()

        sys.stdout = sys.__stdout__  # Reset redirect

        # Check if "Exiting the program. Goodbye!" is in the captured output
        self.assertIn("Exiting the program. Goodbye!", captured_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()