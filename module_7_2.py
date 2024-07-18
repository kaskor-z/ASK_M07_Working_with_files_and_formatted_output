
def custom_write(file_name, strings):
    string_list_1 = []; string_list_2 = []; n_str_ = 0
    file = open(file_name, 'w+')
    for item in strings:
        item_tuple_ = []
        n_str_ += 1; item_tuple_.append(n_str_)
        n_byt_ = file.tell(); item_tuple_.append(n_byt_)
        string_list_1.append(tuple(item_tuple_))   # item_tuple_)
        string_list_2.append(item)
        file.write(item + '\n')
    strings_positions = dict(zip(string_list_1, string_list_2))
    return strings_positions


string_list_ = [
    'У лукоморья дуб зелёный;',
    'Златая цепь на дубе том:',
    'И днём и ночью кот учёный',
    'Всё ходит по цепи кругом;',
    'Идёт направо — песнь заводит,',
    'Налево — сказку говорит.',
    'Там чудеса: там леший бродит,',
    'Русалка на ветвях сидит;'
    ]

result = custom_write('test.txt', string_list_)
print('')
for elem in result.items():
    print(elem)