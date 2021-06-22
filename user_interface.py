from sweepstakes import Sweepstakes
from contestant import Contestant
from marketing_firm import Marketing_Firm

sweepstakes = Sweepstakes()
marketing_firm = Marketing_Firm()

def display_message():
    print(f"Welcome to marketing firm sweepstakes.")
    print("Press -1- to display marketing firm menu.")
    print("Press -2- to display sweepstakes.")
    user_selection = get_user_input_number(input("Please enter a number here:"))
    if user_selection == 1:
        return display_marketing_firm_menu_options()
    elif user_selection == 2:
        return display_sweepstakes_selection_menu()


def get_user_input_string(user_input):
    if user_input == "":
        return user_input


def get_user_input_number(user_selection):
    if user_selection == int():
        return user_selection
    else:
        print("Please pick a number.")
        return get_user_input_number()


def display_contestant_info(contestant):
    print(f"There are {len(sweepstakes.contestants)}.")
    for contestant in sweepstakes.view_contestants():
        print(f"{contestant.contestant_first_name} {contestant.contestant_last_name}, {contestant.contestant_email}, {contestant.add_registration_number()}")


def display_sweepstakes_info(sweepstakes):
    print(f"{sweepstakes.Sweepstakes} sweepstakes.")
    print(f"{sweepstakes.Sweepstakes} has {len(sweepstakes.contestants)}")


def display_sweepstakes_selection_menu(sweepstakes_storage):
    print("Sweepstakes menu:")
    print(f"{marketing_firm.sweepstakes_storage}")
    sweepstakes_name = input("Please enter sweepstakes name.")
    return display_sweepstakes_menu_options(sweepstakes_name)


def display_marketing_firm_menu_options(marketing_firm_name):
    marketing_firm_name = input("Please enter Marketing Firm's name.")
    print(f"{marketing_firm_name} menu:")
    print("Enter -1- to create a sweepstakes.")
    print("Enter -2- to change the marketing firm name. ")
    print("Enter -3- to select a sweepstakes. ")
    user_selection = get_user_input_number(input("Please enter a number here:"))
    if user_selection == 1:
        return marketing_firm.create_sweepstakes()
    elif user_selection == 2:
        return marketing_firm.change_marketing_firm_name()
    elif user_selection == 3:
        print(marketing_firm.sweepstakes_storage)
        return marketing_firm.select_sweepstakes()


def display_sweepstakes_menu_options(sweepstakes_name):
    print(f"{sweepstakes_name} menu:")
    print(f"{display_sweepstakes_info()}")
    print("Enter -1- to register a contestant.")
    print("Enter -2- to view contestants. ")
    print("Enter -3- to select a winner. ")
    user_selection = get_user_input_number(input("Please enter a number here:"))
    if user_selection == 1:
        contestant = Contestant(first_name=input("Please enter first name."), last_name=input("Please enter last name."), email=input("Please enter email address."))
        return sweepstakes.register_contestant(contestant)
    elif user_selection == 2:
        return sweepstakes.view_contestants()
    elif user_selection == 3:
        return sweepstakes.pick_winner()