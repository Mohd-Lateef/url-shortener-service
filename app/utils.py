from . import models

Characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def Base62(id: int):
    code = ""
    while id != 0:
        remainder = id % 62
        code += Characters[remainder]
        id //= 62
    return code[::-1]


def checkIfExists(url : str,db):
    return db.query(models.URLModel).filter(models.URLModel.original_url == url).first()