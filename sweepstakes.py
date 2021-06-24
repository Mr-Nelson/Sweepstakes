import random
from contestant import Contestant
from user_interface import UserInterface


class Sweepstakes:

    def __init__(self, name):
        self.sweepstakes_name = name
        self.contestants = {}



    def register_contestant(self, contestant):
        contestant.contestant_first_name = UserInterface.get_user_input_string("Please enter first name.")
        contestant.contestant_last_name = UserInterface.get_user_input_string("Please enter last name.")
        contestant.contestant_email = UserInterface.get_user_input_string("Please enter email address.")
        contestant.contestant_registration_number = (self.get_registration_number(contestant))
        return self.menu(self)

    def get_registration_number(self, contestant):
        contestant.contestant_registration_number = 10000
        for contestant in self.contestants:
            contestant.contestant_registration_number += 1

    def pick_winner(self):
        is_winner = random.randint(self.contestants)
        Contestant.notify()
        return is_winner
        return self.menu

    def view_contestants(self):
        return UserInterface.display_contestant_info(self.contestants)
        for contestant in contestants:
            print(f"{contestant.contestant_first_name} {contestant.contestant_last_name}, {contestant.contestant_email}, {contestant.contestant_registration_number()}")
        return self.menu

    def menu(self, sweepstakes_name):
        contestant = Contestant()
        validated_user_selection = (False, None)
        UserInterface.display_sweepstakes_menu_options(sweepstakes_name)
        user_selection = UserInterface.get_user_input_number("Please make a selection.")
        while validated_user_selection[0] is False:
            if user_selection == 1:
                self.register_contestant(contestant)
            elif user_selection == 2:
                self.view_contestants()
            elif user_selection == 3:
                self.pick_winner()
        return validated_user_selection[0]