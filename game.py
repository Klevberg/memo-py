from card import Card
from quiz import Quiz

import os.path

import json


while True:

    file_name = input("Which file do you want to use? (example.json) ")
    file = "packs/" + file_name if file_name else "packs/example.json"

    if not os.path.isfile(file):
        print(f"Error: The file {file} does not exist.")
        continue
    
    if file.endswith(".json"):
        file_type = "json"
    else:
        print("Error: Must be a json file.")
        continue

    try:
        with open(file, encoding='utf8') as file:
            data = json.load(file)
        break
    except IOError:
        print("Error: Something went wrong when trying to open the file.")


card_objects = []

for dictionary in data:
    card_objects.append(Card(dictionary))

# TODO - Display valid categories, and prompt user until two valid categories are chosen.
show = input("Which side do you want to see? ")
guess = input("Which side do you want to guess? ")

quiz = Quiz(card_objects, show, guess)
quiz.start()
