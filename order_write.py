def write_my_order_from_string(file_name,order):
    try:
        with open (file_name, "a") as file:
                file.write(order + "\n")

    except FileNotFoundError as errmsg:
        print("No file to write on. Check naming.")
        raise

def write_my_order_from_list(file_name, order):
    try:
        with open(file_name, "a") as file:
            for food_item in order:
                file.write(food_item + "\n")

    except FileNotFoundError as errmsg:
        print("No file to write on. Check naming.")
        raise

def write_my_order_from_dictionary(file_name,order_dictionary):
    try:
        with open (file_name, "a") as file:
            for key in order_dictionary.keys():
                #print(order_dictionary[key])
                string_to_save = str(key) + ": " + str(order_dictionary[key])

                #print(string_to_save)
                file.write(string_to_save + "\n")

    except FileNotFoundError as errmsg:
        print("No file to write on. Check naming.")
        raise

def write_order_from_list_of_dictionaries(file_name, order_list_dict):
    try:
        with open(file_name, "a") as file:
            # write a block of code to:
                # 1. iterate over the list to just get one item

            for item in order_list_dict:
                #print(order_dictionary[key])

                # 2. iterate over the dictionary to get the key and values
                for dict_item in item.keys():
                    string_to_save2 = str(dict_item) + ": " + str(item[dict_item])
                    print(string_to_save2)

                    file.write(string_to_save2 + "\n")


                        # create a string
                        # save the string


    except FileNotFoundError as errmsg:
        print("No file to write on. Check naming.")
        raise
