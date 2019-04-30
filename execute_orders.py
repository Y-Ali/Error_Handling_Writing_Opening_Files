from order_write import *

# #Creating a list and calling the function to write
# order_list = ["fries", "Big Mac", "Lamb Chops", "Steak" ]
# write_my_order_from_list("order.txt",order_list)
#
# #Creating a string and calling the function to write
# order_string = "banana shake"
# write_my_order_from_string("order.txt", order_string)
#
# #Creating a dictionary and calling the function to write
# order_dictionary = {"item": "apples",
#                     "price": 14}
#
# write_my_order_from_dictionary("order.txt",order_dictionary)

#Creating a list of dictionaries and calling the functions to write
order_list_of_dictionaries = [ {'item': 'Spare Ribs','price': 14},
                               {'item': 'Portobello Mushroms', 'price': 10},
                               {'item': 'Lasagna','price': 13} ]

write_order_from_list_of_dictionaries("order.txt", order_list_of_dictionaries)