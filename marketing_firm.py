import user_interface
from sweepstakes import Sweepstakes


class Marketing_Firm:

    def __init__(self, name):
        self.marketing_firm_name = name
        self.sweepstakes_storage = []
        sweepstakes = Sweepstakes()

    def create_sweepstakes(self):
        self.sweepstakes_storage.append(user_interface.get_user_input_string())

    def change_marketing_firm_name(self):
        self.marketing_firm_name = user_interface.get_user_input_string()

    def select_sweepstakes(self):
        print(self.sweepstakes_storage)
        self.select_sweepstakes = user_interface.get_user_input_number()

    def menu(self):
        self.create_sweepstakes()
        self.change_marketing_firm_name()
        self.select_sweepstakes()