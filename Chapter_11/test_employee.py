import unittest
from employee import Employee

class EmployeeTestCases(unittest.TestCase):
    def setUp(self):
        self.e = Employee("John","Smith",60000)

    def test_give_default_raise(self):
        self.e.give_raise()
        self.assertEqual(self.e.salary, 65000)
    
    def test_give_custom_raise(self):
        self.e.give_raise(8000)
        self.assertEqual(self.e.salary, 68000)

if __name__ == "__main__":
    unittest.main()
