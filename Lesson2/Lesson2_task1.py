import csv
import re

files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

match1 = r'Изготовитель системы'
match2 = r'Название ОС'
match3 = r'Код продукта'
match4 = r'Тип системы'


def get_data():
    for f in files:
        with open(f) as file:
            file_reader = csv.reader(file, delimiter=":")
            for row in file_reader:
                if match1 in row:
                    os_prod_list.append(row[1].strip(" "))
                elif match2 in row:
                    os_name_list.append(row[1].strip(" "))
                elif match3 in row:
                    os_code_list.append(row[1].strip(" "))
                elif match4 in row:
                    os_type_list.append(row[1].strip(" "))
    data = [os_prod_list, os_name_list, os_code_list, os_type_list]
    main_data = [[match1], [match2], [match3], [match4]]

    main_data[0].append(os_prod_list)
    main_data[1].append(os_name_list)
    main_data[2].append(os_code_list)
    main_data[3].append(os_type_list)

    return main_data


def write_to_csv():
    with open('data.csv', 'w', newline="") as file:
        file_writer = csv.writer(file, delimiter=" ")
        data = get_data()
        for row in data:
            file_writer.writerow(row)


get_data()
write_to_csv()
