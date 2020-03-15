import unittest
from chapter_one.bin.car import Car
from chapter_one.bin.car import IllegalCarError


class MyTestCase(unittest.TestCase):

    def test_total_mass(self):
        c = Car(1, 1000, 5)
        self.assertEqual(c.total_mass, 1070)

    def test_zero_pax(self):
        self.assertRaises(IllegalCarError, Car, 0, 1000, 5)

    def test_too_meany_pax(self):
        self.assertRaises(IllegalCarError, Car, 6, 1000, 5)

    def test_too_big_weight(self):
        self.assertRaises(IllegalCarError, Car, 5, 2001, 5)

    def test_assignments_of_wrong_mass(self):
        c = Car(1, 1000, 5)
        self.assertRaises(IllegalCarError, c.set_car_mass, 2001)

    def test_assignments_of_zero_pax(self):
        c = Car(1, 1000, 5)
        self.assertRaises(IllegalCarError, c.set_pax_count, 0)

    def test_assignments_of_to_meany_pax(self):
        c = Car(1, 1000, 5)
        self.assertRaises(IllegalCarError, c.set_pax_count, 6)


if __name__ == '__main__':
    unittest.main()
