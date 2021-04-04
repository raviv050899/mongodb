from pymongo import MongoClient

ADDRESS = 'mongodb://localhost:27017/'


class MongoDbService:
    def __init__(self):
        self.mongo_client = None
        self.mydb = None
        self.dbcol = None
        self.entries = 0

    def connect(self):
        self.mongo_client = MongoClient(ADDRESS)
        self.mydb = self.mongo_client["mydatabase"]
        self.dbcol = self.mydb["messages"]

    def add_entry(self, entry):
        self.dbcol.insert_one(entry)
        self.entries += 1

    def get_by_id(self, id):
        return self.dbcol.find_one({'id': id})

    def get_by_modified_value(self, is_modified):
        return self.dbcol.find({'is_modified': is_modified})

    def modify(self, number_of_entries):
        # Define update field.
        update = {"$set": {'is_modified': True}}

        # get number of entries with is_modified=false.
        results = self.get_by_modified_value(False).limit(number_of_entries)

        # For each entry change is_modified fielkd from false to true.
        for entry in results:
            self.dbcol.update_one({'_id': entry['_id']}, update)

    @staticmethod
    def print_entry(entry):
        entry.pop('_id')
        print('(')
        for k, v in entry.items():
            print(f'\t\'{k}\': ', v)
        print(')\n')

    def print_all_entries(self):
        for x in self.dbcol.find():
            self.print_entry(x)

    def clear(self):
        self.dbcol.drop()
        self.entries = 0
