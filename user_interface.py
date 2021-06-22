import marketing_firm
import sweepstakes
from contestant import Contestant
from marketing_firm import Marketing_Firm



@staticmethod()
    def display_message():
        print(f"Welcome to {Marketing_Firm}'s sweepstakes.")
        print(f"Press -1- to display marketing firm menu.")
        print(f"Press -2- to display sweepstakes menu.")
        user_selection = get_user_input_number(prompt=input("Please enter a number here:"))
        if user_selection == 1:
            return display_marketing_firm_menu_options()
        elif user_selection == 2:
            return display_sweepstakes_selection_menu()
        else:
            print("Please choose a number.")
            return display_message()

@staticmethod()
    def get_user_input_string(prompt):
        user_input = prompt(input())
        return user_input

@staticmethod()
    def get_user_input_number(prompt):
        try:
            user_number_input = prompt(int(input()))
            return user_number_input
        except:
            print("Please pick a number.")
            return get_user_input_number()

@staticmethod()
    def display_contestant_info(contestant):
        print(f"There are {len(sweepstakes.Sweepstakes.contestants)}.")
        for each_contestant in sweepstakes.Sweepstakes.view_contestants:
            print(f"{Contestant.contestant_first_name} {Contestant.contestant_last_name}, {Contestant.contestant_email}, {Contestant.contestant_registration_number}")

@staticmethod()
    def display_sweepstakes_info(sweepstakes):
        print(f"{sweepstakes.Sweepstakes} sweepstakes.")
        print(f"{sweepstakes.Sweepstakes} has {len(sweepstakes.Sweepstakes.contestants)}")

@staticmethod()
    def display_sweepstakes_selection_menu(all_sweepstakes):
        print(f"Sweepstakes menu:")
        print(f"{sweepstakes.Sweepstakes.menu}")
        return display_sweepstakes_menu_options()

@staticmethod()
    def display_marketing_firm_menu_options(marketing_firm_name):
        print(f"{Marketing_Firm} menu:")
        print("Enter -1- to create a sweepstakes.")
        print("Enter -2- to change the marketing firm name. ")
        print("Enter -3- to select a sweepstakes. ")
        user_selection = get_user_input_number(prompt=input("Please enter a number here:"))
        if user_selection == 1:
            return marketing_firm.Marketing_Firm.create_sweepstakes()
        elif user_selection == 2:
            return marketing_firm.Marketing_Firm.change_marketing_firm_name()
        elif user_selection == 3:
            return marketing_firm.Marketing_Firm.select_sweepstakes()
        else:
            print("Please choose a number.")
            return display_message()


@staticmethod()
    def display_sweepstakes_menu_options(sweepstakes_name):
        print(f"{sweepstakes.Sweepstakes} menu:")
        print("Enter -1- to register a contestant.")
        print("Enter -2- to view contestants. ")
        print("Enter -3- to select a winner. ")
        user_selection = get_user_input_number(prompt=input("Please enter a number here:"))
        if user_selection == 1:
            return sweepstakes.Sweepstakes.register_contestant()
        elif user_selection == 2:
            return sweepstakes.Sweepstakes.view_contestants()
        elif user_selection == 3:
            return sweepstakes.Sweepstakes.pick_winner()
        else:
            print("Please choose a number.")
            return display_message()