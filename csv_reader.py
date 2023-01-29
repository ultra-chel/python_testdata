import json
import math

from csv import DictReader
from files import CSV_FILE_PATH
from files import JSON_FILE_PATH
from files import JSON_RESULT_FILE_PATH

with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

with open(CSV_FILE_PATH, newline='') as d:
    reader = DictReader(d)
    books = []
    for row in reader:
        books.append(row)
    count_books = math.floor(len(books) / len(users))

result = []
for user in users:
    user_books = []
    user_result = {"name": user.get("name"), "gender": user.get("name"), "address": user.get("address"),
                   "age": user.get("age")}
    for i in range(count_books):
        user_books.append(books.pop())

    user_result["books"] = user_books
    result.append(user_result)

i = 0
for user in result:
    user_books = books.pop()
    if len(books) == 0:
        break
    user["books"].append(user_books)
    result[i] = user
    i += 1

with open(JSON_RESULT_FILE_PATH, "w") as f:
    s = json.dumps(result, indent=4)
    f.write(s)
