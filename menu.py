from tkinter import *
from tkinter import ttk
from time import time


byte_burger = {
    "burger_name": "Byte Burger",
    "bun_type": "Milk",
    "sauce_type": "Tomato",
    "number_of_patties": 1,
    "number_of_cheese_slices": 0,
    "tomato_included": False,
    "lettuce_included": True,
    "onion_included": False,
}

ctrl_alt_delicious = {
    "burger_name": "Ctrl-Alt-Delicious",
    "bun_type": "Milk",
    "sauce_type": "Barbecue",
    "number_of_patties": 2,
    "number_of_cheese_slices": 2,
    "tomato_included": True,
    "lettuce_included": True,
    "onion_included": True,
}

data_crunch = {
    "burger_name": "Data Crunch",
    "bun_type": "Gluten Free",
    "sauce_type": "Tomato",
    "number_of_patties": 0,
    "number_of_cheese_slices": 0,
    "tomato_included": True,
    "lettuce_included": True,
    "onion_included": True,
}

code_cruncher = {
    "burger_name": "Code Cruncher",
    "bun_type": "Milk",
    "sauce_type": "Tomato",
    "number_of_patties": 3,
    "number_of_cheese_slices": 3,
    "tomato_included": True,
    "lettuce_included": True,
    "onion_included": True,
}

burgers_dict = {
    "Byte Burger": byte_burger,
    "Ctrl-Alt-Delicious": ctrl_alt_delicious,
    "Data Crunch": data_crunch,
    "Code Cruncher": code_cruncher,
}

cycle_job = None  # Initialize cycle_job globally


def cycle_burgers_details(initial=True):
    global current_index, cycle_job  # Declare global variables
    if initial:
        current_index = 0
        display_burger_details(list(burgers_dict.keys())[current_index])
    else:
        burger_names = list(burgers_dict.keys())
        current_index = (current_index + 1) % len(burger_names)
        display_burger_details(burger_names[current_index])
    cycle_job = root.after(5000, cycle_burgers_details, False)


# Function to handle button clicks
def button_click(burger_name):
    global cycle_job, current_index  # Declare global variables
    display_burger_details(burger_name)
    current_index = list(burgers_dict.keys()).index(burger_name)  # Update current_index
    root.after_cancel(cycle_job)  # Cancel automatic cycling
    cycle_job = root.after(
        5000, cycle_burgers_details, False
    )  # Reset automatic cycling timer


def display_burger_details(name):
    # use the burger name passed in to display the specified burger details
    # print(name)
    burger = burgers_dict[name]
    cost = get_cost(name)
    # print(burger)
    burger_display = f"Burger name: {burger['burger_name']}\n\nBun type: {burger['bun_type']}\n\nSauce type: {burger['sauce_type']}\n\nNumber of patties: {burger['number_of_patties']}\n\nNumber of slices of cheese: {burger['number_of_cheese_slices']}\n\nTomato included: {'No' if burger['tomato_included'] == False else 'Yes'}\n\nLettuce included: {'No' if burger['lettuce_included'] == False else 'Yes'}\n\nOnion included: {'No' if burger['onion_included'] == False else 'Yes'}\n\nPrice: ${cost}"
    burger_details.set(burger_display)


def get_cost(burger_name):
    """
    determine the cost of a burger via the burger name passed in as a parameter

    parameters:
        - burger_name: the name of th2  e burger clicked on by the user
    returns:
        cost of burger as integer
    """

    # extracting the burger ingredients from the burger list dictionary
    burger = burgers_dict[burger_name]
    bun_type = burger["bun_type"]
    sauce_type = burger["sauce_type"]
    number_of_patties = burger["number_of_patties"]
    number_of_cheese_slices = burger["number_of_cheese_slices"]
    has_tomato = burger["tomato_included"]
    has_lettuce = burger["lettuce_included"]
    has_onion = burger["onion_included"]

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

# Set weight for columns and rows
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="3 3 12 12", width=200, height=400)
# Configure sticky option for mainframe
mainframe.grid(column=0, row=0, sticky=(N, S))


labelframe = ttk.Frame(mainframe, width=200, height=300)
# Configure sticky option for mainframe
labelframe.grid(column=0, row=0, columnspan=4)

burger_details = StringVar()
burger_display_label = ttk.Label(labelframe, textvariable=burger_details)
# Configure widget options for burger display label
burger_display_label.grid(column=0, row=1, sticky=(E, W), columnspan=4)
burger_display_label.place(x=100, y=150, anchor=CENTER)


burger_name = StringVar()
byte_burger = ttk.Button(
    mainframe,
    text="Byte Burger",
    command=lambda name="Byte Burger": button_click(name),
)
ctrl_alt_delicious = ttk.Button(
    mainframe,
    text="Ctrl-Alt-Delicious",
    command=lambda name="Ctrl-Alt-Delicious": button_click(name),
)
data_crunch = ttk.Button(
    mainframe,
    text="Data Crunch",
    command=lambda name="Data Crunch": button_click(name),
)
code_cruncher = ttk.Button(
    mainframe,
    text="Code Cruncher",
    command=lambda name="Code Cruncher": button_click(name),
)

# Configure widget options for buttons
byte_burger.grid(column=0, row=2, sticky=(W, E))
ctrl_alt_delicious.grid(column=1, row=2, sticky=(W, E))
data_crunch.grid(column=2, row=2, sticky=(W, E))
code_cruncher.grid(column=3, row=2, sticky=(W, E))

cycle_burgers_details()

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
