import re
import io


class WordsFinder:

    def __init__(self, *files):
        self.file_names = []
        for item in files:
            self.file_names.append(item)

    def get_all_words(self):
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


finder2 = WordsFinder('M07_L_11_test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
