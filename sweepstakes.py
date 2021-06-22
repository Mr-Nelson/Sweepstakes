import random
import contestant
import user_interface


class Sweepstakes:

    def __init__(self, name):
        self.sweepstakes_name = name
        self.contestants = {}

    def register_contestant(self, user_input):
        self.contestants.update(contestant.contestant_first_name)
        self.contestants.update(contestant.contestant_last_name)
        self.contestants.update(contestant.contestant_email)
        self.contestants.update(contestant.add_registration_number())

    def pick_winner(self):
        is_winner = random.choice(self.contestants)

    def view_contestants(self):
        return self.contestants

    def menu(self):
        self.register_contestant()
        self.view_contestants()
        self.pick_winner()
