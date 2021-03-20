from card import Card
from quiz import Quiz
import json

file_name = input("Which file do you want to use? (example.json) ")
file = "packs/" + file_name if file_name else "packs/example.json"

with open(file, encoding='utf8') as file:
    data = json.load(file)

card_objects = []

for dictionary in data:
    card_objects.append(Card(dictionary))

# TODO - Display valid categories, and prompt user until two valid categories are chosen.
show = input("Which side do you want to see? ")
guess = input("Which side do you want to guess? ")

quiz = Quiz(card_objects, show, guess)
quiz.start()
