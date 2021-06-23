from user_interface import UserInterface
from sweepstakes import Sweepstakes


class MarketingFirm:

    def __init__(self, name):
        self.marketing_firm_name = name
        self.sweepstakes_storage = []


    def create_sweepstakes(self):
        self.sweepstakes_storage.append(UserInterface.get_user_input_string())

    def change_marketing_firm_name(self):
        self.marketing_firm_name = UserInterface.get_user_input_string()

    def select_sweepstakes(self):
        chosen_sweepstakes = UserInterface.get_user_input_number()
        return chosen_sweepstakes

    def menu(self):
        self.create_sweepstakes()
        self.change_marketing_firm_name()
        self.select_sweepstakes()