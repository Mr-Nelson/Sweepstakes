import random
from user_interface import UserInterface
from contestant import Contestant

class Sweepstakes:


    def __init__(self, name):
        self.sweepstakes_name = name
        self.contestants = {}
        contestant = Contestant()

    def register_contestant(self, contestant):
        self.contestants.update(self.get_registration_number(contestant))

    def get_registration_number(self, contestant):
        contestant.contestant_registration_number = 10000
        for contestant in self.contestants:
            contestant.contestant_registration_number += 1

    def pick_winner(self):
        is_winner = random.randint(self.contestants)
        return is_winner

    def view_contestants(self):
        return self.contestants

    def menu(self):
        self.register_contestant()
        self.view_contestants()
        self.pick_winner()
