# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.
import chardet

with open('test_file.txt', 'w') as file:
    file.write('сетевое програмирование\nсокет\nдекоратор')
    file.close()

with open('test_file.txt') as file:
    print(f'кодировка файла - {file.encoding}')
    for line in file:
        encoded_line = line.encode('utf-8')
        decoded_line = encoded_line.decode('utf-8')
        print(decoded_line)
