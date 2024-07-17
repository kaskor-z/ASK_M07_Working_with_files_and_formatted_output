from pprint import pprint

# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться
# запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
#                Все данные в строке разделены запятой с пробелами.

class Product():
    """
Объекты класса Product будут создаваться следующим образом -
        Product('Potato', 50.0, 'Vagetables')
и обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).

    """
    def __init__(self, name, weight, category):
        """
    обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
        """
        self.name = name
        self.weight = weight
        self.category = category
        self.__str__()

    def __str__(self):
        """
        Метод __str__, служебный, возвращает строку в формате
        '<название>, <вес>, <категория>'.
        Все данные в строке разделены запятой с пробелами.
        """
        return self.name + ', ' + str(self.weight) + ', ' + self.category

    def get_product(self):
        return self.__str__()



class Shop():
    """
    Объекты класса Shop будут создаваться следующим образом - Shop() и
    обладать следующими свойствами:
    """
    def __init__(self):
        """
        Инкапсулированный атрибут __file_name = 'products.txt'.
        """
        self.__file_name = 'products.txt'

    def get_products(self):
        """
        Метод get_products(self), который считывает всю информацию из файла __file_name,
        закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        """
        self.file = open(self.__file_name, 'r')
        return self.file.read(); self.file.close()



    def add(self, *products):
        """
        Метод add(self, *products), который принимает неограниченное количество объектов
        класса Product. Добавляет в файл __file_name каждый продукт из products,
        если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку
        'Продукт <название> уже есть в магазине' .
        """
        list_of_products = self.get_products()
        self.file = open(self.__file_name, 'a')
        for item in products:
            if list_of_products.find(item.name) >= 0:   # S.find(str, [start], [end])
                print(f'Продукт {item.name} уже есть в магазине')
            else:
                self.file = open(self.__file_name, 'a')
                self.file.write(item.get_product() + '\n')
        return self.file.close()

#         бакалея
#         Groceries
# # капеллини   овсянка крупа   пшено   рис
# # capellini   oatmeal grits   millet  rice
#
#         фрукты
#         fruit
# яблоки  груши   персики бананы  абрикося    виноград
# apples  pears   peach   bananas apricot     grapes
#
#         овощи
#         Vegetables
# огурци      помидоры    лук     капуста
# cucumbers   tomatoes    onion   cabbage

p2= Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('capellini', 5.2, 'Groceries')
p4 = Product('oatmeal grits', 4.6, 'Groceries')
p5 = Product('millet', 6.7, 'Groceries')
p6 = Product('rice', 12.4, 'Groceries')
p1 = Product('Potato', 50.5, 'Vegetables')
p7 = Product('cucumbers', 32.4, 'Vegetables')
p8 = Product('tomatoes', 45.8, 'Vegetables')
p9 = Product('onion', 25.0, 'Vegetables')
p10 = Product('cabbage', 53.2, 'Vegetables')
p11 = Product('apples', 42.4, 'fruit')
p12 = Product('pears', 33.1, 'fruit')
p13 = Product('rice', 12.4, 'Groceries')
p14 = Product('peach', 28.3, 'fruit')
p15 = Product('bananas', 49.2, 'fruit')
p16 = Product('apricot', 18.7, 'fruit')
p17 = Product('onion', 25.0, 'Vegetables')
p18 = Product('grapes', 41.8, 'fruit')

# print(f' p1 = {p1.get_product()} *****')
# print(f' p2 = {p2.get_product()} *****')
# print(p2)
# print(f' p1 = {p1}\t-> type(p1) = {type(p1)} ===\n p2 = {p2}\t-> type(p1) = {type(p2)} ===')

s1 = Shop()
s1.add(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18)
print(f'\n ============= Перечень принятых на склад продуктов ==============\n\n{s1.get_products()}')