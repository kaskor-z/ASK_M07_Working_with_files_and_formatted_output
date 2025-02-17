# from pprint import pprint

class Product():

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name + ', ' + str(self.weight) + ', ' + self.category

    def get_product(self):
        return self.__str__()


class Shop():

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.file = open(self.__file_name, 'r')
        str_product = self.file.read()
        self.file.close()
        return str_product

    def add(self, *products):
        self.file = open(self.__file_name, 'a')
        for item in products:
            if self.get_products().find(item.name) >= 0:
                print(f'Продукт {item.name} уже есть в магазине')
            else:
                self.file.write(item.get_product() + '\n')
        self.file.close()
        return


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print('\n', p2, '\n')

s1.add(p1, p2, p3)

print(s1.get_products())
