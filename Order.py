from MenuItem import MenuItem

class Order:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def total(self):
        return sum(item.get_price() for item in self.__items if isinstance(item, MenuItem))
    
    def get_items(self):
        return self.__items