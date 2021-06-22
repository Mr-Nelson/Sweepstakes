import user_interface
from sweepstakes import Sweepstakes


class Marketing_Firm:

    def __init__(self, name):
        self.marketing_firm_name = name
        self.sweepstakes_storage = []

    marketing_firm_name = input("Please enter Marketing Firm's name.")

    def create_sweepstakes(self):
        sweepstakes = Sweepstakes()
        self.sweepstakes_storage.append(user_interface.get_user_input_string())

    def change_marketing_firm_name(self):
        self.marketing_firm_name = user_interface.get_user_input_string()

    def select_sweepstakes(self):
        print(self.sweepstakes_storage)
        chosen_sweepstakes = user_interface.get_user_input_number()
        return chosen_sweepstakes

    def menu(self):
        self.create_sweepstakes()
        self.change_marketing_firm_name()
        self.select_sweepstakes()