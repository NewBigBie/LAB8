from abc import ABC


class Count(ABC):
    def _init_(self, address):
        self.address = address

    def calculateFreqs(self, address):
        pass


class ListCount(Count):
    def _init_(self, address):
        Count._init_(self, address)

    def calculateFreqs(self, address):
        list = []
        file = open(address)
        read_list = file.readline().split()

        for i in read_list:
            if i not in list:
                list.append(i)
        for i in range(0, len(list)):
            print(read_list.count(list[i]), " -> ", list[i])


class DictCount(Count):
    def _init_(self, address):
        Count._init_(self, address)

    def calculateFreqs(self, address):
        dict = {}
        file = open(address)
        read_dict = file.readline()

        for i in read_dict.split():
            dict[i] = dict.get(i, 0) + 1
        for i in dict:
            print("{} : {}".format(i, dict[i]))


my_address = 'C:\\Users\\Ergin YALMAN\\Desktop\\strange.txt'

print("\n*LAB - 8 - LIST*\n")
list_file = ListCount(my_address)
list_file.calculateFreqs(my_address)

print("\n*LAB - 8 - DICT*\n")
dict_file = DictCount(my_address)
dict_file.calculateFreqs(my_address)
