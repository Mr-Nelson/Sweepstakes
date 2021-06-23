from contestant import Contestant


class UserInterface:

    @staticmethod
    def display_message():
        print(f"Welcome to marketing firm sweepstakes.")
        print("Press -1- to display marketing firm menu.")
        print("Press -2- to display sweepstakes.")
        user_selection = UserInterface.get_user_input_number(input("Please enter your selection here:"))
        if user_selection == 1:
            return UserInterface.display_marketing_firm_menu_options()
        elif user_selection == 2:
            return UserInterface.display_sweepstakes_selection_menu()


    @staticmethod
    def get_user_input_string(user_input):
        if user_input == "":
            return user_input

    @staticmethod
    def get_user_input_number(user_selection):
        if user_selection == int():
            return user_selection
        else:
            print("Please pick a number.")
            return UserInterface.get_user_input_number(user_selection)

    @staticmethod
    def display_contestant_info(sweepstakes):
        print(f"There are {len(sweepstakes.contestants)}.")
        for contestant in sweepstakes.view_contestants():
            print(f"{contestant.contestant_first_name} {contestant.contestant_last_name}, {contestant.contestant_email}, {contestant.contestant_registration_number()}")

    @staticmethod
    def display_sweepstakes_info(sweepstakes_name, contestants):
        print(f"{sweepstakes_name} sweepstakes.")
        print(f"{sweepstakes_name} has {len(contestants)}")

    @staticmethod
    def display_sweepstakes_selection_menu(sweepstakes_storage):
        print("Sweepstakes menu:")
        print(f"{sweepstakes_storage}")
        sweepstakes_name = UserInterface.get_user_input_string(input("Please enter sweepstakes name."))
        return UserInterface.display_sweepstakes_menu_options(sweepstakes_name)

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm):
        marketing_firm_name = UserInterface.get_user_input_string(input("Please enter Marketing Firm's name."))
        print(f"{marketing_firm_name} menu:")
        print("Enter -1- to create a sweepstakes.")
        print("Enter -2- to change the marketing firm name. ")
        print("Enter -3- to select a sweepstakes. ")
        user_selection = UserInterface.get_user_input_number(input("Please enter a number here:"))
        if user_selection == 1:
            return marketing_firm.create_sweepstakes()
        elif user_selection == 2:
            return marketing_firm.change_marketing_firm_name()
        elif user_selection == 3:
            print(marketing_firm.sweepstakes_storage)
            return marketing_firm.select_sweepstakes()

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes):
        print(f"{sweepstakes.sweepstakes_name} menu:")
        print(f"{UserInterface.display_sweepstakes_info(sweepstakes.sweepstakes_name)}")
        print("Enter -1- to register a contestant.")
        print("Enter -2- to view contestants. ")
        print("Enter -3- to select a winner. ")
        user_selection = UserInterface.get_user_input_number(input("Please enter a number here:"))
        if user_selection == 1:
            contestant = Contestant(first_name=input("Please enter first name."), last_name=input("Please enter last name."), email=input("Please enter email address."))
            sweepstakes.register_contestant(contestant)
        elif user_selection == 2:
            return UserInterface.display_contestant_info(sweepstakes)
        elif user_selection == 3:
            return sweepstakes.pick_winner()