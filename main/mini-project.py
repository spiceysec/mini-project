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
product_list = ["Apple", "Sandwhich", "Coffee", "Tea", "Chocolate Cake", "Cheese Cake", "Orange"] # list of products
with open('../exports/product_list.csv') as f: # open product_list.csv and create variable for it
        reader = csv.reader(f) # create read varaible using csv import function with file
        product_list = list(reader) # set variable product_list as the variable to call when displaying the data in that file

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
    elif option == 5: # if option is to update order status
        #oder_log_menu()
        pass
    elif option == 0:
        output_file = open('../exports/product_list.csv', 'w+') # exports a file called product_list.csv to exports folder, makes the file if there isnt already a csv file
        datawriter = csv.writer(output_file) # uses data writer function from csv import to output the file
        datawriter.writerow(product_list) # uses product_list variable to grab list and write to the file, using  witerow instead of writerows
        output_file.close() # closes the file after writing
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
        list_add_product = input('Enter Product: ') # input from user with name of product to add to list
        print(list_add_product)     # print list (just to test)
        product_list.append(list_add_product)
        print(product_list) # prints product list
        product_menu() # issue here, when adding something to list and this function is reloaded, the item in list is reset and no longer is appended
    elif option == 3:   # if option is equal to the input of 2
        print(product_list) # prints current list
        list_del_product = input('Enter a product to delete: ') # user enteres the product from the list to remove from the list
        product_list.remove(str(list_del_product)) # removes inputed product from user from the list
        product_menu() # same issue as append section
    elif option == 4: # if option is equal to the input 4
        print(product_list) # print product list
        update_in_list = input('Enter a product to update: ') # user to input a name of product to update
        update_value = input('Enter a product to update it with: ') # user to input the product that is updated version
        product_list.remove(str(update_in_list))
        product_list.append(update_value)
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
            print('Place order  Y / N')
            validate = input('')
            if validate == 'y':
                cust_dict = {'Name' :cust_name, 'Address' : cust_addr, 'Number' : cust_phone, 'status' : order_status[0]}
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
main_menu()