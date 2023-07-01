tuple = {
    "type": "TP",
    "locked": False,
    "typelock": None,
}

page = {
    "type": "PG",
    "locked": False,
    "typelock": None,
    "tuples": []
}

table = {
    "type": "TB",
    "locked": False,
    "typelock": None,
    "pages": []
}

area = {
    "type": "AR",
    "locked": False,
    "typelock": None,
    "tables": []
}

database = {
    "type": "DB",
    "locked": False,
    "typelock": None,
    "areas": []
}

for dbs in range(0, 2):
    database["areas"].append(area)
    database["areas"][dbs]["tables"].append(table)
    database["areas"][dbs]["tables"][dbs]["pages"].append(page)
    database["areas"][dbs]["tables"][dbs]["pages"][dbs]["tuples"].append(tuple)

# print(database)