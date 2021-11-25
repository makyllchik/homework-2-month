# class Sort:
#     def __init__(self, my_number: list):
#         self.my_number = my_number
#
#     def bubble_sort(self):
#         swapped = False
#         for i in range(len(self.my_number) - 1, 0, -1):
#             for j in range(i):
#                 if self.my_number[j] > self.my_number[j + 1]:
#                     self.my_number[j], self.my_number[j + 1] = self.my_number[j + 1], self.my_number[j]
#                     swapped = True
#             if swapped:
#                 swapped = False
#             else:
#                 break
#         return self.my_number
#
#     def __str__(self):
#         return f'{self.my_number}'
#
#
# sort = Sort(my_number=[57, 46, 78, 1, 8, 568, 97, 536, 689])
#
# print(sort.bubble_sort())


class Sort:
    def __init__(self, my_number):
        self.my_number = my_number

    def section(self, lst):
        if len(lst) <= 1:
            return lst

        element = lst[0]
        left = list(filter(lambda num: num < element, lst))
        center = [num for num in lst if num == element]
        right = list(filter(lambda num: num > element, lst))

        return self.section(left) + center + self.section(right)

    def quick_sort(self):
        if len(self.my_number) <= 1:
            return self.my_number

        element = self.my_number[0]
        left = list(filter(lambda num: num < element, self.my_number))
        center = [num for num in self.my_number if num == element]
        right = list(filter(lambda num: num > element, self.my_number))

        return self.section(left) + center + self.section(right)


sort = Sort(my_number=[57, 46, 78, 1, 8, 568, 97, 536, 689])

print(sort.quick_sort())
