# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
# строкового представления в байтовое и выполнить обратное преобразование (используя
# методы encode и decode).


words = ["разработка", "администрирование", "protocol", "standard"]
encode_words = []
for w in words:
    encode_words.append(w.encode('utf-8'))
print(encode_words)

decode_words = []
for w in encode_words:
    decode_words.append(w.decode('utf-8'))

print(decode_words)
