
import re
import io
from pprint import pprint

class WordsFinder:
    """
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и
записывать их в атрибут file_names в виде списка или кортежа.
    """
    def __init__(self, *files):
        self.file_names = []
        for item in files:
            self.file_names.append(item)

        """
    Также объект класса WordsFinder должен обладать следующими методами:
        """

    def get_all_words(self):
        """
    Метод get_all_words - подготовительный, он возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        где:
    'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
        Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
    """
        get_all_words_dict = {}
        for file_item in self.file_names:
            with open(file_item, 'r', encoding='utf-8') as file:
                string_list_ = []
                sting_in_ = re.findall(r'\w+', file.read())
                for item in sting_in_:
                    string_list_.append(item.lower())
            get_all_words_dict[file_item] = string_list_
        return get_all_words_dict

    def find(self, word):
        """
    Метод find(self, word) , где word - искомое слово.
        Возвращает словарь, где:
        - ключ - название файла,
        - значение - позиция первого такого слова в списке слов этого файла.

        """
        word_ = word.lower()
        find_dict_ = {}
        for item in self.get_all_words().keys():
            i = 0
            for item_1 in self.get_all_words()[item]:
                if item_1.find(word_) >= 0:
                    find_dict_[item] = i
                    break
                i += 1
        return find_dict_

    def count(self, word):
        """
    Метод count(self, word) , где word - искомое слово.
        Возвращает словарь, где:
        - ключ - название файла,
        - значение - количество слова word в списке слов этого файла.
        """
        word_ = word.lower()
        count_dict_ = {}
        for item in self.find(word_).keys():
            count_sum = 0
            for item_1 in self.get_all_words()[item]:
                count_ = item_1.count(word_)
                if count_ > 0:
                    count_sum += count_
            count_dict_[item] = count_sum
        return count_dict_

        """   
В методах find и count пользуйтесь ранее написанным 
    методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) 
    можно воспользоваться методом словаря - item().
        """


finder2 = WordsFinder('M07_L_11_test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder_01 = WordsFinder('M07_L_11_t_f_1.txt','M07_L_11_t_f_2.txt','M07_L_11_t_f_3.txt','M07_L_11_t_f_4.txt','M07_L_11_t_f_5.txt','M07_L_11_t_f_6.txt','M07_L_11_t_f_7.txt','M07_L_11_t_f_8.txt')
print(f'\n СЛОВАРЬ: {finder_01.get_all_words()}')
print(f' СЛОВАРЬ FIND:  {finder_01.find('ДуБ')}')
print(f' СЛОВАРЬ COUNT: {finder_01.count('дуб')}')