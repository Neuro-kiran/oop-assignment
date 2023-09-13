from userinfo import take_input_from_user,User
from implementation import Dmart
from productinfo import take_product_input_from_user

dservice = Dmart()

user_list = []
while True:
    print('''
    #########################################################
            1. Login
            2. Sign Up
    ##########################################################
    ''')
    choice = int(input('Enter Your Choice : '))
    if choice == 1:
        username = input('Enter Your Username : ')
        password = input('Enter Your Password : ')
        is_login_success = False
        for user in user_list:
            if user.username == username and user.password == password:
                print('Login Successful')
                is_login_success = True
                break

        if is_login_success:
            print('''
                           1. Add Product
                           2. Delete Product
                           3. Update Product
                           4. Search Product(ID,CATEGORY,VENDOR)
                           5. Max Price Product
                           6. Min Price Product
                           7. Search Product In Price Range(X,Y)
                           8. List Product
               ''')
            prch = int(input('Enter Your Choice: '))

            if prch == 1:
                prod = take_product_input_from_user()  # Assuming you have a function for taking product input
                dservice.add_product(prod)
            elif prch == 2:
                pid = int(input('Enter Product Id For Delete: '))
                dservice.delete_product(pid)
            elif prch == 3:
                # Code to update a product
                pid = int(input('Enter Product Id For Update: '))
                updated_prod = take_product_input_from_user()  # Assuming you have a function for taking updated product input
                dservice.update_product(pid, updated_prod)
                print('Product Updated Successfully')
            elif prch == 4:
                key = input('Enter Search Key (ID, CATEGORY, VENDOR): ')
                value = input('Enter Search Value: ')
                dservice.search_product(key, value)
            elif prch == 5:
                dservice.max_price_product()
            elif prch == 6:
                dservice.min_price_product()
            elif prch == 7:
                # Code for searching products in a price range
                min_price = float(input('Enter Minimum Price: '))
                max_price = float(input('Enter Maximum Price: '))
                dservice.search_products_in_price_range(min_price, max_price)
            elif prch == 8:
                dservice.list_products()
            else:
                print('Enter Valid Choice : ')

        else:
            print('Invalid Credentials...!')

    elif choice == 2:
        ob = take_input_from_user()
        #print('User Info : ',ob)
        user_list.append(ob)      # list of users...
        print(f'{ob.username} User Successfully Registered...!')
    else:
        print('Invalid Choice...')

    ch = input('Do you want to Continue : ')
    if ch.lower() in ['n', 'no']:
        break


print('Program Completed...!')

