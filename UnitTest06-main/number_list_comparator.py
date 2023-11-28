class NumberListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, num_list):
        if len(num_list) == 0:
            return 0
        return sum(num_list) / len(num_list)

    def compare_lists(self):
        average1 = self.calculate_average(self.list1)
        average2 = self.calculate_average(self.list2)

        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average1 < average2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
        