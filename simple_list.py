list = []

def provide_options():
    print("To proceed, choose from the options below and press ENTER:")
    print("\t[1] to add an item to the list")
    print("\t[2] to remove an item from the list")
    print("\t[3] to sort the list")
    print("\t[4] to show all your items in the list")
    print("\t[5] to stop the program\n")

def show_items_in_list():
    if (len(list) < 1):
        print("You don't have any items in the list. Please add an item first.")
    else:
        print(f"Here's what you have in the list now:")
        for index in range(1, len(list)+1):
            print(f"[{index}] - {list[index-1].capitalize()}")

def get_user_input():
    return input("What do you want to add to the list: ")

def clean_user_input(str):    
    return str.strip().lower()

def remove_item_from_list(index):
    index = index - 1
    if index < 0 or index > len(list) - 1:
        print("This item is not in the list!")
    else:
        del list[index]
        print("Done!\n")

def start_program():
    print("Hello! Welcome to \"Simple List App\"!\n")

    while True:
        provide_options()
        action = input("What do you want to do? ")
        
        print()

        if action == "1":
            # Get user input, then clean it, and then add to the list
            str = get_user_input()
            str = clean_user_input(str)
            list.append(str)
            print("Done!")
        
        elif action == "2":
            show_items_in_list()
            index_of_item_to_remove = input("\nWhich item to remove? ")
            remove_item_from_list(int(index_of_item_to_remove))

        elif action == "3":
            print("How do you want to sort the list?")
            print("\t[1] to sort in ascending order")
            print("\t[2] to sort in descending order")
            sort_option = input("Answer: ")
            if sort_option == "1":
                list.sort()
            elif sort_option == "2":
                list.sort(reverse=True)
            else:
                print("Invalid option!\n")
                continue

            print("Done!")

        elif action == "4":
            show_items_in_list()
        
        elif action == "5":
            print("Thank you for using \"Simple List\" app. Have a great day ahead!\n")
            break

        print()


start_program()