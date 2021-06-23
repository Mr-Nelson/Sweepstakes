from user_interface import UserInterface


class MarketingFirm:

    def __init__(self, name):
        self.marketing_firm_name = UserInterface.get_user_input_string("Please enter Marketing Firm's name.")
        self.sweepstakes_storage = []

    def change_marketing_firm_name(self):
        self.marketing_firm_name = UserInterface.get_user_input_string("Enter marketing firm's name.")

    def create_sweepstakes(self):
        self.sweepstakes_storage.append(UserInterface.get_user_input_string("Enter sweepstakes name."))

    def select_sweepstakes(self):
        chosen_sweepstakes = (UserInterface.get_user_input_string("Make a selection."))
        return chosen_sweepstakes

    def menu(self):
        user_selection = UserInterface.get_user_input_number("Please make a selection.")
        if user_selection == 1:
            return self.create_sweepstakes()
        elif user_selection == 2:
            return self.change_marketing_firm_name()
        elif user_selection == 3:
            print(self.sweepstakes_storage)
            return self.select_sweepstakes()