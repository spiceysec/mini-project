################################################################################################################
#                  __            __                                                                   __       #
#                 /  |          /  |                                                                 /  |      #
#    _____  ____  $$/  _______  $$/         ______    ______    ______      __   ______    _______  _$$ |_     #
#   /     \/    \ /  |/       \ /  |       /      \  /      \  /      \    /  | /      \  /       |/ $$   |    #
#   $$$$$$ $$$$  |$$ |$$$$$$$  |$$ |      /$$$$$$  |/$$$$$$  |/$$$$$$  |   $$/ /$$$$$$  |/$$$$$$$/ $$$$$$/     #
#   $$ | $$ | $$ |$$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$/ $$ |  $$ |   /  |$$    $$ |$$ |        $$ | __   #
#   $$ | $$ | $$ |$$ |$$ |  $$ |$$ |      $$ |__$$ |$$ |      $$ \__$$ |   $$ |$$$$$$$$/ $$ \_____   $$ |/  |  #
#   $$ | $$ | $$ |$$ |$$ |  $$ |$$ |      $$    $$/ $$ |      $$    $$/    $$ |$$       |$$       |  $$  $$/   #
#   $$/  $$/  $$/ $$/ $$/   $$/ $$/       $$$$$$$/  $$/        $$$$$$/__   $$ | $$$$$$$/  $$$$$$$/    $$$$/    #
#                                         $$ |                       /  \__$$ |                                #
#                                         $$ |                       $$    $$/                                 #
#                                         $$/                         $$$$$$/                                  #
#                                                                                                              #
################################################################################################################

# modules imported
import pymysql
import os
from dotenv import load_dotenv

# load environment file and set variables for connection
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# set connection variable
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# set cursor variable
cursor = connection.cursor()

# main menu function, access other menus, exit programme
def main_menu():
    print('')
    print('############### Main Menu ##############')
    print('#                                      #')
    print('#     Enter numbers to select page     #')
    print('#                                      #')
    print('#            1   Products              #')
    print('#            2   Order Menu            #')
    print('#            3   Couriers              #')   # main menu def block
    print('#                                      #')
    print('#            0   Exit                  #')
    print('#                                      #')
    print('########################################')
    print('')
    print('Enter option below.')
    option = int(input(''))
    print('')
    print(f'You entered option {option}')

    if option == 1:
        product_menu()
    elif option == 2: 
        order_menu()
        pass
    elif option == 3: 
        courier_menu()
        pass
    elif option == 0:
        cursor.close()
        connection.close()
        print('Programme exporting to files...') 
        print('Programme Closing...') 
        print('')
        exit() 
    else: 
        print('')
        print('Invalid Input. ') 
        print('')
        main_menu() # reopen the menu 

# product menu function list product, add product, update product, remove product
def product_menu():
    print('')
    print('############# Product Menu #############')
    print('#                                      #')
    print('#            1  List Products          #')
    print('#            2  Add New Product        #')
    print('#            3  Remove Product         #')
    print('#            4  Update Product         #')
    print('#                                      #')
    print('########################################')    # product page def block
    print('#                                      #')
    print('#           0   Main Menu              #')
    print('#                                      #')
    print('########################################')
    print('')
    print('Enter option below.')
    option = int(input(''))
    print('')
    print(f'You entered option {option}')
    print('')
    if option == 1:
        cursor.execute("SELECT product_name, product_price FROM product_table;")
        for item in cursor:
            print(item)
        product_menu() 
    elif option == 2: 
        add_product_name = str(input('Enter a product name: '))
        add_prod_price = float(input('Enter the products price : £'))
        cursor.execute(f"INSERT INTO product_table(product_name, product_price) VALUES ('{add_product_name}','{add_prod_price}');")
        warning_input = input('')
        if warning_input.lower == "y":
            connection.commit()
        else:
            product_menu()
        product_menu()
    elif option == 3:
        cursor.execute("SELECT product_id, product_name FROM product_table;")
        for item in cursor:
            print(item)
        select_id = input('Enter the ID you want to delete: ')
        warning_input_1 = int(input('WARNING! Are you Sure? Y / N '))
        if warning_input_1.lower() == "y":
            cursor.execute("DELETE FROM product_table  WHERE product_id = '{select_id}';")
            connection.commit()
        else:
            product_menu()
        product_menu()
    elif option == 4: 
        cursor.execute("SELECT product_id, product_name FROM product_table;")
        for item in cursor:
            print(item)
        get_product_id = int(input('Enter a product ID to edit: '))
        print('Would you like to change the product name? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            print('Enter a new product name: ')
            new_prod_name = str(input(''))
            cursor.execute(f"UPDATE product_table SET product_name = '{new_prod_name}' WHERE product_id = '{get_product_id}';")
        print('Would you like to change the product price? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            print('Enter a new price for product: ')
            new_prod_price = float(input(''))
            cursor.execute(f"UPDATE product_table SET product_price = '{new_prod_price}' WHERE product_id = '{get_product_id}';")
            product_menu()
        else: 
            product_menu()
    elif option == 0:   
        main_menu() 
    else: 
        print('') 
        print('Invalid Input.') 
        print('')
        product_menu() 

# order menu function list orders, add order, edit/update orders, remove order 
def order_menu():
    print('')
    print('############# Order Menu ###############')
    print('#                                      #')
    print('#            1  Print Orders           #')
    print('#            2  Create Order           #')
    print('#            3  Update Status          #')
    print('#            4  Remove Order           #')
    print('#                                      #')
    print('########################################')    # oder log page def block
    print('#                                      #')
    print('#           0   Main Menu              #')
    print('#                                      #')
    print('########################################')
    print('')
    print('Enter option below.')
    option = int(input(''))
    print('')
    print(f'You entered option {option}')  
    print('')
    if option == 1:
        cursor.execute("SELECT order_id, order_name, order_address, cust_num, order_products, order_status, courier_id FROM order_table;")
        for item in cursor:
            print(item)
    elif option == 2:
        for i in range(1):
            print('Enter order name below.')
            order_name = input('')
            print('Enter delivery address below.')
            order_addr = input('')
            print('Enter customer phone number below.')
            order_phone = input('')
            cursor.execute("SELECT product_id, product_name, product_price FROM product_table;")
            for item in cursor:
                print(item)
            add_prods = input('Enter product IDs to add to oder with commas seperating the values: ')
            cursor.execute("SELECT courier_id, courier_name FROM courier_table;")
            for item in cursor:
                print(item)
            courier_select = input('Enter courier ID to use for order: ')
            validate = input('Place order  Y / N')
            if validate.lower == 'y':
                cursor.execute(f"INSERT INTO order_table (order_name, order_address, order_num, order_products, order_status, courier_id) VALUES ('{order_name}', '{order_addr}', '{order_phone}', '{add_prods}', 1, '{courier_select}')")
                connection.commit()
                order_menu()
            else:
                order_menu()
        order_menu()
    elif option == 3:
        cursor.execute("SELECT order_id, order_name, order_address, cust_num, order_products, order_status, courier_id FROM order_table;")
        for item in cursor:
            print(item)
        get_order_id = int(input('Enter the order ID of the one you want to change: '))
        print('Would you like to change the order name? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            print('Enter a new order name: ')
            new_order_name = str(input(''))
            cursor.execute(f"UPDATE order_table SET order_name = '{new_order_name}' WHERE order_id = '{get_order_id}';")
        print('Would you like to change the order address? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            print('Enter a new address: ')
            new_address_name = str(input(''))
            cursor.execute(f"UPDATE order_table SET order_address = '{new_address_name}' WHERE order_id = '{get_order_id}';")
        print('Would you like to change the customers number? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            print('Enter a number: ')
            new_cust_num = int(input(''))
            cursor.execute(f"UPDATE order_table SET cust_num = '{new_cust_num}' WHERE order_id = '{get_order_id}';")
        print('Would you like to change the products in the order? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            cursor.execute("SELECT product_id, product_name FROM product_table;")
            for item in cursor:
                print(item)
            new_products = str(input('Enter new products IDs seperated by commas: '))
            cursor.execute(f"UPDATE order_table SET order_products = '{new_products}' WHERE order_id = '{get_order_id}';")
        print('Would you like to change the order status? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            cursor.execute("SELECT status_id, statuses FROM status_table;")
            for item in cursor:
                print(item)
            new_status_id = int(input('Enter the ID of a status: '))
            cursor.execute(f"UPDATE order_table SET order_status = '{new_status_id}' WHERE order_id = '{get_order_id}';")
        print('Would you like to change the courier? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            cursor.execute("SELECT courier_id, courier_name FROM courier_table;")
            for item in cursor:
                print(item)
            new_courier_id = int(input('Enter the ID of a courier: '))
            cursor.execute(f"UPDATE order_table SET coueir_id = '{new_courier_id}' WHERE order_id = '{get_order_id}';")
        else:
            order_menu()
        order_menu()
    elif option == 4:
        cursor.execute("SELECT order_id, order_name, order_address, cust_num, order_products, order_status, courier_id FROM order_table;")
        for item in cursor:
            print(item)
        select_order = int(input('Enter the order ID you want to delete: '))
        warning_input = input('WARNING: are you sure you want to delete? Y / N')
        if warning_input.lower == 'y':
            cursor.execute(f"DELETE FROM order_table WHERE order_id = '{select_order}';")
            order_menu()
        else:
            order_menu()
    elif option == 0:
        main_menu()

# courier manu function list couriers, add courier, update courier info, remove courier 
def courier_menu():
    print('')
    print('############# Courier Menu #############')
    print('#                                      #')
    print('#            1  Print Couriers         #')
    print('#            2  Add Courier            #')
    print('#            3  Update Courier         #')
    print('#            4  Remove Courier         #')
    print('#                                      #')
    print('########################################')    # courier log page def block
    print('#                                      #')
    print('#           0   Main Menu              #')
    print('#                                      #')
    print('########################################')
    print('')
    print('Enter option below.')
    option = int(input(''))
    print('')
    print(f'You entered option {option}')  
    print('')
    if option == 1:
        cursor.execute("SELECT courier_name, courier_num FROM courier_table;")
        for item in cursor:
            print(item)
        courier_menu()
    elif option == 2:
        add_courier_name = input('Enter courier name: ')
        add_courier_num = input('Enter courier number: ')
        print('WARNING: you are about to add a courier, continue? Y / N')
        warning_input = input('')
        if warning_input == "Y" or "y":
            cursor.execute(f"INSERT INTO courier_table(courier_name, courier_num) VALUES ('{add_courier_name}','{add_courier_num}');")
            connection.commit()
            courier_menu()
        else: 
            courier_menu()
    elif option == 3:
        cursor.execute("SELECT courier_id, courier_name FROM courier_table;")
        for item in cursor:
            print(item)
        select_id = input('Enter the ID you want to edit: ')
        warning_input_1 = int(input('Would you like to edit the name? Y / N '))
        if warning_input_1.lower() == "y":
            new_courier_name = str(input('Enter a name for the courier: '))
            cursor.execute(f"UPDATE courier_table SET courier_name = '{new_courier_name}' WHERE courier_id = '{select_id}';")
        print('Would you like to change the couriers phone number? Y / N')
        warning_input_2 = input('')
        if warning_input_2.lower() == "y":
            print('Enter a new phone number for courier: ')
            new_courier_num = int(input(''))
            cursor.execute(f"UPDATE courier_table SET courier_num = '{new_courier_num}' WHERE courier_id = '{select_id}';")
        else: 
            courier_menu()
        warning_input = input('WARNING: you are about to edit a courier, continue? Y / N ')
        if warning_input.lower() == "y":
            connection.commit()
            courier_menu()
        else: 
            courier_menu()
    elif option == 4:
        cursor.execute("SELECT courier_id, courier_name FROM courier_table;")
        for item in cursor:
            print(item)
        select_id = input('Enter the courier ID you want to delete: ')
        warning_input_1 = int(input('WARNING! Are you Sure? Y / N '))
        if warning_input_1.lower() == "y":
            cursor.execute("DELETE FROM courier_table WHERE courier_id = '{select_id}';")
            connection.commit()
            courier_menu()
        else:
            courier_menu()
    elif option == 0:
        main_menu()
    else:
        print('You entered an invalid option.')
        courier_menu()
# call main menu function to run programme
main_menu()