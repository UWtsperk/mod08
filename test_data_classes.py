# ------------------------------------------------------------------------------- #
# Title: Unit Test for Data Classes File
# # Description: A collection of unit tests for data_classes.py.
# ChangeLog: (Who, When, What)
# TPerkins,12.5.2023,Created Script for Module 8
# ------------------------------------------------------------------------------- #
import unittest
from unittest import TestCase

from data_classes import Person, Employee


class TestPerson(TestCase):
    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(TestCase):
    def test_employee_init(self):  # Tests the constructor
        employee = Employee("John", "Doe", "2020-02-29", 5)
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.review_date, "2020-02-29")
        self.assertEqual(employee.review_rating, 5)


if __name__ == '__main__':
    unittest.main()
