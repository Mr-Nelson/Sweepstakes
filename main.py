from user_interface import UserInterface
from marketing_firm import MarketingFirm
from sweepstakes import Sweepstakes


if __name__ == '__main__':
    UserInterface.display_message("\t\tWelcome to marketing firm sweepstakes.\t\t \tPress -1- to display marketing firm menu.\t \tPress -2- to display sweepstakes.\t")
    user_selection = UserInterface.get_user_input_number("Please enter your selection here:")
    if user_selection == 1:
        MarketingFirm.menu(MarketingFirm)
    elif user_selection == 2:
        try:
            Sweepstakes.menu(UserInterface.display_sweepstakes_selection_menu())
        except TypeError:
            print("There are no sweepstakes entered at this time.")