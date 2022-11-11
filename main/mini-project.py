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

import csv
order_status = ["Preparing", "Out for Delivery", "Complete"]
cust_cart = []
cust_dict = {}
order_list = []
with open('../exports/courier_list.csv') as b: # open product_list.csv and create variable for it
        reader = csv.DictReader(b) # create read varaible using csv import function with file
        courier_list = dict(reader)
with open('../exports/product_list.csv') as f: # open product_list.csv and create variable for it
        reader = csv.DictReader(f) # create read varaible using csv import function with file
        product_list = dict(reader) # set variable product_list as the variable to call when displaying the data in that file
product_list = [{"Name":"Coffee","Price":0.85}, {"Name":"Tea","Price":0.85}, {"Name":"Orange Juice","Price":0.85}];# list of products
courier_list = [{"Name" : "John", "Phone" : "69696969696"} ]

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

    if option == 1: # if option is to view products
        product_menu()
    elif option == 2: # if option is to look at couriers
        order_menu()
        pass
    elif option == 3: # if option is to update order status
        courier_menu()
        pass
    elif option == 0:
        product_output_file = open('../exports/product_list.csv', 'w+') # exports a file called product_list.csv to exports folder, makes the file if there isnt already a csv file
        datawriter = csv.writer(product_output_file) # uses data writer function from csv import to output the file
        datawriter.writerow(product_list) # uses product_list variable to grab list and write to the file, using  witerow instead of writerows
        product_output_file.close()
        courier_output_file = open('../exports/courier_list.csv', 'w+')
        datawriter = csv.writer(courier_output_file)
        datawriter.writerow(courier_list)
        courier_output_file.close()
        print('Programme exporting to files...') # print to user that the programme is exporting changed data to a file
        print('Programme Closing...') # print to user that programme is closing
        print('')
        exit() # exit the programme
        
    else: # anything else do this
        print('')
        print('Invalid Input. ') # print that the user has inputted an invalid option
        print('')
        main_menu() # reopen the menu 
        
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
    print(f'You entered option {option}')   # user inputs option
    if option == 1:   # if option is equal to the input of 1
        print(product_list)   # print all items in list
        product_menu()    # go back to products page
    elif option == 2:   # if option is equal to the input of 2
        print(product_list)
        list_add_product = input('Enter Product: ') # input from user with name of product to add to list
        list_add_product_price = input('Enter Product Price: ')
        add_to_product_bit = {}
        add_to_product_bit['Name'] = list_add_product
        add_to_product_bit["Price"] = list_add_product_price
        product_list.append(add_to_product_bit)
        product_menu()
    elif option == 3:   # if option is equal to the input of 3
        print([list((i, product_list[i]))for i in range(len(product_list))]) # prints current list
        product_list_get_index = input('Enter product index Value: ')
        print('WARNING: You are about to delete a product, continue? Y / N')
        warning_input = input('')
        if warning_input == "Y" or "y":
            product_list.pop(int(product_list_get_index)) # removes inputed product from user from the list
            product_menu() # same issue as append section
        else:
            product_menu()
    elif option == 4: # if option is equal to the input 4
        print([list((i, product_list[i]))for i in range(len(product_list))])
        get_product_list_index = int(input('Enter Product index value: '))
        list_add_product = input('Enter Product: ') # input from user with name of product to update in list
        list_add_product_price = input('Enter Product Price: ')
        print('WARNING: you are about to add a product, continue? Y / N')
        warning_input = input('')
        if warning_input == "Y" or "y":
            product_list[get_product_list_index]['Name'] = list_add_product
            product_list[get_product_list_index]["Price"] = list_add_product_price
            product_menu()
        else: 
            product_menu()
    elif option == 0:   # if option is equal to the input of 0
        main_menu()   # go back to main menu
    else: # anything else inputted
        print('') 
        print('Invalid Input.') # print that the user has inputted an invalid option
        print('')
        product_menu() # re run the product menu function
        
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
    print(f'You entered option {option}')  # user inputs option
    print('')
    if option == 1:
        print(order_list)
        order_menu()
    elif option == 2:
        for i in range(1):
            print('Enter name below.')
            cust_name = input('')
            print('Enter address below.')
            cust_addr = input('')
            print('Enter phone number below.')
            cust_phone = input('')
            print([list((i, product_list[i]))for i in range(len(product_list))])
            cust_order = input('Enter products to add to oder with commas seperating the values: ')
            cust_order = str(cust_order)
            print([list((i, courier_list[i]))for i in range(len(courier_list))])
            courier_select = input('Enter courier to use for order: ')
            print('Place order  Y / N')
            validate = input('')
            if validate == 'y':
                cust_dict = {'Name' :cust_name, 'Address' : cust_addr, 'Number' : cust_phone,'products' : cust_order, 'Courier' : courier_list[courier_select],'status' : order_status[0]}
                order_list.append(cust_dict)
            else:
                order_menu()
        order_menu()
    elif option == 3:
        for x in range(1):
            print([list((i, order_list[i]))for i in range(len(order_list))])
            print('Input index value below to change.')
            odiv = int(input(''))
            print([list((i, order_status[i]))for i in range(len(order_status))])
            print('0 = preparing, 1 = out for delivery, 2 = complete')
            osiv = int(input(''))
            order_list[odiv]['status'] = order_status[osiv]
            order_menu()
        else:
            order_menu()
        order_menu()
    elif option == 4:
        print([list((i, order_list[i]))for i in range(len(order_list))])
        print('Enter below the order to remove.')
        order_del = int(input(''))
        print(order_del)
        order_list.remove(order_list[order_del])
        order_menu()
    elif option == 0:
        main_menu()
        
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
    print(f'You entered option {option}')  # user inputs option
    print('')
    if option == 1:
        print(courier_list)
        courier_menu()
    elif option == 2:
        add_courier_name = input('Enter courier name: ')
        add_courier_num = input('Enter courier number: ')
        print('WARNING: you are about to add a courier, continue? Y / N')
        warning_input = input('')
        if warning_input == "Y" or "y":
            add_to_courier_bit = {}
            add_to_courier_bit['Name'] = add_courier_name
            add_to_courier_bit["Phone"] = add_courier_num
            courier_list.append(add_to_courier_bit)
            print(courier_list)
            courier_menu()
        else: 
            courier_menu()
    elif option == 3:
        print([list((i, courier_list[i]))for i in range(len(courier_list))])
        get_product_list_index = int(input('Enter Courier index value: '))
        update_in_list = input('Enter a courier to update: ')
        update_value = input('Enter a courier to update it with: ')
        print('WARNING: you are about to add a courier, continue? Y / N')
        warning_input = input('')
        if warning_input == "Y" or "y":
            courier_list[get_product_list_index]['Name'] = update_in_list
            courier_list[get_product_list_index]["Phone"] = update_value
            courier_menu()
        else: 
            courier_menu()
    elif option == 4:
        print([list((i, courier_list[i]))for i in range(len(courier_list))]) # prints current list
        courier_list_get_index = input('Enter product index Value: ')
        print('WARNING: You are about to delete a courier, continue? Y / N')
        warning_input = input('')
        if warning_input == "Y" or "y":
            product_list.pop(int(courier_list_get_index)) # removes inputed product from user from the list
            courier_menu() # same issue as append section
        else:
            courier_menu()
    elif option == 0:
        main_menu()
    else:
        print('You entered an invalid option.')
        courier_menu()
main_menu()