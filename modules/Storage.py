from array import array
from inspect import _void
import json
import pathlib
from typing import TypedDict
from modules.types.User import User


DATABASE = f"{pathlib.Path().resolve()}/storage.json"


def loadDatabase() -> list[User] | list:
    """Loads the database and converts from JSON to dict"""
    storedArr = []
    with open(DATABASE, 'r') as db:
        storedArr = json.load(db)
    return storedArr


def writeDatabase(storedArr: list[User]) -> _void:
    """Writes in the database and converts from dict to JSON"""
    with open(DATABASE, 'w') as json_file:
        json.dump(storedArr, json_file, 
                            indent=4,  
                            separators=(',',': '))
    return