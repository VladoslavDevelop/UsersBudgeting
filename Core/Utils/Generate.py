import random


class Generate:
    """
    Класс для генерации случайных строк.
    """

    def __init__(self, count: int):
        self.count = count

    def generate(self):
        """
        Генерация случайной строки.
        :return:
        """

        simbols = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

        payload = ''
        for i in range(0, self.count):
            payload += random.choice(simbols)

        return payload
