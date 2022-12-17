# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных


words2 = [b'class', b'function', b'method']
for w in words2:
    print(w, type(w), len(w))
