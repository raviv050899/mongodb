from src.tests.base_tests import BaseTests
import unittest
import HtmlTestRunner
import random


class Tests(BaseTests):
    def setUp(self):
        super().setUp()

    def test_validate_number_of_entries(self):
        # Generate random number between 1000 and 10,999.
        entries = random.randint(1000, 10000)

        # Generate entries.
        self.data_base.generate_random_entries(number_of_entries=entries)

        # Validate entries count.
        self.assertEqual(entries, self.data_base.get_number_of_entries())

    def test_validate_modify_entries(self):
        # Generate random number, this number will be number of entries.
        entries = random.randint(1000, 10000)

        # Generate entries.
        self.data_base.generate_random_entries(number_of_entries=entries)

        # Generate random number, this number will be the amout of modify entries.
        modify = random.randint(1000, entries)

        # Modify.
        self.data_base.modify(number_of_entries=modify)

        number_of_modify_entries = self.data_base.validate(print_all_modify_entries=False)

        # Validate number of modify entries.
        self.assertEqual(modify, number_of_modify_entries)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/raviv/Downloads/nms/reports'))
