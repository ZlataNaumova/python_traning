from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self): #переопределяем функцию вывода значения на консоль. использется при вызове print
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other): #функция сравнения списков групп. мы переопределяем старую стандартную фуккцию
        return self.name == other.name and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max( self ): #функция для создания ключа сортировки по индексу группы. возвращает либо индекс либо оч. большое число, если индекс пустой
        #оч большое число необходимо, т.к при добавлении новой группы ей присваивается индекс больше тех, что уже содержатся на странице, но какой
        #именно мы не знаем
        if self.id:
            return int(self.id)
        else:
            return maxsize
