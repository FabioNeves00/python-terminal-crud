from cmath import log
from typing import List
from modules.Storage import loadDatabase
from modules.types.User import User


def query(key: str, value: str) -> list[User] or str:
    try:
        response = []
        data = loadDatabase()
        for i in data:
            if(value.lower() in i[key].lower()):
                response.append(i)
        return "Not found in storage" if len(response) == 0 else response
    except KeyError:
        return "Query key not found in storage."