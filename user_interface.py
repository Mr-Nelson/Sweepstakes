class UserInterface:

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_user_input_string(prompt):
        user_input = (input(prompt))
        return user_input

    @staticmethod
    def get_user_input_number(prompt):
        try:
            user_selection = int(input(prompt))
            return user_selection
        except ValueError:
            print("Please pick a number.")
            return UserInterface.get_user_input_number(prompt)

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
        sweepstakes_name = UserInterface.get_user_input_string("Please enter sweepstakes name.")
        return UserInterface.display_sweepstakes_menu_options(sweepstakes_name)

    @staticmethod
    def display_marketing_firm_menu_options(marketing_firm_name):
        print(f"{marketing_firm_name} menu:")
        print("Enter -1- to create a sweepstakes.")
        print("Enter -2- to change the marketing firm's name. ")
        print("Enter -3- to select a sweepstakes. ")

    @staticmethod
    def display_sweepstakes_menu_options(sweepstakes):
        print(f"{sweepstakes.sweepstakes_name} menu:")
        print(f"{UserInterface.display_sweepstakes_info()}")
        print("Enter -1- to register a contestant.")
        print("Enter -2- to view contestants. ")
        print("Enter -3- to select a winner. ")

