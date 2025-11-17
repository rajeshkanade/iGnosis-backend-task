import os
import json


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE_PATH = os.path.join(BASE_DIR, "users.json")


def ensure_user_file():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f, indent=4)


def read_users():
    ensure_user_file()
    with open(FILE_PATH, "r") as f:
        return json.load(f)


def write_users(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
