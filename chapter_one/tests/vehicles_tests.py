import unittest
from chapter_one.bin.vehicles import *
import sys
from io import StringIO


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.workshop = Workshop()
        self.stdout = StringIO()
        sys.stdout = self.stdout

    def test_cars(self):
        vehicle = Cars(4)
        self.workshop.accept(vehicle)
        output = self.stdout.getvalue().strip()
        self.assertEqual('Repairing a car with 4 number of wheels', output)

    def test_bicycles(self):
        vehicle = Bicycles(2)
        self.workshop.accept(vehicle)
        output = self.stdout.getvalue().strip()
        self.assertEqual('Repairing a bycycle with 2 number of wheels', output)

    def test_trucks0(self):
        vehicle = Trucks(12)
        self.workshop.accept(vehicle)
        output = self.stdout.getvalue().strip()
        self.assertEqual('Repairing a truck with 12 number of wheels', output)

    def tearDown(self):
        del self.workshop


if __name__ == '__main__':
    unittest.main()
