""" Decision Matrix program, 
take in user input and output the best choice based on user-generated characteristics"""

# Decision class?
class Decision:
    """Holds all characteristics of the decision"""
    def __init__(self):
        self.options = []
        self.criteria = []
        self.choice = ""
    
    def add_option(self, option):
        self.options.append(option)
    
    def add_criteria(self, criterion):
        self.criteria.append(criterion)



# To begin, a user is greeted and given information and options about how to proceed
def greet_user():
    """Greet the user and assign name"""
    print("Hello and welcome to the Decision Matrix. Let's break down a difficult choice in some parts. \nTo start, what is your name?")
    user_name = input("My name is... ")
    print(f"Great. Nice to meet you {user_name.title()}")
    # Add option to verify if that's right

    return user_name

# While loop to identify choice
def identify_choice():
    print("""What is it you're here to accomplish? For example: 
I need to...
    ...select the best candidate.
    ...pick out a new dresser.
    ...buy a new car.
    ...choose where to go to school.""")




# While loop to identify all characteristics

def main():
    user_name = greet_user()
    identify_choice()


main()