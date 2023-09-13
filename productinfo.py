
class Product:

    def __init__(self,pid,pnm,prc,pqty,pven,pcat,mnfdate,expdate,discount = 0):
        self.product_id = pid
        self.product_name = pnm
        self.product_price = prc
        self.product_qty = pqty
        self.product_vendor = pven
        self.product_category = pcat
        self.product_mdate = mnfdate
        self.product_edate = expdate
        self.product_discount = discount

    def __str__(self):
        return f'''\n
        Product Name : {self.product_name} 
        Product Price : {self.product_price}
        Product Vendor : {self.product_vendor}
        Product Manf Date : {self.product_mdate.year}-{self.product_mdate.month}-{self.product_mdate.day}
        Product Exp Date : {self.product_edate.year}-{self.product_edate.month}-{self.product_edate.day}'''

    def __repr__(self):
        return str(self)


from datetime import datetime   # to deal with date and time...


def take_product_input_from_user():  # to take the input from user --> fill in the data inside Product Template
    pid = int(input('Enter Product Id : '))
    nm = input('Enter Product Name : ')
    price = float(input('Enter Product Price : '))
    qty = int(input('Enter Product Qty : '))
    ven = input('Enter Product Vendor : ')
    cate = input('Enter Product Category : ')
    dis = input('Enter Discount Percentage : ')
    mnf =  datetime(year=int(input('Enter Manf Year : ')),
                    month=int(input('Enter Manf Month : ')),
                    day=int(input('Enter Manf Day : ')))
    exp = datetime(year=int(input('Enter Exp Year : ')),
                   month=int(input('Enter Exp Month : ')),
                   day=int(input('Enter Exp Day : ')))
    product = Product(pid=pid,pnm=nm,prc=price,
            pqty=qty,
            pven=ven,pcat=cate,mnfdate=mnf,expdate=exp,discount=dis)
    return product

#prod = take_product_input_from_user()
#print(prod)