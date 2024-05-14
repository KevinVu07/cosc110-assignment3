import sys

# a dictionary to store burger orders and how many times each order was made
burger_order_dict = {}


def main():
    # read file orders.txt, check if key burger_order has been in burger_order_dict or not. If not, add key burger_order in with value of 1. If the key already in the dict, increase the value by 1.
    try:
        with open("orders.txt") as file:
            for line in file:
                burger_order = convert_to_tuple(line)
                if burger_order == None:
                    sys.exit()
                if burger_order not in burger_order_dict:
                    burger_order_dict[burger_order] = 1
                else:
                    burger_order_dict[burger_order] += 1
    except FileNotFoundError:
        sys.exit(
            "Error in reading file. Please double check the filepath or if the file existed."
        )

    # sort the burger_order_dict by values, return a sorted_burger_order_list with elements being the lists contain element 0 - key (burger_order tuple) and element 1 - value (how many time each order was made)
    sorted_burger_order_list = sorted(
        sorted(burger_order_dict.items()), key=lambda x: x[1], reverse=True
    )

    # get number of top common orders to display via input from user
    orders_to_display = 0
    while orders_to_display <= 0:
        while True:
            try:
                orders_to_display = int(
                    input(
                        "How many of the top burger orders would you like to output? "
                    )
                )
                break
            except ValueError:
                print("Invalid value. Please enter a positive integer")
        if orders_to_display > 0:
            break
        print("Invalid value. Please enter a positive integer")

    # display the top common orders based on how many top burger orders the user would like to see
    print("The top burger orders were:")
    displayTopOrders(orders_to_display, sorted_burger_order_list)


def displayTopOrders(orders_to_display, order_list):
    """
    output the top common orders based on how many top orders user would like to see

    parameters:
        - orders_to_display: number of top common orders to display from the user input
        - order_list: the sorted order list containing the lists of burger orders and how many time the orders were made

    returns:
        none. output the burger order, number of time it was ordered, and the burger cost to the screen
    """

    # if the orders_to_display input from the user greater than the length of the order_list, set the orders_to_display equal the length of the order list, else keep the same order_to_display unchanged
    orders_to_display = (
        len(order_list) if orders_to_display >= len(order_list) else orders_to_display
    )

    # iterate from index 0 to index (orders_to_display - 1), display the elements from the top (0) in the sorted order_list
    for i in range(orders_to_display):
        burger_order = order_list[i][0]
        burger_cost = get_cost(burger_order)
        number_of_order = order_list[i][1]
        print(f"{burger_order}\t{number_of_order}\t${burger_cost}")


def convert_to_tuple(line):
    """
    reading data from orders.txt, return a tuple with entries:
    bun: milk / gluten free
    sauce: tomato / barbecue / none
    number_of_patties: integer
    number_of_cheese_slices: integer
    has_tomato: True / False
    has_lettuce: True / False
    has_onion: True / False

    parameters:
        - line: a line read from the dataset orders.txt, representing an order made
    """

    # extract the values within the line to each entries in the tuple
    try:
        (
            bun,
            sauce,
            number_of_patties,
            number_of_cheese_slices,
            has_tomato,
            has_lettuce,
            has_onion,
        ) = (
            line.strip().lower().split(",")
        )
    except ValueError:
        print(
            "Error reading data. Please ensure each line of orders.txt starts with the bun type (milk or gluten free), followed by a comma, then the sauce type (tomato, barbecue or none), followed by a comma, then the number of patties (0-3), followed by a comma, then the number of slices of cheese (0-3), followed by a comma, then whether tomato is included (yes or no), followed by a comma, then whether lettuce is included (yes or no), followed by a comma, then whether onion is included (yes or no)."
        )
        # return None if encounter any error converting the data to tuple entries
        return None

    # convert the integer elements to int type from string
    try:
        number_of_patties = int(number_of_patties)
    except ValueError:
        print(
            "The data for number of patties must be an integer. Please double check the dataset."
        )
        return None

    # convert the integer elements to int type from string
    try:
        number_of_cheese_slices = int(number_of_cheese_slices)
    except ValueError:
        print(
            "The data for number of cheese slices must be an integer. Please double check the dataset."
        )
        return None

    # convert boolean entries from string to appropriate boolean
    if has_tomato == "yes":
        has_tomato = True
    elif has_tomato == "no":
        has_tomato = False

    if has_lettuce == "yes":
        has_lettuce = True
    elif has_lettuce == "no":
        has_lettuce = False

    if has_onion == "yes":
        has_onion = True
    elif has_onion == "no":
        has_onion = False

    # convert back the entries to a tuple variable
    burger_order = (
        bun,
        sauce,
        number_of_patties,
        number_of_cheese_slices,
        has_tomato,
        has_lettuce,
        has_onion,
    )

    # return the tuple variable
    return burger_order
    # return None if error converting line to tuple


def get_cost(burger_order):
    """
    determine the cost of a burger via the burger order tuple passed in as a parameter

    parameters:
        - burger_order: the tupe value containing entries for a burger order made
    returns:
        cost of burger as integer
    """

    # extracting the tupe variable burger_order to individual entries for the burger order
    (
        bun,
        sauce,
        number_of_patties,
        number_of_cheese_slices,
        has_tomato,
        has_lettuce,
        has_onion,
    ) = burger_order

    # a list of all possible number of meat patties
    number_of_patties_list = [0, 1, 2, 3]

    # a list of all possible number of cheese slices
    number_of_cheese_slices_list = [0, 1, 2, 3]

    # the base cost of a burger
    total_cost = 5

    # Check each ingredient input and increase the total cost accordingly if there is extra ingredients from the base burger
    # extra cost for gluten free bun
    if bun == "gluten free":
        total_cost += 1

    if number_of_patties not in number_of_patties_list:
        sys.exit(
            f"The number of patties is invalid for one of the burger order. The patties can only be one of these values: {number_of_patties_list}"
        )

    # extra cost for extra patties
    if number_of_patties > 1:
        number_of_extra_patties = number_of_patties - 1
        total_cost = total_cost + (number_of_extra_patties * 3)

    if number_of_cheese_slices not in number_of_cheese_slices_list:
        sys.exit(
            f"The number of cheese slices is invalid for one of the burger order. The cheese slices can only be one of these values: {number_of_cheese_slices_list}"
        )

    # extra cost for extra cheese slices
    if number_of_cheese_slices > 1:
        number_of_extra_cheese_slices = number_of_cheese_slices - 1
        total_cost = total_cost + (number_of_extra_cheese_slices * 1)

    # list of boolean salad choices
    salad_choices = [has_tomato, has_lettuce, has_onion]

    # extra cost for extra salad choices
    if all(salad_choices):
        total_cost += 2
    elif salad_choices.count(True) == 2:
        total_cost += 1

    # return final total cost of the burger
    return total_cost


if __name__ == "__main__":
    main()
