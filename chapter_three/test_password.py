import unittest
from chapter_three import password


class MyTestCase(unittest.TestCase):
    def test_mach(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(True, self.is_in_list(['144556', '444455', '225555'], list_of_potencial_passwords))

    def test_no_returning(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(False, '143455' in list_of_potencial_passwords)

    def test_first_match(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(True, self.is_in_list(['138899'], list_of_potencial_passwords))

    def test_double_inside_adjacent_match(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(True, '144556'in list_of_potencial_passwords)

    def test_last_match(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(True, '588999'in list_of_potencial_passwords)

    def test_no_mach(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(False, '145556' in list_of_potencial_passwords)

    # Trouble
    def test_no_four_middle(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(False, '155559' in list_of_potencial_passwords)

    def test_no_four_end(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(False, '138888' in list_of_potencial_passwords)

    def test_check_positive_with_brake_in_treee(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(True, '444566' in list_of_potencial_passwords)

    def test_check_positive_with_brake_in_two(self):
        list_of_potencial_passwords = password.find_password()
        self.assertEqual(True, '223444' in list_of_potencial_passwords)

    def is_in_list(self, control_list, potential_list):
        ans = []
        for l in control_list:
            if l in potential_list:
                ans.append(l)
        if len(ans) == len(control_list):
            return True
        else:
            False


if __name__ == '__main__':
    unittest.main()
