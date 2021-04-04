from src.data_base import DataBase

data_base = DataBase('my_database')
try:
    data_base.create()
    data_base.generate_random_entries(number_of_entries=20)
    data_base.modify(number_of_entries=3)
    data_base.print_all_entries()
    data_base.validate()
    data_base.clear()
    data_base.delete_container()
except Exception as ex:
    print(ex)
    data_base.clear()
    data_base.delete_container()




