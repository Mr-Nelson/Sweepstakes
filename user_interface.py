from marketing_firm import Marketing_Firm
from sweepstakes import Sweepstakes
from contestant import Contestant


@staticmethod
    def display_message():
        print(f"Welcome to {Marketing_Firm}'s {Sweepstakes}.")
        print(f"Press -1- to display {Marketing_Firm} menu.")
        print(f"Press -2- to display {Sweepstakes} menu.")
        user_selection = get_user_input_number(prompt=input("Please enter a number here:"))
        return user_selection

@staticmethod
    def get_user_input_string(prompt):
        user_input = prompt(input())
        return user_input

@staticmethod
    def get_user_input_number(prompt):
        try:
            user_number_input = prompt(int(input()))
            return user_number_input
        except:
            print("Please pick a number.")
            return get_user_input_number()

@staticmethod
    def display_contestant_info(contestant):
        print(f"There are {len(Sweepstakes.contestants)}.")
        for each_contestant in Sweepstakes.view_contestants:
            print(f"{Contestant.contestant_first_name} {Contestant.contestant_last_name}, {Contestant.contestant_email}, {Contestant.contestant_registration_number}")

@staticmethod
    def display_sweepstakes_info(sweepstakes):
        print(f"{Sweepstakes} sweepstakes.")
        print(f"{Sweepstakes} has {len(Sweepstakes.contestants)}")

@staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        print(f"Sweepstakes menu:")
        print(f"{Sweepstakes.menu}")

@staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print(f"{Marketing_Firm} menu:")
        print(f"{Marketing_Firm.menu}")

@staticmethod
    def display_sweepstakes_menu_options(sweepstakes_name):
        print(f"{Sweepstakes} menu:")
        print(f"{Sweepstakes.menu}")