def custom_write(fale_name, strings):
    fail = open(fale_name, "w", encoding="utf-8")
    string_positions = {}
    keys = []
    values = []
    number_str = 0
    for string in strings:
        number_str += 1
        keys.append((number_str, fail.tell()))
        fail.write(f'{string}\n')
        values.append(string)
    fail.close()
    string_positions = dict(zip(keys, values))

    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test_file.txt', info)
for elem in result.items():
    print(elem)
