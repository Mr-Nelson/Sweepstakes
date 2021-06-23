from user_interface import UserInterface

user_interface = UserInterface
user_interface.display_message()
print(f"Welcome to marketing firm sweepstakes.")
print("Press -1- to display marketing firm menu.")
print("Press -2- to display sweepstakes.")
user_selection = UserInterface.get_user_input_number("Please enter your selection here:")
if user_selection == 1:
    UserInterface.display_marketing_firm_menu_options()
elif user_selection == 2:
    UserInterface.display_sweepstakes_selection_menu()