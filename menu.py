from tkinter import *
from tkinter import ttk


byte_burger = {
    "burger_name": "byte burger",
    "bun_type": "milk",
    "sauce_type": "tomato",
    "number_of_patties": 1,
    "number_of_cheese_slices": 0,
    "tomato included": False,
    "lettuce included": True,
    "onion included": False,
}

ctrl_alt_delicious = {
    "burger_name": "Ctrl-Alt-Delicious",
    "bun_type": "milk",
    "sauce_type": "barbecue",
    "number_of_patties": 2,
    "number_of_cheese_slices": 2,
    "tomato included": True,
    "lettuce included": True,
    "onion included": True,
}

data_crunch = {
    "burger_name": "Data Crunch",
    "bun_type": "gluten free",
    "sauce_type": "tomato",
    "number_of_patties": 0,
    "number_of_cheese_slices": 0,
    "tomato included": True,
    "lettuce included": True,
    "onion included": True,
}

code_cruncher = {
    "burger_name": "Code Cruncher",
    "bun_type": "milk",
    "sauce_type": "tomato",
    "number_of_patties": 3,
    "number_of_cheese_slices": 3,
    "tomato included": True,
    "lettuce included": True,
    "onion included": True,
}

burgers_list = [
    {"Byte Burger": byte_burger},
    {"Ctrl-Alt-Delicious": ctrl_alt_delicious},
    {"Data Crunch": data_crunch},
    {"Code Cruncher": code_cruncher},
]


def displayBurgerDetails(name):
    # use the burger name passed in to display the specified burger details
    print(name)


def get_cost(burger_name):
    """
    determine the cost of a burger via the burger name passed in as a parameter

    parameters:
        - burger_name: the name of the burger clicked on by the user
    returns:
        cost of burger as integer
    """

    # extracting the burger ingredients from the burger list dictionary
    burger = burgers_list[burger_name]
    bun_type = burger["bun_type"]
    sauce_type = burger["sauce_type"]
    number_of_patties = burger["number_of_patties"]
    number_of_cheese_slices = burger["number_of_cheese_slices"]
    has_tomato = burger["tomato included"]
    has_lettuce = burger["lettuce included"]
    has_onion = burger["onion included"]

    # the base cost of a burger
    total_cost = 5

    # Check each ingredient input and increase the total cost accordingly if there is extra ingredients from the base burger
    # extra cost for gluten free bun
    if bun_type == "gluten free":
        total_cost += 1

    # extra cost for extra patties
    if number_of_patties > 1:
        number_of_extra_patties = number_of_patties - 1
        total_cost = total_cost + (number_of_extra_patties * 3)

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


root = Tk()
root.title("Welcome to Codetown Burger Co")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

burger_details = ttk.Frame(mainframe)

burger_name = StringVar()
byte_burger = ttk.Button(
    mainframe,
    text="Byte Burger",
    command=lambda name="Byte Burger": displayBurgerDetails(name),
)
ctrl_alt_delicious = ttk.Button(
    mainframe,
    text="Ctrl-Alt-Delicious",
    command=lambda name="Ctrl-Alt-Delicious": displayBurgerDetails(name),
)
data_crunch = ttk.Button(
    mainframe,
    text="Data Crunch",
    command=lambda name="Data Crunch": displayBurgerDetails(name),
)
code_cruncher = ttk.Button(
    mainframe,
    text="Code Cruncher",
    command=lambda name="Code Cruncher": displayBurgerDetails(name),
)

burger_details.grid(column=0, row=1, columnspan=4, sticky=(N, E, S, W))
byte_burger.grid(column=0, row=2, sticky=(W, E))
ctrl_alt_delicious.grid(column=1, row=2, sticky=(W, E))
data_crunch.grid(column=2, row=2, sticky=(W, E))
code_cruncher.grid(column=3, row=2, sticky=(W, E))

root.mainloop()
