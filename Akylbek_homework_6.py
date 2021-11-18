class Total:
    def __init__(self, numbers: list, seek_sum: int):
        self.numbers = numbers
        self.seek_sum = seek_sum

    def find_index(self):
        for index in range(len(self.numbers)):
            for search_index in range(index + 1, len(self.numbers)):
                if (self.numbers[index] + self.numbers[search_index]) == self.seek_sum:
                    return [index, search_index]
        return None

    def __str__(self):
        return f'List of numbers: {self.numbers}\n' \
               f'Summa: {self.seek_sum}\n'


selected_number = Total(numbers=[2, 5, 8, 7, 1, 5, 3, 3], seek_sum=9)
print(selected_number)
print(selected_number.find_index())
