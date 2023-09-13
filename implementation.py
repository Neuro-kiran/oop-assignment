from inventoryservices import InventoryServices
from productinfo import Product

product_list = []


class Dmart(InventoryServices):
    def add_product(self,prod):
        if type(prod)==Product:
            product_list.append(prod)
            print('Product Successfully Added...')
        else:
            print('Invalid Product')

    def delete_product(self,pid):
        for prod in product_list:
            if prod.product_id == pid:
                product_list.remove(prod)
                print("Product Successfully Deleted..")
                break

    def update_product(self, product_id, updated_product):
        for prod in product_list:
            if prod.product_id == product_id:
                prod.product_name = updated_product.product_name
                prod.product_price = updated_product.product_price
                prod.product_qty = updated_product.product_qty
                prod.product_vendor = updated_product.product_vendor
                prod.product_category = updated_product.product_category
                prod.product_mdate = updated_product.product_mdate
                prod.product_edate = updated_product.product_edate
                prod.product_discount = updated_product.product_discount
                print("Product Successfully Updated..")
                break
        else:
            print("Product not found for the given ID.")

    def search_product(self, key, value):
        found_products = []
        for prod in product_list:
            if key == 'ID' and str(prod.product_id) == value:
                found_products.append(prod)
            elif key == 'CATEGORY' and prod.product_category == value:
                found_products.append(prod)
            elif key == 'VENDOR' and prod.product_vendor == value:
                found_products.append(prod)

        if found_products:
            print("Matching Products:")
            for prod in found_products:
                print(prod)
        else:
            print("No products found matching the search criteria.")

    def max_price_product(self):
        if product_list:
            max_price_product = max(product_list, key=lambda prod: prod.product_price)
            print("Product with Maximum Price:")
            print(max_price_product)
        else:
            print("No products in the inventory.")

    def min_price_product(self):
        if product_list:
            min_price_product = min(product_list, key=lambda prod: prod.product_price)
            print("Product with Minimum Price:")
            print(min_price_product)
        else:
            print("No products in the inventory.")

    def search_products_in_price_range(self, min_price, max_price):
        matching_products = [prod for prod in product_list if min_price <= prod.product_price <= max_price]
        if matching_products:
            print("Products in Price Range:")
            for prod in matching_products:
                print(prod)
        else:
            print("No products found within the specified price range.")

    def list_products(self):
        if product_list:
            print("List of Products:")
            for prod in product_list:
                print(prod)
        else:
            print("No products in the inventory.")



