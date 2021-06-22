from sweepstakes import Sweepstakes


class Contestant:

    def __init__(self, first_name, last_name, email):
        self.contestant_first_name = first_name
        self.contestant_last_name = last_name
        self.contestant_email = email
        self.contestant_registration_number = 0

    def add_registration_number(self, contestant):
        sweepstakes = Sweepstakes()
        self.contestant_registration_number = 10000
        for contestant in sweepstakes.contestants():
            self.contestant_registration_number += 1

    def notify(self, is_winner):
        is_winner = False
        if is_winner:
            pass
        else:
            pass