from modules.Storage import loadDatabase, writeDatabase
from modules.types.User import User


def handleInteraction(newUsers: list[User]) -> str:
    for user in newUsers:
        createUser(user)

def createUser(newUser: User) -> str:
    """Creates a user in the database: newUser is a User object"""
    try:
        storageArr = loadDatabase()
        storageArr.append(newUser)
        writeDatabase(storageArr)
        return 'Success.'
    except:
        return 'An error has occurred try again.'
    
    