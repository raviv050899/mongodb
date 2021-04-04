import random
import string


class Utils:
    @staticmethod
    def generate_random_string(length):
        """
        Generate random string.
        :param length: The require length of the return string.
        :return: Random string base on given length (upper & lower case characters)
        """
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length))