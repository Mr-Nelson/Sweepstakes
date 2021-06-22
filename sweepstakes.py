import random
import user_interface
from contestant import Contestant


class Sweepstakes:

    def __init__(self, name):
        self.sweepstakes_name = name
        self.contestants = {}

    def register_contestant(self, contestant):
        Contestant.contestant_first_name
        Contestant.contestant_last_name
        Contestant.contestant_email
        Contestant.add_registration_number()

    def pick_winner(self):
        is_winner = random.randrange(self.contestants)

    def view_contestants(self):
        pass

    def menu(self):
        self.register_contestant()
        self.view_contestants()
        self.pick_winner()