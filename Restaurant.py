class Restaurant:
     
    def __init__(self):
        self.__orders = []
        self.__menu = []
    
    def set_order(self, order):
        self.__orders.append(order)
    
    def get_orders(self):
        return self.__orders
    
    def set_menu_item(self, item):
        self.__menu.append(item)

    def get_menu_items(self):
        return self.__menu