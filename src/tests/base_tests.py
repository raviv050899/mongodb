import unittest
from src.data_base import DataBase


class BaseTests(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     pass

    def setUp(self):
        self.data_base = DataBase('my_database')
        self.data_base.create()

    def tearDown(self):
        self.data_base.clear()
        self.data_base.delete_container()

    # @classmethod
    # def tearDownClass(cls):
    #     pass
