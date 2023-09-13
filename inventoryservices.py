from abc import ABC, abstractmethod

class InventoryServices(ABC):
    @abstractmethod
    def add_product(self, prod):
        pass

    @abstractmethod
    def delete_product(self, pid):
        pass

    @abstractmethod
    def update_product(self, product_id, updated_product):
        pass

    @abstractmethod
    def search_product(self, key, value):
        pass

    @abstractmethod
    def max_price_product(self):
        pass

    @abstractmethod
    def min_price_product(self):
        pass

    @abstractmethod
    def search_products_in_price_range(self, min_price, max_price):
        pass

    @abstractmethod
    def list_products(self):
        pass

    def m1(self):
        print("normal method --> it's not an abstract method")  # body
