import unittest
from src.student import Student  # 假设类定义在 student.py 中

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student1 = Student("Alice", 20)
        self.student2 = Student("Bob", 21)

    def test_get_info(self):
        self.assertEqual(self.student1.get_info(), "Name: Alice, Age: 20")
        self.assertEqual(self.student2.get_info(), "Name: Bob, Age: 21")

    def test_name_property(self):
        self.assertEqual(self.student1.name, "Alice")
        self.assertEqual(self.student2.name, "Bob")

    def test_age_property(self):
        self.assertEqual(self.student1.age, 20)
        self.assertEqual(self.student2.age, 21)

if __name__ == '__main__':
    unittest.main()
