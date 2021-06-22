import user_interface
from sweepstakes import Sweepstakes


class Marketing_Firm:

    def __init__(self, name):
        self.marketing_firm_name = name
        sweepstakes_storage = []

    def create_sweepstakes(self):
        pass

    def change_marketing_firm_name(self):
        pass

    def select_sweepstakes(self):
        pass

    def menu(self):
        self.create_sweepstakes()
        self.change_marketing_firm_name()
        self.select_sweepstakes()