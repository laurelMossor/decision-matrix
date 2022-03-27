""" Decision Matrix program, 
take in user input and output the best choice based on user-generated characteristics"""

# Decision class?
class Decision:
    """Holds all characteristics of the decision"""
    def __init__(self):
        self.options = []
        self.criteria = []
        self.user_decision = ""
    
    def add_option(self, option):
        self.options.append(option)
    
    def add_criteria(self, criterion):
        self.criteria.append(criterion)
    
    def add_decision(self, decision):
        self.user_decision = decision



# To begin, a user is greeted and given information and options about how to proceed
def greet_user():
    """Greet the user and assign name"""
    print("Hello and welcome to the Decision Matrix. Let's break down a difficult choice in some parts. \nTo start, what is your name?")
    user_name = input("My name is... ")
    print(f"Great. Nice to meet you {user_name.title()}")
    # Add option to verify if that's right

    return user_name

# While loop to identify choice
def identify_decision(user_name):
    print("""What is it you're here to accomplish? For example: \nI need to...
    ...select the best candidate.
    ...pick out a new dresser.
    ...buy a new car.
    ...choose where to go to school.""")
    print()
    print(f"{user_name}, what do you need to make a decision about?")

    while True:
        user_decision = input("I need to... ")
        print(f"You need to {user_decision}, is that correct? [Y/N]")
        choice = input("> ").upper()
        if choice == "Y":
            print("Great, let's move on.")
            break
        if choice == "N":
            continue
        else:
            print("Please select Y or N.")
    
    x.add_decision(user_decision)

# While loop to identify all characteristics
x = Decision()


def main():
    """Commenting out successful code and hardcoding answers as I go on"""
    user_name = greet_user()
    # user_name = "Laurel"
    identify_decision(user_name)
    # x.add_decision("buy a car")



main()