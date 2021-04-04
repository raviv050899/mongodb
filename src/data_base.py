from src.container_service import ContainerService
from src.mongo_db_service import MongoDbService
from src.utils import Utils
import random
import time


class DataBase:
    def __init__(self, name):
        self.name = name
        self.config = None
        self.container_service = None
        self.mongo_db_service = None

    def create(self):
        self._create_container_()
        self._create_mongodb_()

    def _create_container_(self):
        """
        Create mongo docker container and start.
        :return: None
        """
        self.container_service = ContainerService(self.name)
        self.container_service.create()
        self.container_service.run()

    def _create_mongodb_(self):
        """
        Create mongo db service client and connect.
        :return: None
        """
        self.mongo_db_service = MongoDbService()
        self.mongo_db_service.connect()

    def print_all_entries(self):
        """
        Print all entries from data base with the following structure:
        {
            'id':  uniqe integer value
            'is_modified':  True or False value
            'status':  integer value
            'data':  text field
            'timestamp':  integer value
        }
        :return: None
        """
        self.mongo_db_service.print_all_entries()

    def clear(self):
        """
        Remove all the entries form the database.
        :return: None
        """
        self.mongo_db_service.clear()

    def delete_container(self):
        """
        Stop and remove the docker container.
        :return: None
        """
        self.container_service.stop()
        self.container_service.remove()

    def get_number_of_entries(self):
        """
        Get and return how many entries database contains.
        :return: how many entries database contains.
        """
        return self.mongo_db_service.entries

    def generate_random_entries(self, number_of_entries):
        """
        Generate random N entries inside database.
        :param number_of_entries: Number of entries to generate.
        :return:
        """
        counter = 1
        for i in range(number_of_entries):
            self.mongo_db_service.add_entry(
                {
                    'id': counter,
                    'is_modified': False,
                    'status': random.randint(1, 1000000),
                    'data': Utils.generate_random_string(length=random.randint(8, 15)),
                    'timestamp': int(time.time())
                })
            counter += 1

    def modify(self, number_of_entries):
        """
        Randomly selects a number of entries and for each entry modifies
        the value of ‘is_modified’ field from false to true.
        :param number_of_entries: Number of entries to modify.
        :return: None
        """
        self.mongo_db_service.modify(number_of_entries)

    def validate(self, print_all_modify_entries=False):
        """
        Goes over the database and finds the entries that were modified.
        :return: All the entries that were modified by id's
        """
        counter = 0
        for entry in self.mongo_db_service.get_by_modified_value(True):
            if print_all_modify_entries:
                MongoDbService.print_entry(entry)
            counter += 1
        return counter
