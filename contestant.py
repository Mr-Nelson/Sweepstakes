from user_interface import UserInterface


class Contestant:

    def __init__(self, first_name=UserInterface.get_user_input_string("Please enter first name."),
                       last_name=UserInterface.get_user_input_string("Please enter last name."),
                       email=UserInterface.get_user_input_string("Please enter email address.")):
        self.contestant_first_name = first_name
        self.contestant_last_name = last_name
        self.contestant_email = email
        self.contestant_registration_number = None

    def notify(self, is_winner):
        is_winner = False
        if is_winner:
            pass
        else:
            pass