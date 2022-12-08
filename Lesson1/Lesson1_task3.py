# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
# байтовом типе.


words4 = ["attribute", "класс", "функция", "type"]

for w in words4:
    try:
        print(bytes(w, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово {w} невозможно записать в байтовом типе')

# невозможно записать в байтовом типе слова на русском языке, поскольку они не подлежат кодировке ASCII
