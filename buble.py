from math import fsum


class Buffer:
    def __init__(self):
        self.sum = list()

    def add(self, *arg):
        self.sum += arg
        while len(self.sum) >= 5:
            print(int(fsum(self.sum[0:5])))
            self.sum = self.sum[5:]

    def get_current_part(self):
        return self.sum


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()


