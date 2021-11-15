import re

# file_path = "MOCK_DATA.txt"
# result_file_path = "mail.txt"
# file_reader = open(file_path, mode="r", encoding="Latin-1")
# results_file = open(result_file_path, mode="w", encoding="Latin-1")
# my_text_1 = file_reader.read()
#
# searching = r"[\w+_-]+@[\w_+]+.[\w.]+"
# results_all = re.findall(searching, my_text_1)
#
#
# for item in results_all:
#     print(item)
#     results_file.write(item+"\n")
#
# print(f"Total: {str(len(results_all))}")


file_path = "MOCK_DATA.txt"
result_file_path = "fullname.txt"
file_reader = open(file_path, mode="r", encoding="Latin-1")
results_file = open(result_file_path, mode="w", encoding="Latin-1")
my_text_1 = file_reader.read()

searching=r"[A-Z][a-z]+\W+\w+\s[A-Z]\w+|[A-Z][A-Za-z]+\s[A-Z]\w+|[A-Za-z]\w+\s[A-Z][']?[A-Z]\w+"
results_all = re.findall(searching, my_text_1)
for item in results_all:
    print(item)
    results_file.write(item + "\n")

print(f"Total: {str(len(results_all))}")


# file_path = "MOCK_DATA.txt"
# result_file_path = "domen.txt"
# file_reader = open(file_path, mode="r", encoding="Latin-1")
# results_file = open(result_file_path, mode="w", encoding="Latin-1")
# my_text_1 = file_reader.read()
#
# searching = r"[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|" \
#             r"[A-Z]+[a-z]+\w+[.]+[a-z]+|" \
#             r"[A-Z]+[a-z]+[.]+[a-z]+[0-9]|"\
#             r"[A-Z]+[a-z]+[.]+[a-z]+|" \
#             r"[A-Z]+[.]+[a-z]+|" \
#             r"[A-Z]+[.]+[a-z]+[0-9]"
# results_all = re.findall(searching, my_text_1)
#
# for item in results_all:
#     print(item)
#     results_file.write(item + "\n")
#
# print(f"Total: {str(len(results_all))}")


# file_path = "MOCK_DATA.txt"
# result_file_path = "colour.txt"
# file_reader = open(file_path, mode="r", encoding="Latin-1")
# results_file = open(result_file_path, mode="w", encoding="Latin-1")
# my_text_1 = file_reader.read()
#
# searching = r"#\w+"
# results_all = re.findall(searching, my_text_1)
#
# for item in results_all:
#     print(item)
#     results_file.write(item+"\n")
#
# print(f"Total: {str(len(results_all))}")
