def custom_write(file_name, strings):
    fail = open(file_name, "w", encoding="utf-8")
    string_posotions = {}
    keys = []
    values = []
    number_str = 0
    for string in strings:
        number_str += 1
        keys.append((number_str, fail.tell()))
        fail.write(f' {string} \n')
        values.append(string)
    fail.close
    string_posotions = dict(zip(keys, values))

    return string_posotions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
