from modules.Interaction import handleInteraction
from modules.Query import query

listOfUsers = []


def interactionMenu():
    user = {
        "cpf": input('Type the users cpf (0 to cancel): '),
        "name": input('Type the users name(0 to cancel): '),
        "address": input('Type the users address (0 to cancel): ')
    }
    if user["cpf"] != "0" or user["name"] != "0" or user["address"] != "0":
        listOfUsers.append(user)
        choice = input('Want to add another? (y/n) ')
        if choice == "" or choice == "y":
            interactionMenu()
        handleInteraction(listOfUsers)
        menu()
    else:
        menu()

    
    
def queryMenu():
    queryKey = input("Choose a key to search into:\n1) CPF\n2) Name\n3) Address\n--------\nb) Back to main menu\nn) Exit\n\nChoice: ")
    if queryKey == "b":
        menu()
        return
    queryValue = input("\nEnter your search: ")
    if queryKey == "1":
        return query('cpf', queryValue)
    elif queryKey == "2":
        return query('name', queryValue)
    elif queryKey == "3":
        return query('address', queryValue)
    else:
        return


def mainMenu() -> str:
    """Display the users main menu and returns his choice; 1 for interaction menu 2 for query menu and any other to exit"""
    return input('What do you want to do:\n1) Create a user\n2) Search\n--------\nn) Exit\n\nChoice: ')


def menu():
    choice = mainMenu()
    if choice == "1":
        interactionMenu()
    elif choice == "2":
        query = queryMenu()
        print(query)
        menu()
    else:
        print("Goodbye!")